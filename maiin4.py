###################################ЗАДАЧА1######################
# Потрібно проаналізувати взаємозв'язок між користувачами, сесіями та виручкою за днями. Усе необхідно запрограмувати в Python з використанням pandas, NumPy і Matplotlib.
# Сформуйте таблицю мінімум на 30 днів із колонками "date", "users", "sessions", "revenue".
#
# Розрахуйте кореляційну матрицю для цих метрик.
#
# Побудуйте діаграми розсіювання для пар: users-sessions, users-revenue, sessions-revenue.
#
# Побудуйте лінійний графік "revenue" за датами.
#
# Виведіть матрицю та всі графіки.
###############################РОЗВ'ЯЗАННЯ################################
##################import pandas as pd
####################import numpy as np
#####################import matplotlib.pyplot as plt

# dates = pd.date_range(start="2025-10-01", periods=30, freq='D')
#
# np.random.seed(42)
# users = np.random.randint(50, 150, size=30)
# sessions = users + np.random.randint(0, 50, size=30)
# revenue = sessions * np.random.uniform(5, 10, size=30)
#
# df = pd.DataFrame({
#     "date": dates,
#     "users": users,
#     "sessions": sessions,
#     "revenue": revenue
# })
#
# print(df.head())
#
# corr_matrix = df[["users", "sessions", "revenue"]].corr()
# print("Кореляційна матриця:")
# print(corr_matrix)
#
# plt.figure(figsize=(15, 4))
#
# plt.subplot(1, 3, 1)
# plt.scatter(df["users"], df["sessions"], color='blue')
# plt.xlabel("Users")
# plt.ylabel("Sessions")
# plt.title("Users vs Sessions")
#
# plt.subplot(1, 3, 2)
# plt.scatter(df["users"], df["revenue"], color='green')
# plt.xlabel("Users")
# plt.ylabel("Revenue")
# plt.title("Users vs Revenue")
#
# plt.subplot(1, 3, 3)
# plt.scatter(df["sessions"], df["revenue"], color='red')
# plt.xlabel("Sessions")
# plt.ylabel("Revenue")
# plt.title("Sessions vs Revenue")
#
# plt.tight_layout()
# plt.show()
#
# plt.figure(figsize=(10, 5))
# plt.plot(df["date"], df["revenue"], marker='o', color='purple')
# plt.xlabel("Date")
# plt.ylabel("Revenue")
# plt.title("Revenue за 30 днів")
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()

###################################ЗАДАЧА2######################
# Потрібно проаналізувати дані A/B-експерименту та візуалізувати конверсії. Усе необхідно запрограмувати в Python з використанням pandas, NumPy і Matplotlib.
# Сформуйте таблицю з полями "group" (A або B) і "converted" (0/1) з не менш ніж 100 спостереженнями в кожній групі.
#
# Розрахуйте конверсію в групах, абсолютну різницю та відносну зміну.
#
# Побудуйте 95% довірчі інтервали для конверсії в кожній групі.
#
# Побудуйте стовпчасту діаграму конверсій груп із відображенням довірчих інтервалів.
#
# Виведіть усі розраховані значення та графік.
###############################РОЗВ'ЯЗАННЯ################################
# #########import pandas as pd
# ################import numpy as np
# ################import matplotlib.pyplot as plt
# ##################from scipy import stats
#
# np.random.seed(42)
#
# n_A = 120
# n_B = 130
#
# converted_A = np.random.binomial(1, 0.3, n_A)
# converted_B = np.random.binomial(1, 0.35, n_B)
#
# df = pd.DataFrame({
#     "group": ["A"]*n_A + ["B"]*n_B,
#     "converted": np.concatenate([converted_A, converted_B])
# })
#
# print(df.head())

