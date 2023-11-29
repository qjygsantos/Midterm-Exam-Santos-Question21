from flask import Flask, jsonify, request 
app = Flask(__name__) 

#1
hearts = [
    {
        "heart_id":"heart1",
        "date": "29/11/23",
        "heart_rate":"80bpm"
    },
    {
        "heart_id":"heart2",
        "date": "30/11/23",
        "heart_rate":"120bpm"
    },
    {
        "heart_id":"heart3",
        "date": "1/12/23",
        "heart_rate":"140bpm"
    }
]

#2
@app.route("/hearts", methods = ['Get'])
def getHearts():
    return jsonify(hearts)
#3



#4

@app.route("/hearts", methods=['POST']) 
def add_hearts():     
    heart = request.get_json()     
    hearts.append(hearts)     
    return {'id': len(hearts)}, 200 


#5
@app.route('/hearts/<int:index>', methods=['DELETE']) 
def delete_heart(index):     
    hearts.pop(index)     
    return 'The heart rate has been deleted', 200 
    
    
if __name__ == "__main__":     
    app.run()
