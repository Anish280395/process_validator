import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("breach_analysis.csv")
print(df.head())

# Count breaches by type
counts = df['Breach Type'].value_counts()

plt.figure(figsize=(8,5))
counts.plot(kind='bar', color='coral')
plt.title('Number of Breaches by Type')
plt.ylabel('Number of Cases')
plt.xlabel('Breach Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('breach_type_chart.png')
plt.show()

#analyze which steps are most often missing:
missing_df = df[df["Breach Type"] == "Missing Steps"]
if not missing_df.empty:
    all_missing = missing_df["Details"].str.cat(sep=", ").split(", ")
    missing_series = pd.Series(all_missing).value_counts()

    plt.figure(figsize=(8,5))
    missing_series.plot(kind='bar', color='teal')
    plt.title('Most Frequently Missing Steps')
    plt.ylabel('Number of Occurrences')
    plt.xlabel('Step')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('missing_steps_chart.png')
    plt.show()
else:
    print("No Missing Steps breaches to plot!")