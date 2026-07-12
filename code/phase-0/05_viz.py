import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic")


# sns.histplot(data=titanic, x="age", bins=30)
# plt.show()

# sns.countplot(data=titanic, x="pclass")
# plt.show()

# sns.boxplot(data=titanic, x="pclass", y="fare")
# plt.show()


# sns.barplot(data=titanic, x="sex", y="survived")
# plt.show()


# sns.barplot(data=titanic, x="pclass", y="survived", hue="sex")


# sns.countplot(data=titanic, x="pclass", hue="sex")
# plt.show()


# Matrix

numeric = titanic.select_dtypes(include=["number"])
corr = numeric.corr()
print(corr)

sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Кореляційна матриця Titanic")
plt.show()
