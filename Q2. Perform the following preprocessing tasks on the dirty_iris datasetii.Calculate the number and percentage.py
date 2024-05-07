# Q2. Perform the following preprocessing tasks on the dirty_iris datasetii.
# i) Calculate the number and percentage of observations that are complete.
# ii) Replace all the special values in data with NA.
# iii) Define these rules in a separate text file and read them. (Use editfile function in R
# (package editrules). Use similar function in Python). Print the resulting constraint object. –
# Species should be one of the following values: setosa, versicolor or virginica. – All
# measured numerical properties of an iris should be positive. – The petal length of an iris is
# at least 2 times its petal width. – The sepal length of an iris cannot exceed 30 cm. – The
# sepals of an iris are longer than its petals.
# iv)Determine how often each rule is broken (violatedEdits). Also summarize and plot the
# result.
# v) Find outliers in sepal length using boxplot and boxplot.stats
# Code :
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dirty_iris dataset

dirty_iris = pd.read_csv("dirty_iris.csv")

# Task (i): Calculate the number and percentage of complete observations
complete_obs = dirty_iris.dropna()
num_complete_obs = len(complete_obs)
total_obs = len(dirty_iris)
percentage_complete = (num_complete_obs / total_obs) * 100
print("Number of complete observations:", num_complete_obs)
print("Percentage of complete observations:", percentage_complete)



# Task (ii): Replace special values with NA
dirty_iris.replace(["?", "!", "#", "*"], pd.NA, inplace=True)


# Task (iii): Read rules from a separate text file
def read_rules(file_path):
with open(file_path, "r") as file:
rules = file.readlines()
return [rule.strip() for rule in rules]


# Define a function to check if a value breaks the rules
def check_rules(df, rules):
violations = []
species_violations = 0
non_positive_violations = 0
petal_length_violations = 0
sepal_length_violations = 0
sepal_petal_violations = 0

for rule in rules:
feature, condition = rule.split(":", 1) # Split only at the first colon
feature = feature.strip()
condition = condition.strip()

# Check if the condition is violated
if "species" in feature.lower():
valid_species = {"setosa", "versicolor", "virginica"}
species_violations = (
df["Species"].str.lower().isin(valid_species) == False
).sum()
elif "properties" in feature.lower():
numeric_columns = df.select_dtypes(include="number").columns
for col in numeric_columns:
non_positive_violations += (df[col] <= 0).sum()
elif "petal length" in feature.lower():
petal_length_violations = (df["Petal.Length"] < 2 *

df["Petal.Width"]).sum()
elif "sepal length" in feature.lower():
sepal_length_violations = (df["Sepal.Length"] > 30).sum()
elif "sepals" in feature.lower():
sepal_petal_violations = (df["Sepal.Length"] <=

df["Petal.Length"]).sum()

return (
species_violations,
non_positive_violations,
petal_length_violations,
sepal_length_violations,
sepal_petal_violations,
)

# Read rules from the text file
rules_file = "iris_rules.txt"
rules = read_rules(rules_file)


# Task (iv): Determine how often each rule is broken
(
species_violations,
non_positive_violations,
petal_length_violations,
sepal_length_violations,
sepal_petal_violations,
) = check_rules(dirty_iris, rules)



# Task (v): Find outliers in sepal length using boxplot
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Box plot
sns.boxplot(data=dirty_iris.drop(columns="Species"), ax=axes[0])
axes[0].set_title("Boxplot of Numerical Properties")

# Bar plot
rule_break_frequency = {
"Species Violations": species_violations,
"Non-Positive Violations": non_positive_violations,
"Petal Length Violations": petal_length_violations,
"Sepal Length Violations": sepal_length_violations,
"Sepal Petal Violations": sepal_petal_violations,
}

axes[1].bar(rule_break_frequency.keys(), rule_break_frequency.values())
axes[1].set_title("Frequency of Rule Violations")

plt.show()