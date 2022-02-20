from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import jsonify
import mysql.connector
import json

app=Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key="any string but secret"

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="website"
    )

    # print(request.form["name"])
    # print(request.form["account"])
    # print(request.form["password"])
    name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]

    mycursor = mydb.cursor()
    sql = "select * from member where account='"+account+"'"
    
    mycursor.execute(sql)
    results = mycursor.fetchall()
    # print(results)
    if len(results) == 0:
        mycursor = mydb.cursor()
        sql = "insert into member (username, account, password) value (%s, %s, %s)"
        val = (request.form["name"],request.form["account"],request.form["password"])
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("success.html")
    else:
        return redirect("http://127.0.0.1:3000/error/?message=fail")



@app.route("/signin", methods=["POST"])
def signin():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="website"
    )

    print(request.form["account"])
    print(request.form["password"])
    account=request.form["account"]
    password=request.form["password"]

    mycursor = mydb.cursor()
    #比對資料庫帳密
    sql = "select * from member where account='"+account+"' and password='"+password+"'"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    
    # print(results)
    # print(len(results))
    if len(results) == 1:
        session["state"]="login"
        
        mycursor = mydb.cursor()
        sql_name = "select username from member where account='"+account+"'"
        mycursor.execute(sql_name)
        myresult = mycursor.fetchall()
        
        #將陣列轉字串
        value = "".join('%s' %id for id in myresult)

        #將姓名存到session
        session["value"]=value
        return redirect("/member/")
    else:
        return redirect("http://127.0.0.1:3000/error/?message=keyerror")


@app.route("/signout")
def signout():
    session["state"]=""
    return render_template("index.html")


@app.route("/member/")
def member():
    if session["state"] == "login":
        value = session["value"]
        return render_template("test_login.html", value=value)

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
    elif message == "fail":
        return render_template("fail.html")


# -----------------------------
# data ={
#     "id":0,
#     "name":"Jack捷克"
# }
# memberdata = [data]
# -----------------------------
@app.route("/api/members", methods=["get"])
def members():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="website"
    )
    
    username=request.args.get("username")
    # print(request.args.get("username"))
    mycursor = mydb.cursor()
    sql = "select * from member where account='"+username+"'"
    # sql = "select * from member where account='John'"
    mycursor.execute(sql)
    results=mycursor.fetchall()
    # print(results)
    if len(results) == 1:
        # mycursor = mydb.cursor(dictionary=True, buffered=True)
        mycursor = mydb.cursor()
        #將mysql  資料轉成json格式輸出
        sql = "select json_object('id', id, 'name', username,'username', account) from member where account='"+username+"'"
        mycursor.execute(sql)
        results=mycursor.fetchone()
        #輸出型態為list 無法 return
        # print(results)
        print(results)
        print(type(results))

        #將tuple轉成STR
        results = "".join('%s' %id for id in results)
        print(results)
        print(type(results))

        # 將str轉成 dict
        eval(results),type(eval(results))
        print(eval(results))
        print(type(eval(results)))

        # 將字典加入KEYS:data
        dic={"data":eval(results)}
        print(dic)
        # dataresults = {"data": results}
        # print(dataresults)
        # print(type(dataresults))

        return dic
    else:
        dic={"data":"null"}
        print(dic)
        return dic

app.debug = True
app.run(port=3000)