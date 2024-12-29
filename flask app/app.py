from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('pay_fraud_predictor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        step = int(request.form['step'])
        payment_type = int(request.form['payment_type'])
        amount = float(request.form['amount'])
        oldbalance_org = float(request.form['oldbalance_org'])
        newbalance_orig = float(request.form['newbalance_orig'])
        oldbalance_dest = float(request.form['oldbalance_dest'])
        newbalance_dest = float(request.form['newbalance_dest'])
        
        input_point = np.array([[step, payment_type, amount, oldbalance_org, newbalance_orig, oldbalance_dest, newbalance_dest]])
        
        prediction = model.predict(input_point)
        
        if prediction[0] == 0:
            result = 'Your Transaction is Non-Frauded ✔️ (Authorised)'
        else:
            result = 'Your Transaction is Frauded ✖️ (Unauthorised)'
        
        return render_template('result.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)