from flask import Flask, request
from mega import Mega

app = Flask(__name__)


@app.route('/')
def index():
    from mega import Mega
    megaa = Mega()
    data = request.json
    if data is None:
        return "Hi"
    try:
        email = data['email']
        pwd = data['pwd']
    except:
        return "Please Use Json in Correct Format Given :-  { 'email' : 'Your Mail Here' , 'pwd' : 'Your Password " \
               "Here' } "
    try:
        m = megaa.login(email, pwd)
        q = m.get_storage_space(giga=True)
        used = str(q['used']) + " GB"
        total = str(int(q['total'])) + " GB"
        hit = True
    except:
        hit = False
    if hit:
        result = {"result": "success", "Used_Storage": used, "Total_Storage": total}
    else:
        result = {"result": "fail"}
    return str(result)

  
if __name__ == "__main__":
    app.run(threaded=True)
