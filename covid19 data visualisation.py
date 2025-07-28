import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('covid_data.csv')

# Preview data
print(data)

# Extract data
countries = data['Country']
total_cases = data['TotalCases']
total_deaths = data['TotalDeaths']
total_recovered = data['TotalRecovered']

# ---------------------------
# 1. Bar chart: Total Cases
# ---------------------------
plt.figure(figsize=(10, 6))
plt.bar(countries, total_cases, color='skyblue')
plt.title('Total COVID-19 Cases by Country')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ---------------------------
# 2. Bar chart: Deaths vs Recovered
# ---------------------------
x = range(len(countries))

plt.figure(figsize=(10, 6))
plt.bar(x, total_deaths, width=0.4, label='Deaths', color='red', align='center')
plt.bar([i + 0.4 for i in x], total_recovered, width=0.4, label='Recovered', color='green', align='center')
plt.xticks([i + 0.2 for i in x], countries)
plt.title('COVID-19 Deaths vs Recovered')
plt.xlabel('Country')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ---------------------------
# 3. Line chart: Trends
# ---------------------------
plt.figure(figsize=(10, 6))
plt.plot(countries, total_cases, label='Cases', marker='o')
plt.plot(countries, total_deaths, label='Deaths', marker='x')
plt.plot(countries, total_recovered, label='Recovered', marker='s')
plt.title('COVID-19 Stats Overview')
plt.xlabel('Country')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

