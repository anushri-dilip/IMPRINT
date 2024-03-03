import secrets
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', image_url='images/bg.jpg')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve form data
    electricity = float(request.form['electricity']) / 1000  # Convert kWh to MWh
    water = float(request.form['water']) / 1000  # Convert gallons to cubic meters
    food_items = request.form['food'].split(',')  # Split food items by comma
    car_usage = float(request.form['car_usage']) / 1000  # Convert miles to kilometers
    bike_usage = float(request.form['bike_usage']) / 1000  # Convert miles to kilometers

    # Calculate carbon emissions for each input
    # Conversion factors:
    # 1 MWh of electricity = 0.5 metric tonnes of CO2
    # 1 cubic meter of water = 0.1 metric tonnes of CO2
    # Car usage = 0.2 metric tonnes of CO2 per kilometer
    # Bike usage = 0.05 metric tonnes of CO2 per kilometer
    carbon_electricity = electricity * 0.5
    carbon_water = water * 0.1
    carbon_car = car_usage * 0.2
    carbon_bike = bike_usage * 0.05

    # Calculate carbon emissions for food consumption
    # Assume vegetarian diet has lower carbon emissions
    if 'meat' in food_items:
        carbon_food = 0.5  # High carbon emissions for meat consumption
    else:
        carbon_food = 0.2  # Lower carbon emissions for vegetarian diet

    # Calculate total carbon footprint
    total_carbon_footprint = carbon_electricity + carbon_water + carbon_food + carbon_car + carbon_bike
    
    print("Total carbon footprint:", total_carbon_footprint)  # Print total carbon footprint for debugging
    
    # Determine message based on total carbon footprint
    if total_carbon_footprint < 5:
        message = "It's good. Keep it up!"
        suggestions = []
    elif total_carbon_footprint == 5:
        message = "There's room for improvement. Consider the following ways to decrease carbon emissions:"
        suggestions = [
            "Switch to energy-efficient appliances",
            "Reduce water usage by fixing leaks",
            "Use public transportation or carpooling more often",
            "Opt for walking or biking for short distances"
        ]
    else:
        message = "It's above the recommended usage. Consider the following ways to decrease carbon emissions:"
        suggestions = [
            "Reduce meat consumption",
            "Use renewable energy sources",
            "Plant trees to offset carbon emissions",
            "Reduce car usage by combining trips or using alternative transportation"
        ]

    return render_template('result.html', total_carbon_footprint=total_carbon_footprint, message=message, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)



