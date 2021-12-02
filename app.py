from flask import Flask, json, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'contact': 2847384983,
        'title': u'Relative 1',
        'description': u'Lives in Mumbai',
        'done': False
    },
    {
        'contact': 7394574930,
        'title': u'Relative 1',
        'description': u'Lives in Mumbai',
        'done': False
    },
    {
        'contact': 8478748535,
        'title': u'Relative 1',
        'description': u'Lives in Mumbai',
        'done': False
    }
]

@app.route('/add-data', methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data !'
        },400)

    task = {
        'contact': tasks[-1]['contact']+1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'Task added successfully !!'
    })

#@app.route('/')
#def hello_world():
#    return 'Hello World'

@app.route('/')
def get_task():
    return jsonify({
        'data':tasks
    })

if(__name__ == '__main__'):
    app.run(debug=True)
                                      