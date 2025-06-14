# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15hSWUvwhslWSkep4ooQMZF5dzt_-Fj4Z
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import warnings
warnings.filterwarnings('ignore')

df =pd.read_csv('diabetes.csv')

df.head()

number_column_names= df.select_dtypes(include=['number']).columns
print("numerical column names:",number_column_names.tolist())

object_column_names =df.select_dtypes(include=['object']).columns
print("object column names:", object_column_names.tolist())

df.describe().T

df[df['Pregnancies']==0].shape

df[df['Glucose']==0].shape

df = df.loc[(df[['Pregnancies', 'Glucose', 'BloodPressure']] != 0).all(axis=1)]
df.loc[df['SkinThickness']==0,'SkinThickness']=df['SkinThickness'].mean()
df.loc[(df['Insulin']!=0),'InsulinKnown']=1
df.loc[(df['Insulin']!=0),'InsulinKnown']=1