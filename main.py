from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home:
    return render_template('home.html')

@app.route('/print', methods=['POST'])
def print():
    return 'Print Page'

if __name__ == '__main__':
    app.run(debug=True)

