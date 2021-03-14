'''
Flask
request
render_templete
'''

from flask import Flask, request, render_template

# Application declaration
app = Flask(__name__)


# Start an application and declarate the main function
@app.route('/')
def main():
    return render_template('app.html')


# Clarification of route
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']
        choice = request.form['choice']

        if choice == 'addition':
            oper_value = x + y
            return render_template('app.html', sum=sum)

        elif choice == 'subtraction':
            oper_value = x - y
            return render_template('app.html', sum=sum)

        elif choice == 'multiplication':
            oper_value = x * y
            return render_template('app.html', sum=sum)

        elif choice == 'division':
            oper_value = x / y
            return render_template('app.html', sum=sum)

        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run() 
