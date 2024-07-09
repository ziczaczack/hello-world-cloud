from flask import Flask, request, render_template, flash

app = Flask(__name__)

@app.route('/')
def hello():    
    return render_template("homepage.html")

if __name__ == '__main__':
    app.run()