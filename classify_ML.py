import numpy as np, pandas as pd, os, re, math
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

class Classify_Model:
    def __init__(self):
        self.svm = self.create_model()

    def create_model(self):
        load_dotenv()
        DATA_FILE = os.getenv("data_file")
        df = pd.read_csv(DATA_FILE)
        X = df.drop('Number', axis=1)
        Y = df['Number']
        X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
        clf_svm = LinearSVC(penalty='l2', dual=False, tol=0.001)
        clf_svm.fit(X_train, Y_train)
        return clf_svm
    
    def predict(self, input_df):
        try:
            output = self.svm.predict(input_df)
            output = int(output[0])
            return output
        except:
            return None
