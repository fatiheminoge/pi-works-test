import pandas as pd

df = pd.read_csv('country_vaccination_stats.csv')
df_copy = df.copy()

# Question 4
df_copy['daily_vaccinations'] = df['daily_vaccinations'].fillna(df.groupby('country')['daily_vaccinations'].transform('min')).fillna(0)
df_copy.to_csv('country_vaccination_imputed.csv')

# Question 5
df_copy.groupby('country')['daily_vaccinations'].agg('median')[:3]

# Question 6
total_vacc_in_date = df_copy[df_copy['date'] == '1/6/2021']['daily_vaccinations'].sum()
print(total_vacc_in_date)