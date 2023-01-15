import requests
from flask import Flask,render_template,url_for
from flask import request as req
from transformers import pipeline
summarizer = pipeline("summarization")


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method== "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer api_cDqsshiYYdsPmHybqxvnlZYIctoHFwMovw"}

        data=req.form["data"]

        maxL=int(req.form["maxL"])
        minL=maxL//4
        output=summarizer(data, max_length=maxL, min_length=minL, do_sample=False)[0]

        print(output)
        return render_template("index.html",result=output["summary_text"])
    else:
        return render_template("index.html")
app.run()
