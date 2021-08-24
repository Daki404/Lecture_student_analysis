import matplotlib.pyplot as plt
import seaborn as sns
import random

tmp = [random.randint(14, 22) for _ in range(1000)]

ax = plt.subplots()
ax = sns.countplot(tmp)

plt.show()