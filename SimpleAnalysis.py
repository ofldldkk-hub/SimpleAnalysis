import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.randint(-10000, 10001, size=1000)
series = pd.Series(data, name='Исходные_данные')

def clean_data(series):
    mask = series.apply(lambda x: isinstance(x, (int, np.integer)) and -10000 <= x <= 10000)
    return series[mask]

cleaned_series = clean_data(series)

min_val = cleaned_series.min()
max_val = cleaned_series.max()
sum_val = cleaned_series.sum()
std_val = cleaned_series.std()
duplicates_count = cleaned_series.duplicated().sum()

print("Все данные корректны, очистка не требуется.")
print("=== Статистические характеристики очищенного набора ===")
print(f"Минимальное значение: {min_val}")
print(f"Максимальное значение: {max_val}")
print(f"Сумма чисел: {sum_val}")
print(f"Среднеквадратическое отклонение: {std_val:.4f}")
print(f"Количество повторяющихся значений: {duplicates_count}")

with open('stats_output.txt', 'w', encoding='utf-8') as f:
    f.write("=== Статистические характеристики ===\n")
    f.write(f"Минимальное значение: {min_val}\n")
    f.write(f"Максимальное значение: {max_val}\n")
    f.write(f"Сумма чисел: {sum_val}\n")
    f.write(f"Среднеквадратическое отклонение: {std_val:.4f}\n")
    f.write(f"Количество повторяющихся значений: {duplicates_count}\n")

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(cleaned_series.values, color='blue', marker='.', linestyle='-', linewidth=0.5, markersize=2)
plt.title('Линейный график исходных данных')
plt.xlabel('Индекс')
plt.ylabel('Значение')

rounded_data = cleaned_series.apply(lambda x: round(x / 100) * 100)
plt.subplot(1, 2, 2)
plt.hist(rounded_data, bins=30, edgecolor='black', alpha=0.7, color='green')
plt.title('Гистограмма (округление до сотен)')
plt.xlabel('Диапазоны')
plt.ylabel('Частота')
plt.tight_layout()
plt.savefig('initial_plots.png', dpi=150)
plt.show()

df = pd.DataFrame({
    'Исходные_данные': cleaned_series,
    'Сортировка_по_возрастанию': cleaned_series.sort_values().values,
    'Сортировка_по_убыванию': cleaned_series.sort_values(ascending=False).values
})
df.to_csv('dataframe_result.csv', index=False)

id_sum = sum(map(int, str(70227403)))
while id_sum > 9:
    id_sum = sum(map(int, str(id_sum)))
marker_style = ['o', 's', '^', 'D', '*', 'p', 'h', 'v', '<', '>'][id_sum % 10]

plt.figure(figsize=(10, 6))
plt.plot(df['Сортировка_по_возрастанию'], label='По возрастанию',
         color='red', marker=marker_style, markersize=3, linestyle='-', linewidth=0.5)
plt.plot(df['Сортировка_по_убыванию'], label='По убыванию',
         color='blue', marker=marker_style, markersize=3, linestyle='-', linewidth=0.5)
plt.title('Сравнение отсортированных рядов')
plt.xlabel('Индекс в отсортированном массиве')
plt.ylabel('Значение')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('sorted_plots.png', dpi=150)
plt.show()

print("\nПрограмма завершена. Созданы файлы: stats_output.txt, dataframe_result.csv, initial_plots.png, sorted_plots.png")