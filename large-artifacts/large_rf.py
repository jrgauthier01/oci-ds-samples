#!/usr/bin/env python
# coding: utf-8


import sklearn
import joblib 
from sklearn.datasets import make_classification 

dataset = make_classification(n_samples=10000, n_features=75, n_informative=55, n_redundant=10, n_classes=10)

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=30000, max_depth=50, n_jobs=-1)

rf_model.fit(dataset[0], dataset[1])

joblib.dump(rf_model, 'rf.joblib')





