import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Improve the appearance of plots
sns.set_style("whitegrid")

# ==========================================
# Load Dataset
# ==========================================

# Read the customer churn dataset
df = pd.read_csv("Churn Data.csv")

# Display the first five records
print("\nFirst Five Records\n")

print(df.head())

# ==========================================
# Data Understanding
# ==========================================

# Number of rows and columns
print("Dataset Shape :", df.shape)

print()

# Display column names
print("Columns in Dataset:\n")

print(df.columns)

print()

# Display information about the dataset
df.info()

# ==========================================
# Data Cleaning
# ==========================================

# Replace blank spaces in TotalCharges with 0
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")

# Convert TotalCharges into float
df["TotalCharges"] = df["TotalCharges"].astype("float")

# Convert SeniorCitizen values into meaningful labels
df["SeniorCitizen"] = df["SeniorCitizen"].replace({
    0:"No",
    1:"Yes"
})

# Check missing values
print(df.isnull().sum())

print()

# Check duplicate rows
print("Duplicate Rows :", df.duplicated().sum())

# Check duplicate customer IDs
print("Duplicate Customer IDs :", df["customerID"].duplicated().sum())

# ============================================================
# Customer Churn Distribution
# ============================================================

# Create figure
plt.figure(figsize=(5,4))

# Plot customer churn count
ax = sns.countplot(x="Churn", data=df)

# Display count labels on bars
for container in ax.containers:
    ax.bar_label(container)

# Chart title
plt.title("Customer Churn Distribution")

# Axis labels
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")

# Show chart
plt.show()


# ============================================================
# Customer Churn Percentage
# ============================================================

# Count customers in each churn category
churn_counts = df["Churn"].value_counts()

# Create figure
plt.figure(figsize=(5,5))

# Plot pie chart
plt.pie(
    churn_counts,
    labels=churn_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#66b3ff", "#ff9999"]
)

plt.grid(False)

# Add title
plt.title("Customer Churn Percentage")

# Display chart
plt.show()


# ============================================================
# Gender vs Customer Churn
# ============================================================


# Create figure
plt.figure(figsize=(6,5))

# Plot count of male and female customers by churn status
ax = sns.countplot(x="gender", hue="Churn", data=df)

# Display count labels on each bar
for container in ax.containers:
    ax.bar_label(container)

# Add chart title
plt.title("Customer Churn by Gender")

# Label axes
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

# Display legend
plt.legend(title="Churn")

# Show chart
plt.show()


# ============================================================
# Senior Citizen vs Customer Churn
# ============================================================


# Create a cross-tabulation
churn_by_senior = pd.crosstab(df["SeniorCitizen"], df["Churn"])

# Create stacked bar chart
ax = churn_by_senior.plot(
    kind="bar",
    stacked=True,
    figsize=(6,5)
)

# Add count labels
for container in ax.containers:
    ax.bar_label(container, label_type="center", fontsize=9)

# Add chart title
plt.title("Customer Churn by Senior Citizen Status")

# Label axes
plt.xlabel("Senior Citizen")
plt.ylabel("Number of Customers")

# Rotate labels
plt.xticks(rotation=0)

# Display legend
plt.legend(title="Churn")

# Show chart
plt.show()

# ============================================================
# Partner vs Customer Churn
# ============================================================

# Create figure
plt.figure(figsize=(6,5))

# Plot Partner vs Churn
ax = sns.countplot(x="Partner", hue="Churn", data=df)

# Display count labels
for container in ax.containers:
    ax.bar_label(container)

# Add title
plt.title("Customer Churn by Partner Status")

# Label axes
plt.xlabel("Partner")
plt.ylabel("Number of Customers")

# Display legend
plt.legend(title="Churn")

# Show chart
plt.show()


# ============================================================
# Dependents vs Customer Churn
# ============================================================


# Create figure
plt.figure(figsize=(6,5))

# Plot Dependents vs Churn
ax = sns.countplot(x="Dependents", hue="Churn", data=df)

# Display count labels
for container in ax.containers:
    ax.bar_label(container)

# Add title
plt.title("Customer Churn by Dependents")

# Label axes
plt.xlabel("Dependents")
plt.ylabel("Number of Customers")

# Display legend
plt.legend(title="Churn")

# Show chart
plt.show()


# ============================================================
# Contract Type vs Customer Churn
# ============================================================


# Create figure
plt.figure(figsize=(7,5))

# Plot Contract Type vs Churn
ax = sns.countplot(x="Contract", hue="Churn", data=df)

# Display count labels
for container in ax.containers:
    ax.bar_label(container)

# Add chart title
plt.title("Customer Churn by Contract Type")

# Label axes
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

# Rotate x-axis labels for better readability
plt.xticks(rotation=10)

# Display legend
plt.legend(title="Churn")

# Show chart
plt.show()


# ============================================================
# Payment Method vs Customer Churn
# ============================================================

plt.figure(figsize=(10,5))

ax = sns.countplot(
    x="PaymentMethod",
    hue="Churn",
    data=df
)

for container in ax.containers:
    ax.bar_label(container, fontsize=8)

plt.title("Customer Churn by Payment Method")

plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.legend(title="Churn")

plt.show()


# ============================================================
# Customer Tenure Distribution
# ============================================================

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="tenure",
    bins=30,
    kde=True,
    color="steelblue",
    edgecolor="black"
)

plt.title("Distribution of Customer Tenure")

plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")

plt.show()


# ============================================================
# Monthly Charges vs Customer Churn
# ============================================================

plt.figure(figsize=(6,5))

sns.boxplot(
    x="Churn",
    y="MonthlyCharges",
    data=df
)

plt.title("Monthly Charges by Churn Status")

plt.xlabel("Churn")
plt.ylabel("Monthly Charges")

plt.show()

