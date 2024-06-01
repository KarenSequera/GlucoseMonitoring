from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Placeholder for storing the previous glucose level and ISF (Insulin Sensitivity Factor)
previous_glucose_level = 100
ISF = 50  # Default ISF value, you can adjust it as needed

@app.route('/glucose', methods=['GET'])
def get_glucose():
    global previous_glucose_level
    
    # Generate a new glucose level based on the previous one
    new_glucose_level = generate_coherent_glucose(previous_glucose_level)
    
    # Update previous glucose level
    previous_glucose_level = new_glucose_level
    
    return jsonify({'glucose_level': new_glucose_level})

@app.route('/inject-insulin', methods=['POST'])
def inject_insulin():
    global previous_glucose_level
    
    # Get the units of insulin to be injected from the request
    data = request.get_json()
    units = data.get('units')
    
    # Decrease glucose level based on insulin units and ISF
    previous_glucose_level -= units * ISF
    
    return jsonify({'message': 'Insulin injected successfully'})

def generate_coherent_glucose(previous_glucose):
    # Generate a new glucose level that increases more slowly
    return previous_glucose + random.randint(1, 5)

if __name__ == '__main__':
    app.run(debug=True)