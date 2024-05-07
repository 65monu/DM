# Q5. Use Naive bayes, K-nearest, and Decision tree classification algorithms and build
# classifiers. Divide the data set into training and test set. Compare the accuracy of the
# different classifiers under the following situations:
# 5.1 a) Training set = 75% Test set = 25%
# b) Training set = 66.6% (2/3rd of total), Test set = 33.3%
# 5.2 Training set is chosen by
# i) hold out method
# ii) Random subsampling
# iii) Cross-Validation. Compare the accuracy of the classifiers obtained.
# 5.3 Data is scaled to standard format.
# Code 5.1 :

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Define different training/test set splits
splits = [
('75/25 split', 0.25),



('66.6/33.3 split', 1/3)
]

# Initialize classifiers
classifiers = {
'Naive Bayes': GaussianNB(),
'K-nearest neighbors': KNeighborsClassifier(),
'Decision tree': DecisionTreeClassifier()
}

# Iterate over each split
for split_name, test_size in splits:
# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
random_state=42)

print(f"\nTraining and test set split: {split_name}")

# Train and evaluate each classifier
for classifier_name, classifier in classifiers.items():
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of {classifier_name}: {accuracy:.4f}")
Output of the 5.1 question is as follow : -



Code 5.3 :
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np

# Initialize classifiers
classifiers = {
'Naive Bayes': GaussianNB(),
'K-nearest neighbors': KNeighborsClassifier(),
'Decision tree': DecisionTreeClassifier()
}

# Define training set selection methods
methods = {
'Holdout method': train_test_split,
'Random subsampling': train_test_split,
'Cross-Validation': cross_val_score
}

# Define scaling methods
scaling_methods = {
'No scaling': None,
'Standard scaling': StandardScaler()
}

# Define evaluation metrics
evaluation_metrics = {
'Holdout method': accuracy_score,
'Random subsampling': accuracy_score,
'Cross-Validation': np.mean
}

# Iterate over each training set selection method and scaling method
for method_name, method in methods.items():

for scaling_name, scaling_method in scaling_methods.items():
# Split the dataset or perform cross-validation
if method_name == 'Cross-Validation':
X_scaled = X if scaling_method is None else

scaling_method.fit_transform(X)

for classifier_name, classifier in classifiers.items():
scores = cross_val_score(make_pipeline(scaling_method,

classifier), X_scaled, y, cv=5)

accuracy = np.mean(scores)
print(f"Accuracy of {classifier_name} with {method_name} and

{scaling_name}: {accuracy:.4f}")
else:
X_train, X_test, y_train, y_test = method(X, y, test_size=0.25,

random_state=42)

# Scale the data
if scaling_method is not None:
X_train = scaling_method.fit_transform(X_train)
X_test = scaling_method.transform(X_test)
# Train and evaluate each classifier
for classifier_name, classifier in classifiers.items():
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = evaluation_metrics[method_name](y_test, y_pred)
print(f"Accuracy of {classifier_name} with {method_name} and

{scaling_name}: {accuracy:.4f}")