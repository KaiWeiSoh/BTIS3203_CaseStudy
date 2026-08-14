import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Q1. Prepare and Understand Data & Visualisation 1
# Load dataset locally from the provided file
file_path = 'water_consumption.csv'
df = pd.read_csv(file_path)

print("--- Initial Data Structure ---")
print(df.info())

# Convert date string to pandas datetime object to extract the year
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# Data Transformation: Remove 'Malaysia' aggregate to avoid double-counting geographic data
df_states = df[df['state'] != 'Malaysia'].copy()

# VISUALISATION 1: Pie Chart of Total Domestic vs Non-Domestic Consumption
total_consumption = df_states.groupby('sector')['value'].sum()

plt.figure(figsize=(8, 8))
plt.pie(total_consumption, 
        labels=total_consumption.index.str.title(), 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=['#66b3ff', '#ff9999'],
        explode=(0.05, 0), # Slightly pull out the domestic slice for aesthetics
        shadow=True)
plt.title('Overall Distribution of Water Consumption\n(Excluding National Aggregate)')
plt.savefig('Q1_Sector_Distribution_Pie.png', dpi=300)
plt.show()

# Q2. Conduct Analysis & Visualisation 2 
# Isolate non-domestic (industrial/commercial) consumption
nondomestic_df = df_states[df_states['sector'] == 'nondomestic']

# Focus on major manufacturing hubs
target_states = ['Selangor', 'Johor', 'Pulau Pinang']
hubs_df = nondomestic_df[nondomestic_df['state'].isin(target_states)]

# Calculate % growth from 2003 to 2022
growth_results = {}
for state in target_states:
    state_data = hubs_df[hubs_df['state'] == state]
    val_2003 = state_data[state_data['year'] == 2003]['value'].values[0]
    val_2022 = state_data[state_data['year'] == 2022]['value'].values[0]
    growth = ((val_2022 - val_2003) / val_2003) * 100
    growth_results[state] = growth

print("\n--- Non-Domestic Water Consumption Growth (2003-2022) ---")
for state, growth in growth_results.items():
    print(f"{state}: {growth:.2f}%")

# VISUALISATION 2: Line Chart of Growth over Time
plt.figure(figsize=(10, 6))
sns.lineplot(data=hubs_df, x='year', y='value', hue='state', marker='o', linewidth=2.5)
plt.title('Non-Domestic Water Consumption Trend in Major Industrial Hubs (2003 - 2022)')
plt.xlabel('Year')
plt.ylabel('Water Consumption (MLD)')
plt.xticks(range(2003, 2023, 2))
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Q2_Industrial_Water_Growth.png', dpi=300)
plt.show()

# Q3.Intensity Ratio Visualisation 3
# Filter data for the most recent year (2022)
df_2022 = df_states[df_states['year'] == 2022]

# Pivot table to put domestic and nondomestic as columns
pivot_2022 = df_2022.pivot_table(index='state', columns='sector', values='value')

# Feature Engineering: Calculate Industrial Intensity Ratio
pivot_2022['Industrial_Intensity_Ratio'] = pivot_2022['nondomestic'] / pivot_2022['domestic']

# Sort states by highest ratio
sorted_ratio = pivot_2022.sort_values(by='Industrial_Intensity_Ratio', ascending=False)

# VISUALISATION 3: Bar Chart of Intensity Ratios
plt.figure(figsize=(12, 7))
sns.barplot(x=sorted_ratio['Industrial_Intensity_Ratio'], y=sorted_ratio.index, palette='viridis')
plt.title('Industrial Water Intensity Ratio by State (2022)\n(Non-Domestic : Domestic Usage)')
plt.xlabel('Ratio (Higher value indicates heavier industrial/commercial proportion)')
plt.ylabel('State')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Q3_Water_Intensity_Ratio.png', dpi=300)
plt.show()