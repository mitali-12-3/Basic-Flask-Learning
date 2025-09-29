from flask import Flask, request
app= Flask(__name__)

@app.route("/")
def home():
    return 'Hello Bitches! I am trying to learn shit'

@app.route("/about")
def about():
    return 'About me? Bitches'

@app.route("/contact")
def contact():
    return 'Bitch Pleaseeeeeee! Lamborghini Keysss'

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        return "You unemployed bitch sent me stuff"
    else:
        return "What you looking at mf?"