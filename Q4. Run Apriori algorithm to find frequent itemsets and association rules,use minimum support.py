# Q4. Run Apriori algorithm to find frequent itemsets and association rules
# 1.1 Use minimum support as 50% and minimum confidence as 75%
# 1.2 Use minimum support as 60% and minimum confidence as 60 %
# Code :
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

# Convert numerical features to categorical for Apriori algorithm
df_iris_bin = pd.DataFrame()
for col in df_iris.columns:
df_iris_bin[col] = pd.cut(df_iris[col], bins=3, labels=[f'{col}_low',
f'{col}_medium', f'{col}_high'])

# Find frequent itemsets with minimum support as 50% and minimum confidence as 75%
frequent_itemsets_1 = apriori(df_iris_bin, min_support=0.5, use_colnames=True)
rules_1 = association_rules(frequent_itemsets_1, metric="confidence",
min_threshold=0.75)

# Find frequent itemsets with minimum support as 60% and minimum confidence as 60%
frequent_itemsets_2 = apriori(df_iris_bin, min_support=0.6, use_colnames=True)
rules_2 = association_rules(frequent_itemsets_2, metric="confidence",
min_threshold=0.6)

# Print the results
print("Frequent Itemsets and Association Rules with minimum support as 50% and
minimum confidence as 75%:")
print(frequent_itemsets_1)
print(rules_1)

print("\nFrequent Itemsets and Association Rules with minimum support as 60% and
minimum confidence as 60%:")
print(frequent_itemsets_2)
print(rules_2)