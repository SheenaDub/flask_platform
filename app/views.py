from flask import render_template

from systeminfocookie import sys1

from app import app


@app.route('/')
def index():
    output = sys1.main()
    returnDict = {}
    returnDict['platform']=output
    returnDict['title']='Home'
    return render_template("index.html", **returnDict)
    