import numpy as np
import pandas as pd                                 
from flask import Flask, request, jsonify, render_template
import pickle


model = pickle.load(open(r'C:\Users\ADMIN\OneDrive\Desktop\Loan-defaulter-Webapp-main\loandef.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('user.html')
@app.route('/predict', methods=['POST'])
def predict():
     employed = int(request.form['employed'])
     balance = float(request.form['balance'])
     salary = float(request.form['salary'])

        # Create a DataFrame from the user input
     user_df = pd.DataFrame({'Employed': [employed], 'Bank Balance': [balance], 'Annual Salary': [salary]})

        # Use the trained classifier to predict the outcome
     prediction = model.predict(user_df)
     output=prediction[0]
     if output==0:
         return render_template('result.html', prediction_text='he doesnot default')
     else:
          return render_template('result1.html', prediction_text='he may default')
         
if __name__ == "__main__":
    app.run(debug=True)


       
        

    
