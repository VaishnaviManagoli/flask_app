from flask import Flask,jsonify,request

app= Flask(__name__)

data= [
{
    
    'Contact':  "9987644456",
    'name': "Raju",
    'done': False,
    'id': 1
},
{
    'Contact':  "9876543222",
    'name': "Rahul",
    'done': False,
    'id': 2
}
]
@app.route("/")
def hello_world():
    return "hello world"
@app.route("/add-data",methods=["Post"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data!"
        },400)
    task={
        'id': data[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False
    }    
   
  