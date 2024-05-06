"""
This module contains a Flask application for temperature conversion 
and serves as the main entry point.
"""

import uuid
from flask import Flask
import tensorflow as tf

# Loading the TensorFlow SavedModel
model = tf.saved_model.load("\tf_model\saved_model.pb")

# Creating a Flask application instance
app = Flask(__name__)

# Generating a Universally Unique Identifier (UUID) using the built-in uuid module
app_id = uuid.uuid4()

# Defining a home route
@app.route("/")
def application_home():
    """
    Route handler for the root URL ("/").
    Returns a JSON response containing the application ID.
    """
    return {'app id': app_id}, 200

# Defining a route for the temperature conversion with dynamic parameter
@app.route("/convert/<fahrenheit>")
def temp_convert(fahrenheit):
    """
    Route handler for URL pattern "/convert/<fahrenheit>".
    Converts Fahrenheit temperature to Celsius and returns the result 
    along with the application ID.
    """
    try:
        fahrenheit = float(fahrenheit)

        # Calculating Celsius temperature
        celsius = (fahrenheit - 32) * 5/9

        # Returning a JSON response containing the Celsius temperature and the application ID
        return {'celsius': celsius, 'app id': app_id}, 200

    except ValueError:
        # Handling the case where the input cannot be converted to a float
        return {"Error": "Invalid input"}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 
    '''
    Makes the Flask application accessible on port 8080 from within the container
    Allows the application to listen on all available network interfaces within the container.
    '''
    

