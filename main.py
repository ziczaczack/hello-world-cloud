from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, please enter two numbers in the URL like this: /add?num1=4&num2=5'

@app.route('/add')
def add_numbers():
    # Get the values of num1 and num2 from the query parameters
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    
    # Perform addition
    result = num1 + num2
    
    # Return the result as a string
    return f'The sum of {num1} and {num2} is {result}'

if __name__ == '__main__':
    app.run()
