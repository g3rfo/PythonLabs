import matplotlib.pyplot as plt

names = ['Pyshchyk', 'Ivzhenko', 'Dyachenko', 'Rudenko']
avg_grades = [90, 80.8, 81.6, 87]

plt.figure(figsize=(8, 8))
plt.title('Вагомість студента у середній оцінці групи', fontsize=15)
plt.pie(list(avg_grades), labels=names, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()
