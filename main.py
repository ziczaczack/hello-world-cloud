from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    num1 = request.args.get('num1', default='0', type=int)
    num2 = request.args.get('num2', default='0', type=int)
    
    # Perform addition
    result = num1 + num2
    
    return f'The sum of {num1} and {num2} is {result}'

if __name__ == '__main__':
    app.run()