###################################ЗАДАЧА3######################
# Потрібно перевірити дію центральної граничної теореми на прикладі несиметричного розподілу. Усе необхідно запрограмувати в Python з використанням pandas, NumPy і Matplotlib.
# Згенеруйте генеральну сукупність щонайменше з 50 000 спостережень із несиметричного розподілу.
#
# Сформуйте кілька підвибірок фіксованого розміру n і для кожної обчисліть середнє.
#
# Збережіть вибіркові середні та побудуйте їхню гістограму.
#
# Повторіть процедуру для щонайменше двох різних n і виведіть обидві гістограми.
#
# Виведіть середнє і стандартне відхилення вибіркових середніх для кожного n.
###############################РОЗВ'ЯЗАННЯ################################
# #########import numpy as np
#################### import matplotlib.pyplot as plt
#
# np.random.seed(42)
#
# population = np.random.exponential(scale=2, size=50000)
#
# print(f"Середнє генеральної сукупності: {population.mean():.3f}")
# print(f"Стандартне відхилення генеральної сукупності: {population.std():.3f}")
#
# def sample_means(population, n, num_samples=1000):
#     means = []
#     for _ in range(num_samples):
#         sample = np.random.choice(population, size=n, replace=True)
#         means.append(sample.mean())
#     return np.array(means)
#
# n_small = 5
# n_large = 50
# means_small = sample_means(population, n_small)
# means_large = sample_means(population, n_large)
#
# print(f"n={n_small}: середнє = {means_small.mean():.3f}, std = {means_small.std():.3f}")
# print(f"n={n_large}: середнє = {means_large.mean():.3f}, std = {means_large.std():.3f}")
#
# plt.figure(figsize=(12,5))
#
# plt.subplot(1, 2, 1)
# plt.hist(means_small, bins=30, color='skyblue', edgecolor='black')
# plt.title(f"Гістограма вибіркових середніх (n={n_small})")
# plt.xlabel("Середнє")
# plt.ylabel("Частота")
#
# plt.subplot(1, 2, 2)
# plt.hist(means_large, bins=30, color='salmon', edgecolor='black')
# plt.title(f"Гістограма вибіркових середніх (n={n_large})")
# plt.xlabel("Середнє")
# plt.ylabel("Частота")
#
# plt.tight_layout()
# plt.show()

###################################ЗАДАЧА4######################
# Потрібно проаналізувати часовий ряд продажів і візуалізувати ковзаючі метрики. Усе необхідно запрограмувати в Python з використанням pandas, NumPy і Matplotlib.
# Сформуйте таблицю "date" і "sales" за 90 днів.
#
# Додайте ковзне середнє і ковзне стандартне відхилення за обраним вікном.
#
# Побудуйте графік вихідних продажів і графік ковзного середнього на одному полі.
#
# Побудуйте окремий графік ковзного стандартного відхилення.
#
# Виведіть таблицю з першими рядками нових стовпців і обидва графіки.
###############################РОЗВ'ЯЗАННЯ################################
###############import pandas as pd
################import numpy as np
######################import matplotlib.pyplot as plt

np.random.seed(42)

dates = pd.date_range(start="2025-10-01", periods=90, freq='D')

sales = np.random.poisson(lam=200, size=90) + np.linspace(0, 20, 90)

df = pd.DataFrame({
    "date": dates,
    "sales": sales
})

window = 7
df["rolling_mean"] = df["sales"].rolling(window=window).mean()
df["rolling_std"] = df["sales"].rolling(window=window).std()

print(df.head(10))

plt.figure(figsize=(12,5))
plt.plot(df["date"], df["sales"], label="Продажі", color="blue", marker='o', markersize=4)
plt.plot(df["date"], df["rolling_mean"], label=f"{window}-денне ковзне середнє", color="red", linewidth=2)
plt.xlabel("Дата")
plt.ylabel("Продажі")
plt.title("Продажі та ковзаюче середнє")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(12,5))
plt.plot(df["date"], df["rolling_std"], label=f"{window}-денне ковзне std", color="green", linewidth=2)
plt.xlabel("Дата")
plt.ylabel("Стандартне відхилення")
plt.title("Ковзаюче стандартне відхилення продажів")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()