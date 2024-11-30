import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv('DZ_AZ02.csv')
print(df.head())

print(df.describe())

print(f"Средняя оценка по математике - {df['Math'].mean()}")
print(f"Средняя оценка по биологии - {df['Biology'].mean()}")
print(f"Средняя оценка по русскому - {df['Russian'].mean()}")
print(f"Средняя оценка по английскому - {df['English'].mean()}")
print(f"Средняя оценка по географии - {df['Geography'].mean()}")

print(f"Медианная оценка по математике - {df['Math'].median()}")
print(f"Медианная оценка по биологии - {df['Biology'].median()}")
print(f"Медианная оценка по русскому - {df['Russian'].median()}")
print(f"Медианная оценка по английскому - {df['English'].median()}")
print(f"Медианная оценка по географии - {df['Geography'].median()}")

print(f"Стандартное отклонение оценок по математике - {df['Math'].std()}")

Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
IQR = Q3_math - Q1_math

print(f"Первый квартиль по математике - {Q1_math}")
print(f"Третий квартиль по математике - {Q3_math}")
print(f"Межкваральный размах по математике - {IQR}")
