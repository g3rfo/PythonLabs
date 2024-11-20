import numpy as np
import matplotlib.pyplot as plt

years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
Ukraine = [45593342, 45489648, 45272155, 45167350, 45038236, 44880758, 44690584, 44474512, 44207754, 43848986, 38000000, 37000000]
USA = [313877662, 316059947, 318386329, 320738994, 323071755, 325122128, 326838199, 328329953, 331526933, 332048977, 333271411, 334914895]

np.array(years)
np.array(Ukraine)
np.array(USA)

# Завдання 1

plt.plot(years, Ukraine, label='Ukraine', color = "purple")
plt.plot(years, USA, label='USA', color = "yellow")

plt.title('Population, total', fontsize=15)   # назва графіка
plt.xlabel('Year', fontsize=12, color='red') # позначення вісі абсцис
plt.ylabel('Population, (M)', fontsize=12, color='red') # позначення вісі ординат
plt.legend()
plt.grid(True)

plt.show()

# Завдання 2

answer = input("Enter country(Ukraine/USA):").strip()
if answer.lower() == "ukraine":
    plt.bar(years, np.array(Ukraine) / 1_000_000, color='purple', label='Ukraine')
    plt.title('Population of Ukraine', fontsize=15)
    plt.ylabel('Population (Millions)', fontsize=12)
elif answer.lower() == "usa":
    plt.bar(years, np.array(USA) / 1_000_000, color='yellow', label='USA')
    plt.title('Population of USA', fontsize=15)
    plt.ylabel('Population (Millions)', fontsize=12)
else:
    print("Invalid country name. Please enter 'Ukraine' or 'USA'.")
    exit()

plt.xlabel('Year', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='-', alpha=0.7)  # Додаємо горизонтальну сітку
plt.xticks(years, rotation=45)  # Обертаємо підписи років для зручності

plt.show()