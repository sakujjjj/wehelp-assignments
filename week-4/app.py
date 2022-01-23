from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app=Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key="any string but secret"

@app.route("/")
def index():

    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    # name=request.args.get("name", "")
    # password=request.args.get("password", "")
    
    username=request.form["name"]
    userpwd =request.form["password"]
    
    if username and userpwd:
        if username == "test" and userpwd == "test":
            session["state"]="login"
            #驗證成功
            return redirect("/member/")
        else:
        # 驗證失敗
            return redirect("http://127.0.0.1:3000/error/?message=keyerror")
    else: 
        return redirect("http://127.0.0.1:3000/error/?message=keynone")

@app.route("/signout")
def signout():
    session["state"]=""
    return render_template("index.html")


@app.route("/member/")
def member():
    if session["state"] == "login":
        return render_template("login.html")
    else: 
        return render_template("index.html")

@app.route("/error/")
def error():
    # 抓到要求字串
    message=request.args.get("message")
    # 如果要求字串 = error 回傳"帳號 密碼錯誤"
    if message == "keyerror":
        return render_template("keyerror.html")
    elif message == "keynone":
        return render_template("keynone.html")
    # return "登入失敗"



@app.route("/calculate", methods=["post"])
def calculate():
    # maxNumber=request.args.get("max", "")
    # maxNumber=int(maxNumber)
    maxNumber=request.form["max"]
    maxNumber=int(maxNumber)
    result=0
    for n in range(maxNumber+1):
        result+=n
        
    return render_template("result.html", data=result)
    



@app.route("/getSum")
def getSum():
    name=request.args.get("max","None")

    # data=request.args.get("max","None")
    return name+"hi"


app.run(port=3000)