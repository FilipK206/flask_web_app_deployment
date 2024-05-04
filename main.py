from flask import Flask
import uuid

app = Flask(__name__)
app_id = uuid.uuid4()

@app.route("/")
def application_start():
    return {'app id': app_id}, 200

@app.route("/convert/<fahrenheit>")
def temp_convert(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        
        return {'celsius': celsius, 'app id': id}, 200
    
    except ValueError:
        return {"Error": "Invaild input"}, 400
    
if __name__ == '__main__':
    app.run(debug=True)
