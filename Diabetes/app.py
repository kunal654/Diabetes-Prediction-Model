from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load and prepare the dataset
diabetes_dataset = pd.read_csv("diabetes.csv")
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [
        request.form['pregnancies'],
        request.form['glucose'],
        request.form['bloodPressure'],
        request.form['skinThickness'],
        request.form['insulin'],
        request.form['bmi'],
        request.form['dpf'],
        request.form['age']
    ]
    input_data = np.asarray(input_data, dtype=float).reshape(1, -1)
    input_data = scaler.transform(input_data)
    prediction = classifier.predict(input_data)
    result = "You are a diabetic person." if prediction[0] == 1 else "You are not a diabetic person."
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
