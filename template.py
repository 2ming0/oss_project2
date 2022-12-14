#PLEASE WRITE THE GITHUB URL BELOW!
#https://github.com/2ming0/oss_project2

import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def load_dataset(dataset_path):
	#To-Do: Implement this function
	return pd.read_csv(dataset_path)

def dataset_stat(dataset_df):	
	#To-Do: Implement this function
    n_feats = dataset_df.shape[1] - 1
    n_class0 = len(dataset_df.loc[dataset_df['target'] == 0])
    n_class1 = len(dataset_df.loc[dataset_df['target'] == 1])
    return n_feats, n_class0, n_class1

def split_dataset(dataset_df, testset_size):
    #To-Do: Implement this function
    df_data = dataset_df.drop('target', axis=1)
    df_target = dataset_df['target']
    return train_test_split(df_data, df_target, test_size=testset_size)

def decision_tree_train_test(x_train, x_test, y_train, y_test):
    #To-Do: Implement this function
	dt = DecisionTreeClassifier()
	dt.fit(x_train, y_train)
	acc = accuracy_score(y_test,dt.predict(x_test))
	prec = precision_score(y_test,dt.predict(x_test))
	recall = recall_score(y_test,dt.predict(x_test))
	return acc, prec, recall

def random_forest_train_test(x_train, x_test, y_train, y_test):
    #To-Do: Implement this function
    rf = RandomForestClassifier()
    rf.fit(x_train, y_train)
    pred = rf.predict(x_test)
    
    acc = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    
    return acc, precision, recall

def svm_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
	pipe = make_pipeline(
		StandardScaler(),
		SVC()
	)
	pipe.fit(x_train, y_train)
	
	pred = pipe.predict(x_test)
 
	acc = accuracy_score(y_test, pred)
	prec = precision_score(y_test, pred)
	recall = recall_score(y_test, pred)
	
	return (acc, prec, recall)

def print_performances(acc, prec, recall):
	#Do not modify this function!
	print ("Accuracy: ", acc)
	print ("Precision: ", prec)
	print ("Recall: ", recall)

if __name__ == '__main__':
	#Do not modify the main script!
	data_path = sys.argv[1]
	data_df = load_dataset(data_path)

	n_feats, n_class0, n_class1 = dataset_stat(data_df)
	print ("Number of features: ", n_feats)
	print ("Number of class 0 data entries: ", n_class0)
	print ("Number of class 1 data entries: ", n_class1)

	print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
	x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))

	acc, prec, recall = decision_tree_train_test(x_train, x_test, y_train, y_test)
	print ("\nDecision Tree Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = random_forest_train_test(x_train, x_test, y_train, y_test)
	print ("\nRandom Forest Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = svm_train_test(x_train, x_test, y_train, y_test)
	print ("\nSVM Performances")
	print_performances(acc, prec, recall)