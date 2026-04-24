import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

# Sample data
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura", "Daniel", "Emma", "James", "Olivia", 
               "Ethan", "Sophia", "Matthew", "Isabella", "Andrew", 
               "Mia","Joseph", "Charlotte", "Samuel", "Amelia", "Benjamin", "Harper", "Elijah", "Evelyn", "Lucas", "Abigail"]
gender = ["Male", "Female"]
maital_status = ["Married", "Unmarried"]
race = ["White", "Black", "Latino", "Asian", "Native American", "Other"]
religion = ["Protestant", "Catholic", "Jewish", "Atheist", "Others"]
yes_no = ["Yes", 'No']
education = ['High School', 'Associate Degree', "Bachelor's Degree", 
             'Postgraduate degree', 'Less then high school']
area = ['urban', 'suburban', 'rural']
region = ['east', 'west', 'south', 'midwest']
names = []
for i in range(1000):
    names.append(f"{random.choice(first_names)}")

# Generate random student data
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
print("Counts of students in each gender:")
print(students_df['Gender'].value_counts()) 
print("-_"*40)
print("Voters with income greater than 100k:")
print(students_df[students_df['Income'] > 100000]) 
print("-_"*40)
print("First voter details:")
print(students_df.iloc[0]) 
print("-_"*40)
print(students_df.head())



# # Distribution of GPA
# plt.figure(figsize=(8, 5))
# sns.histplot(students_df['GPA'], kde=True, bins=15)
# plt.title('Distribution of GPA')
# plt.xlabel('GPA')
# plt.ylabel('Count')
# plt.show()

# # Average GPA by Year (Bar Plot)
# plt.figure(figsize=(8, 5))
# sns.barplot(x='Year', y='GPA', data=students_df, ci=None)
# plt.title('Average GPA by Year')
# plt.xlabel('Year')
# plt.ylabel('Average GPA')
# plt.show()

# # Count of Students per Major (Bar Plot)
# plt.figure(figsize=(10, 5))
# sns.countplot(x='Major', data=students_df)
# plt.title('Number of Students per Major')
# plt.xlabel('Major')
# plt.ylabel('Count')
# plt.xticks(rotation=45)
# plt.show()

# # GPA vs. Credits Completed (Scatter Plot)
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x='Credits_Completed', y='GPA', hue='Year', data=students_df)
# plt.title('GPA vs. Credits Completed')
# plt.xlabel('Credits Completed')
# plt.ylabel('GPA')
# plt.legend(title='Year')
# plt.show()

# # Absences by Major (Box Plot)
# plt.figure(figsize=(10, 5))
# sns.boxplot(x='Major', y='Abscences', data=students_df)
# plt.title('Absences by Major')
# plt.xlabel('Major')
# plt.ylabel('Absences')
# plt.xticks(rotation=45)
# plt.show()

