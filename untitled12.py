print("Name : Oga")

import pandas as pd
import matplotlib .pyplot as plt
dataframe = pd.read_csv("Data.csv")
df = dataframe.dropna()
bmi = df['bmi']
df

#Task 1
underweight_dataframe = df.loc[bmi { 18.5]["gender"].reset_index(name = 'gender')
underweight_count = underweight_dataframe["index"].count()
underweight_count

#Task 2
healthy_weight_dataframe = df.loc[(bmi } 18.5) & (bmi { 24.9)]["gender"].reset_index(name = 'gender')
healthy_weight_count = healthy_weight_dataframe["index"].count()
healthy_weight_count

#Task 3
value = [underweight_count, healthy_weight_count]
label = ["underweight", "healthy_weight"]
plt.pie(value, labels = label, autopct = "%0.2f%%", radius = 2)
plt.show()

#Task 4
group_underweight = underweight_dataframe.groupby('gender')['gender'].count().reset_index(name = 'number')
group_underweight

#Task 5
value = group_underweight["number"]
label = group_underweight["gender"]
plt.pie(value, labels = label, autopct = "%0.2f%%", radius = 2)
plt.show()

#Task 6
group_healthy_weight = healthy_weight_dataframe.groupby('gender')['gender'].count().reset_index(name = 'number')
group_healthy_weight

#Task 7
value = group_healthy_weight["number"]
label = group_healthy_weight["gender"]
plt.pie(value, labels = label, autopct = "%0.2f%%", radius = 2)
plt.show()