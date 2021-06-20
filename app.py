from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

messages = [
    {'name': 'Tcigam', 'message': 'Zdarova Kirill'}, 
    {'name': 'Xoce', 'message': 'Здравствуйте'},
    {'name': 'Derreck', 'message': 'How do you do'}
]

# @app.route('/api')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index1.html')


# @app.route('/message')
# def message():
#     message = request.form['name']
#     print(message)
#     return True

@app.route('/api', methods=['GET', 'POST'])
def index2():
    # if request.method == 'POST':
    #     sms = request.json['sms']
    #     name = request.json['name']
    #     messages.append({'name': name, 'message': sms})
    
    content = request.get_json()
    print(content)
    return jsonify(messages)


app.run(debug=True)