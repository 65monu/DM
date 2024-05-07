# 1. Create a file “people.txt” with the following data

# i) Read the data from the file “people.txt”.
# ii) Create a ruleset E that contain rules to check for the following conditions:
# 1. The age should be in the range 0-150.
# 2. The age should be greater than yearsmarried.
# 3. The status should be married or single or widowed.
# 4. If age is less than 18 the agegroup should be child, if age is between 18 and 65 the
# agegroup should be adult, if age is more than 65 the agegroup should be elderly.
# iii) Check whether ruleset E is violated by the data in the file people.txt.
# iv) Summarize the results obtained in part (iii)
# v) Visualize the results obtained in part (iii)
# Code :
import pandas as pd

# Create the data
data = {
"Age": [21, 2, 18, 221, 34],
"agegroup": ["adult", "child", "adult", "elderly", "child"],
"height": [6.0, 3, 5.7, 5, -7],
"status": ["single", "married", "married", "widowed", "married"],
"yearsmarried": [-1, 0, 20, 2, 3],
}

# Create a DataFrame
df = pd.DataFrame(data)

3

# Save the DataFrame to a file
df.to_csv("people.txt", sep="\t", index=False)

# Read data from the file
data = pd.read_csv("people.txt", delim_whitespace=True)

# Define ruleset E
def ruleset_E(data):
violations = []

# Rule 1: Age should be in the range 0-150
age_violations = data[(data["Age"] < 0) | (data["Age"] > 150)]
if not age_violations.empty:
violations.append("Age should be in the range 0-150")

# Rule 2: Age should be greater than yearsmarried
age_years_married_violations = data[data["Age"] <= data["yearsmarried"]]
if not age_years_married_violations.empty:
violations.append("Age should be greater than yearsmarried")

# Rule 3: Status should be married, single, or widowed
status_violations = data[~data["status"].isin(["married", "single",
"widowed"])]
if not status_violations.empty:
violations.append("Status should be married, single, or widowed")

# Rule 4: Determine age group
age_group_violations = data[
~(
(data["Age"] < 18) & (data["agegroup"] == "child")
| (
(data["Age"] >= 18)
& (data["Age"] <= 65)
& (data["agegroup"] == "adult")
)

4

| ((data["Age"] > 65) & (data["agegroup"] == "elderly"))
)
]
if not age_group_violations.empty:
violations.append("Incorrect age group")

return violations

# Check violations using ruleset E
violations = ruleset_E(data)

# Summarize results
if violations:
print("Violations detected:")
for violation in violations:
print("- ", violation)
else:
print("No violations detected")
# Visualize the results
import matplotlib.pyplot as plt

# Count violations per rule
rule_counts = {}
for violation in violations:
rule = violation.split(":")[0]
if rule in rule_counts:
rule_counts[rule] += 1
else:
rule_counts[rule] = 1
# Plot violations per rule
plt.bar(rule_counts.keys(), rule_counts.values())
plt.xlabel("Rule")
plt.ylabel("Violation Count")
plt.title("Violations per Rule")
plt.show()
