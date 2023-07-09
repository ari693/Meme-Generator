from flask import Flask, render_template
import requests
import json

app=Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.get(url).text)
    meme_large = response.get("preview")[-2] if response.get("preview") else ""
    subreddit = response["subreddit"]
    return meme_large, subreddit





@app.route("/")
def index():
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)
app.run(host="0.0.0.0",port=80)