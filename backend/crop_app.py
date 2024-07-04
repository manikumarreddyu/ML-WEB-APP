# import joblib
# from flask import Flask, render_template, request, redirect
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('Home_1.html')

# @app.route('/Predict')
# def prediction():
#     return render_template('Index.html')

# @app.route('/form', methods=["POST"])
# def brain():
#     Nitrogen=float(request.form['Nitrogen'])
#     Phosphorus=float(request.form['Phosphorus'])
#     Potassium=float(request.form['Potassium'])
#     Temperature=float(request.form['Temperature'])
#     Humidity=float(request.form['Humidity'])
#     Ph=float(request.form['ph'])
#     Rainfall=float(request.form['Rainfall'])
     
#     values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
#     if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
#         joblib.load('crop_appp','r')
#         model = joblib.load(open('crop_appp','rb'))
#         arr = [values]
#         acc = model.predict(arr)
#         # print(acc)
#         return render_template('prediction.html', prediction=str(acc))
#     else:
#         return "Sorry...  Error in entered values in the form Please check the values and fill it again"



# if __name__ == '__main__':
#     app.run(debug=True)

import joblib
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=["POST"])
def predict_crop():
    if request.method == 'POST':
        try:
            # Extract data from POST request
            data = request.get_json()
            Nitrogen = float(data['Nitrogen'])
            Phosphorus = float(data['Phosphorus'])
            Potassium = float(data['Potassium'])
            Temperature = float(data['Temperature'])
            Humidity = float(data['Humidity'])
            Ph = float(data['ph'])
            Rainfall = float(data['Rainfall'])
            
            # Validate input values
            if 0 < Ph <= 14 and Temperature < 100 and 0 < Humidity <= 100:
                # Load the machine learning model (adjust the path as needed)
                model = joblib.load('path_to_your_model.pkl')
                
                # Make prediction
                input_data = [[Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]]
                prediction = model.predict(input_data)[0]
                
                return jsonify({'prediction': prediction}), 200
            else:
                return jsonify({'error': 'Invalid input values. Please check and try again.'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
