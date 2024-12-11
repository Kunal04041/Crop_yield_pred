import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Define the root route to display the form
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Handle the prediction logic
@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    rainfall = float(request.form["rainfall"])
    temperature = float(request.form["temperature"])
    pesticides = float(request.form["pesticides"])
    crop = int(request.form["crop"])
    
    # Mock prediction logic (replace with your model's logic)
    crops = [
        "Cassava", "Maize", "Plantains and others", "Potatoes", 
        "Rice (paddy)", "Sorghum", "Soybeans", "Sweet potatoes", 
        "Wheat", "Yams"
    ]
    selected_crop = crops[crop]
    
    # Example prediction logic (to be replaced with your model)
    predicted_yield = rainfall * 0.1 + temperature * 0.2 - pesticides * 0.05 + crop * 2
    
    # Display result
    return f"<h1>Predicted Yield for {selected_crop}: {predicted_yield:.2f} tons</h1>"

if __name__ == "__main__":
    app.run(debug=True)
