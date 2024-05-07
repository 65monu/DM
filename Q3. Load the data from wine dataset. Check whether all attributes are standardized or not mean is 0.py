# Q3. Load the data from wine dataset. Check whether all attributes are standardized or not
# (mean is 0 and standard deviation is 1). If not, standardize the attributes. Do the same
# with Iris dataset.
# Code :
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine, load_iris

# Load wine dataset
wine_data = load_wine()
wine_X = wine_data.data

# Standardize wine dataset
wine_scaler = StandardScaler()
wine_X_standardized = wine_scaler.fit_transform(wine_X)

# Check if all attributes are standardized
wine_mean = np.mean(wine_X_standardized, axis=0)
wine_std = np.std(wine_X_standardized, axis=0)

if np.allclose(wine_mean, 0) and np.allclose(wine_std, 1):
print("All attributes in the wine dataset are standardized.")
else:
print("Attributes in the wine dataset are not standardized. Standardizing...")

# Load Iris dataset
iris_data = load_iris()
iris_X = iris_data.data

# Standardize Iris dataset
iris_scaler = StandardScaler()
iris_X_standardized = iris_scaler.fit_transform(iris_X)

# Check if all attributes are standardized
iris_mean = np.mean(iris_X_standardized, axis=0)
iris_std = np.std(iris_X_standardized, axis=0)

if np.allclose(iris_mean, 0) and np.allclose(iris_std, 1):
print("All attributes in the Iris dataset are standardized.")
else:
print("Attributes in the Iris dataset are not standardized. Standardizing...")