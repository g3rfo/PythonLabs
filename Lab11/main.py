import csv
# Параметри введення даних у файлі Export_of_goods_and_services.csv
finale_file_fieldnames = ['Series Name', 'Series Code', 'Country Name', 'Country Code', '2018 [YR2018]', '2019 [YR2019]']
# Перевірка відкриття файлу Export_of_goods_and_services.csv, виведення вмісту
try:
    start_csv_file = open('Export_of_goods_and_services.csv', 'r')
    reader = csv.DictReader(start_csv_file, delimiter=',')
    print("Country Name: 2018 [YR2018], 2019 [YR2019]")
    for row in reader:
        print(row['Country Name'], ':', row['2018 [YR2018]'],',', row['2019 [YR2019]'])
    start_csv_file.seek(0)
except:
    print('Could not open Export_of_goods_and_services.csv')
    exit()
# Параметри введення даних у файл Lab11_file.csv
finale_file_fieldnames = ['Country Name', '2018 [YR2018]', '2019 [YR2019]']
# Перевірка відкриття файлу Lab11_file.csv
try:
    final_csv_file = open('Lab11_file.csv', 'w', newline= '')
    writer = csv.DictWriter(final_csv_file, fieldnames=finale_file_fieldnames, delimiter=',')
    writer.writeheader()
except:
    print('Could not open Lab11_file.csv')
    exit()
# Вибір країн, для занесення у файл Lab11_file.csv
user_input = input('\n<<<<<<<<<<<------------------>>>>>>>>>>>\nEnter countries to add in final csv file: ')
selected_countries = [country.strip() for country in user_input.split(",")]
# Занасення даних вибраних країн у файл Lab11_file.csv
for row in reader:
    if row['Country Name'] in selected_countries:
        writer.writerow({'Country Name' : row['Country Name'], '2018 [YR2018]' : row['2018 [YR2018]'], '2019 [YR2019]' : row['2019 [YR2019]']})
# Закриття всіх файлів
start_csv_file.close()
final_csv_file.close()