from flask import Flask
import sys

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
       
        return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run()