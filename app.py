from flask import Flask, render_template
import random
#create the app 
app=Flask(__name__)

facts=["ABC","DEF","EFG","XYZ"]

# routes ---> www.xyx/a --> /b

@app.route("/")
def home():
    fact=random.choice(facts)
    return render_template("index.html",fact=fact)


if __name__=="__main__":
    app.run(debug=True)
