######################################ЗАДАЧА1################################
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
###########################################ОЗВ'ЯЗАННЯ#################################
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# np.random.seed(42)
# n_days = 30
# dates = pd.date_range(start='2025-10-01', periods=n_days)
#
# users = np.random.randint(50, 200, size=n_days)
# sessions = users + np.random.randint(0, 50, size=n_days)
# revenue = sessions * np.random.uniform(5, 15, size=n_days)
#
# data = pd.DataFrame({
#     'date': dates,
#     'users': users,
#     'sessions': sessions,
#     'revenue': revenue
# })
#
# print("Перші рядки таблиці:")
# print(data.head())
#
# corr_matrix = data[['users', 'sessions', 'revenue']].corr()
# print("\nКореляційна матриця:")
# print(corr_matrix)
#
# plt.figure(figsize=(15,4))
#
# plt.subplot(1,3,1)
# plt.scatter(data['users'], data['sessions'], color='blue')
# plt.xlabel('Users')
# plt.ylabel('Sessions')
# plt.title('Users vs Sessions')
#
# plt.subplot(1,3,2)
# plt.scatter(data['users'], data['revenue'], color='green')
# plt.xlabel('Users')
# plt.ylabel('Revenue')
# plt.title('Users vs Revenue')
#
# plt.subplot(1,3,3)
# plt.scatter(data['sessions'], data['revenue'], color='red')
# plt.xlabel('Sessions')
# plt.ylabel('Revenue')
# plt.title('Sessions vs Revenue')
#
# plt.tight_layout()
# plt.show()
#
# plt.figure(figsize=(12,5))
# plt.plot(data['date'], data['revenue'], marker='o', color='purple')
# plt.xlabel('Date')
# plt.ylabel('Revenue')
# plt.title('Revenue over Time')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()

######################################ЗАДАЧА2################################
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
###########################################ОЗВ'ЯЗАННЯ#################################
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats
#
# np.random.seed(42)
# n = 150
#
# group_A = np.random.binomial(1, 0.20, n)
# group_B = np.random.binomial(1, 0.27, n)
#
# data = pd.DataFrame({
#     'group': ['A']*n + ['B']*n,
#     'converted': np.concatenate([group_A, group_B])
# })
#
# print("Перші рядки таблиці:")
# print(data.head())
#
# conversion_rates = data.groupby('group')['converted'].mean()
# abs_diff = conversion_rates['B'] - conversion_rates['A']
# rel_change = abs_diff / conversion_rates['A']
#
# print("\nКонверсії за групами:")
# print(conversion_rates)
# print(f"\nАбсолютна різниця: {abs_diff:.3f}")
# print(f"Відносна зміна: {rel_change:.2%}")
#
# def confidence_interval(p, n, alpha=0.05):
#     z = stats.norm.ppf(1 - alpha/2)
#     se = np.sqrt(p*(1-p)/n)
#     return p - z*se, p + z*se
#
# ci_A = confidence_interval(conversion_rates['A'], n)
# ci_B = confidence_interval(conversion_rates['B'], n)
#
# print(f"\n95% Довірчий інтервал для групи A: {ci_A}")
# print(f"95% Довірчий інтервал для групи B: {ci_B}")
#
# groups = ['A', 'B']
# rates = [conversion_rates['A'], conversion_rates['B']]
# errors = [
#     conversion_rates['A'] - ci_A[0],
#     conversion_rates['B'] - ci_B[0]
# ]
#
# plt.figure(figsize=(6,5))
# plt.bar(groups, rates, yerr=errors, capsize=8, color=['skyblue','salmon'])
# plt.ylabel('Conversion Rate')
# plt.title('A/B Test Conversion Rates with 95% CI')
# plt.ylim(0, max(rates)+0.1)
# plt.show()

######################################ЗАДАЧА3################################
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
###########################################ОЗВ'ЯЗАННЯ#################################
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# np.random.seed(42)
# population_size = 50000
#
# population = np.random.exponential(scale=2.0, size=population_size)
#
# print(f"Середнє генеральної сукупності: {np.mean(population):.3f}")
# print(f"Стандартне відхилення генеральної сукупності: {np.std(population):.3f}")
#
# def sample_means(pop, n_samples=1000, sample_size=30):
#     means = []
#     for _ in range(n_samples):
#         sample = np.random.choice(pop, size=sample_size, replace=False)
#         means.append(np.mean(sample))
#     return np.array(means)
#
# sample_sizes = [10, 50]
# results = {}
#
# for n in sample_sizes:
#     means = sample_means(population, n_samples=1000, sample_size=n)
#     results[n] = means
#     print(f"\nВибірка n={n}: середнє = {np.mean(means):.3f}, std = {np.std(means):.3f}")
#
# plt.figure(figsize=(12,5))
#
# for i, n in enumerate(sample_sizes):
#     plt.subplot(1, len(sample_sizes), i+1)
#     plt.hist(results[n], bins=30, color='skyblue', edgecolor='black')
#     plt.title(f'Вибіркові середні (n={n})')
#     plt.xlabel('Середнє')
#     plt.ylabel('Частота')
#
# plt.tight_layout()
# plt.show()

######################################ЗАДАЧА4################################
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
###########################################ОЗВ'ЯЗАННЯ#################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range(start='2025-01-01', periods=90)
sales = np.random.poisson(lam=50, size=90)

df = pd.DataFrame({
    'date': dates,
    'sales': sales
})

window = 7
df['rolling_mean'] = df['sales'].rolling(window=window).mean()
df['rolling_std'] = df['sales'].rolling(window=window).std()

print(df.head(15))

plt.figure(figsize=(12,6))
plt.plot(df['date'], df['sales'], label='Продажі', marker='o')
plt.plot(df['date'], df['rolling_mean'], label=f'Ковзаюче середнє ({window} днів)', color='red', linewidth=2)
plt.title('Продажі та ковзаюче середнє')
plt.xlabel('Дата')
plt.ylabel('Продажі')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,4))
plt.plot(df['date'], df['rolling_std'], label=f'Ковзне std ({window} днів)', color='green', linewidth=2)
plt.title('Ковзаюче стандартне відхилення продажів')
plt.xlabel('Дата')
plt.ylabel('Стандартне відхилення')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()