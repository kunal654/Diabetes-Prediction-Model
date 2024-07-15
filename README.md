# Diabetes Prediction Model

This project implements a machine learning model to predict whether a person has diabetes based on various medical attributes. The model uses a Support Vector Machine (SVM) classifier and has been evaluated for accuracy on both training and test data.

## Table of Contents
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Prediction](#prediction)
- [Contributing](#contributing)
- [License](#license)

## Dataset
The dataset used in this project is the [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database), which contains several medical predictor variables and one target variable, `Outcome`. The predictor variables include:
- `Pregnancies`
- `Glucose`
- `BloodPressure`
- `SkinThickness`
- `Insulin`
- `BMI`
- `DiabetesPedigreeFunction`
- `Age`

The target variable `Outcome` is binary (0 or 1) indicating whether the patient is diabetic or not.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/kunal654/Diabetes-Prediction-Model.git
   cd Diabetes-Prediction-Model
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure you have the dataset (`diabetes.csv`) in the project directory.
2. Run the script:
   ```bash
   python diabetes_prediction.py
   ```

The script will load the dataset, preprocess the data, train the model, and allow you to input medical attributes to get a diabetes prediction.

## Model Training
The dataset is loaded into a pandas DataFrame, and the following steps are performed:
- Display basic statistics and structure of the data.
- Separate the data into features (`X`) and labels (`Y`).
- Standardize the feature data using `StandardScaler`.
- Split the data into training and testing sets.
- Train an SVM classifier with a linear kernel on the training data.

## Evaluation
The model is evaluated using accuracy scores on both the training and test datasets:
```python
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data:', training_data_accuracy)

test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data:', test_data_accuracy)
```

## Prediction
The script also allows user input for making predictions. It takes the following inputs:
- Number of pregnancies
- Glucose level
- Blood pressure
- Skin thickness
- Insulin level
- BMI
- Diabetes pedigree function
- Age

The inputs are standardized, and the model predicts whether the person is diabetic or not:
```python
if prediction[0] == 0:
  print('The person is not diabetic')
else:
  print('The person is diabetic')
```

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Developed by [Kunal Gautam](https://www.linkedin.com/in/kunal-gautam-2981b2292/)**  
[GitHub](https://github.com/kunal654)
