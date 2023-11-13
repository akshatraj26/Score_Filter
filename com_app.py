from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hi This is my second page. I am a Homosexual."

@app.route('/members')
def members():
    return "Everyone is accepted and welcomed here"

@app.route('/greetings')
def greetings():
    return "Good Morning! I am Akshat Raj."

if __name__ == '__main__':
    app.run(debug=True)
    

from flask import Flask, redirect, url_for 

app = Flask(__name__)


@app.route('/')
def members():
    return "Он никогда не полюбит меня. Он не гомосексуал."


@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is " + str(score)

# Check for results
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    
    if marks < 50:
        result = "fail"
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug=True)
    
      
