import pandas as pd

# Part 1
people = pd.DataFrame(
    {
        "name": ["Ігор", "Петро", "Юля", "Катя", "Леся"],
        "age": [25, 23, 22, 22, 20],
        "salary": [2000.00, 1800.00, 1800.00, 1900.00, 1500.00],
        "city": ["Київ", "Львів", "Одеса", "Київ", "Львів"],
    }
)


# print(people.head())
# print(people.info())
#
#
# print(people.describe())  # default only int and float
# print(people.describe(include="str"))  # only str
# print(people.describe(include="all"))  # all types

# Part 2 Selection

salaries = people["salary"]

print(type(salaries))


people_name_and_city = people[["name", "city"]]

print(people_name_and_city)

name_1 = people.loc[1, "name"]

print(name_1)

first_3_rows = people.iloc[:3]

print(first_3_rows)

mask = people["age"] > 22

print(mask)
people_filter_by_age = people[mask]

print(people_filter_by_age)

avg_salary_over_22 = people_filter_by_age["salary"].mean()
print(avg_salary_over_22)


# part 3

people_by_city = people.groupby("city")
print(people_by_city.size())

avg_salary_by_city = people_by_city["salary"].mean()
print(avg_salary_by_city)

age_min_and_max_by_city = people_by_city.agg({"age": ["min", "max"]})

print(age_min_and_max_by_city)

# part 4 Titanic

import seaborn as sns

titanic = sns.load_dataset("titanic")

print(titanic.head())
print(titanic.info())
print(titanic.describe())


print(titanic.isna())
print(titanic.isna().sum())
print(titanic["survived"].mean())
print(titanic.groupby("sex")["survived"].mean())
print(titanic.groupby("pclass")["survived"].mean())

print(titanic.groupby(["sex", "pclass"])["survived"].mean())
