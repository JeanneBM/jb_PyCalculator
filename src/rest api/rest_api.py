from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('server.html')

@app.route('/case', methods=['POST'])
def case(oper_value=oper_value):
    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']
        choice = request.form['choice']

        if choice == 'addition':
            oper_value = x + y
            return render_template('server.html', oper_value=oper_value)

        elif choice == 'subtraction':
            oper_value = x - y
            return render_template('server.html', oper_value=oper_value)

        elif choice == 'multiplication':
            oper_value = x * y
            return render_template('server.html', oper_value=oper_value)

        elif choice == 'division':
            sum = x / y
            return render_template('server.html', oper_value=oper_value)
        
        else:
            return render_template('server.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
    
    
    
