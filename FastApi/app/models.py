import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

Xvar = ['EmpSatisfaction', 'SpecialProjectsCount', 'Absences']
Yvar = 'Termd'

MODEL_PATH = 'C:/Users/user/Desktop/DataScience/FastApi/models/logistic_regressiom.pkl'


def train_model():
    df = pd.read_csv(
        'C:/Users/user/Desktop/DataScience/FastApi/data/HR_Dataset Refresh.csv')

    X = df[Xvar]
    Y = df[Yvar]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y)

    model = LogisticRegression(
        solver='liblinear', random_state=42, class_weight='balanced')

    model.fit(X_train, Y_train)

    joblib.dump(model, MODEL_PATH)
    return model


def load_model():
    joblib.load(MODEL_PATH)
    
    
    
