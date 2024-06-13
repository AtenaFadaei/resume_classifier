import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


def EDA(path_to_data:str):
    """Perform explatory data analysis.
        - list columns
        -length of data
        - 

    Args:
        path_to_data: path to data file.
    """
    resumeDataSet = pd.read_csv(path_to_data ,encoding='utf-8')
    resumeDataSet['cleaned_resume'] = ''
    print(resumeDataSet.head())
    print(f"Length of data:{len(resumeDataSet)}")


def main():
    EDA("/mnt/c/Users/Atena/Documents/Training/NLP/projects/0_Resume_Screening_with_Python/data/UpdatedResumeDataSet.csv")
    

if __name__ == "__main__":
    main()