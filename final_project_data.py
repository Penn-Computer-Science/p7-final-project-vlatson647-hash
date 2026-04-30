import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

# Sample data
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura", "Daniel", "Emma", "James", "Olivia", 
               "Ethan", "Sophia", "Matthew", "Isabella", "Andrew", 
               "Mia","Joseph", "Charlotte", "Samuel", "Amelia", "Benjamin", "Harper", "Elijah", "Evelyn", "Lucas", "Abigail",
               "Liam","Noah","Lucas","Henry","Jack","Aiden","Sebastian","Wyatt","Leonardo","Julian","Nora"
               "Grace","Chloe","Lily","Zoe", 'Vincent']
gender = ["Male", "Female"]
maital_status = ["Married", "Unmarried"]
race = ["White", "Black", "Latino", "Asian", "Native American", "Other"]
religion = ["Protestant", "Catholic", "Jewish", "Atheist", "Others"]
yes_no = ["Yes", 'No']
education = ['High School', 'Associate Degree', "Bachelor's Degree", 
             'Postgraduate degree', 'Less then high school']
area = ['urban', 'suburban', 'rural']
region = ['east', 'west', 'south', 'midwest']
party = ['Dem', 'Dem', 'GOP', 'GOP', 'Ind']
names = []
for i in range(random.randint(50000, 100000)):
    names.append(f"{random.choice(first_names)}")

# Generate random voter data
data = {
    "Name": names,
    "Gender": [random.choice(gender) for _ in names],
    "Marital Status": [random.choice(maital_status) for _ in names],
    "Race/Ethnicity": [random.choice(race) for _ in names],
    "Religion": [random.choice(religion) for _ in names],
    "Religion": [random.choice(religion) for _ in names],
    "Age": [random.randint(18,65) for _ in names],
    "First Time Voting": [random.choice(yes_no) for _ in names],
    "Education": [random.choice(education) for _ in names],
    "Income": [random.randint(30000,200000) for _ in names],
    "Area type": [random.choice(area) for _ in names],
    "Region": [random.choice(region) for _ in names],
    "Leaning": [random.choice(party) for _ in names],
}

students = pd.DataFrame(data)

#print(round(students_df.describe()))

students.to_csv('exitpoll.csv', index=False) # Save to CSV file
# print("DataFrame saved to 'students_data.csv'")


# Calcualtes Data


df =  pd.read_csv("exitpoll.csv")
students_df = pd.DataFrame(df)
print("Head of the DataFrame:")
print(students_df.head()) #.head() shows the first 5 rows of the dataframe
print("-_"*40)
print("Tail of the DataFrame:")
print(students_df.tail()) #.tail() shows the last 5 rows of the dataframe
print("-_"*40)  
print("Summary of the DataFrame:")
print(students_df.info()) #.info() gives a summary of the dataframe
print("-_"*40)
print("Statistical Summary:")
print(round(students_df.describe(),1)) #.describe() gives statistical summary of numerical columns
print("-_"*40)
print("Counts of voters in each gender:")
print(students_df['Gender'].value_counts()) 
print("-_"*40)
print("Voters with income greater than 100k:")
print(students_df[students_df['Income'] > 100000]) 
print("-_"*40)
print("First voter details:")
print(students_df.iloc[0]) 
print("-_"*40)
print(students_df.head())
print("-_"*40)
print('Parties by Gender')
print(pd.crosstab(students_df['Gender'], students_df['Leaning']))
print('Parties by Gender(%)')
print((pd.crosstab(students_df['Gender'], students_df['Leaning'], normalize='index')*100).round(2))
print("-_"*40)
print('Parties by Region')
print(pd.crosstab(students_df['Region'], students_df['Leaning']))
print('Parties by Region(%)')
print((pd.crosstab(students_df['Region'], students_df['Leaning'], normalize='index')*100).round(2))
print("-_"*40)
print('Parties by Religion')
print(pd.crosstab(students_df['Religion'], students_df['Leaning']))
print('Parties by Religion(%)')
print((pd.crosstab(students_df['Religion'], students_df['Leaning'], normalize='index')*100).round(2))
print("-_"*40)
print('Parties by Race/Ethnicity')
print(pd.crosstab(students_df['Race/Ethnicity'], students_df['Leaning']))
print('Parties by Race/Ethnicity(%)')
print((pd.crosstab(students_df['Race/Ethnicity'], students_df['Leaning'], normalize='index')*100).round(2))
print("-_"*40)
print('Parties by Education')
print(pd.crosstab(students_df['Education'], students_df['Leaning']))
print('Parties by Education(%)')
print((pd.crosstab(students_df['Education'], students_df['Leaning'], normalize='index')*100).round(2))
print("-_"*40)
print('Parties by Marital Status')
print(pd.crosstab(students_df['Marital Status'], students_df['Leaning']))
print('Parties by Marital Status(%)')
print((pd.crosstab(students_df['Marital Status'], students_df['Leaning'], normalize='index')*100).round(2))
print("-_"*40)
print('Parties by Area type')
print(pd.crosstab(students_df['Area type'], students_df['Leaning']))
print('Parties by Area type(%)')
print((pd.crosstab(students_df['Area type'], students_df['Leaning'], normalize='index')*100).round(2))
print("-_"*40)
print("Vote Count")
print(students_df['Leaning'].value_counts()) 
print((students_df['Leaning'].value_counts(normalize=True)*100).round(2))
print("-_"*40)


plt.figure(figsize=(10, 5))
sns.countplot(x='Leaning', data=students_df)
plt.title('Number of Voters per Party')
plt.xlabel('Leanings')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
sns.countplot(x='Gender', data=students_df)
plt.title('Number of Voters per Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
sns.countplot(x='Region', data=students_df)
plt.title('Number of Voters per Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


