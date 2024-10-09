string1 = "fgj543kldsgjkfhd1"
string2 = "k2l9kk7hfghfgdaq6"
string3 = "9kg56kncpggfq"

def file_open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened! Mode:", mode)
        return file


file_name1 = "TF17_1.txt"
file_name2 = "TF17_2.txt"
file_name3 = "TF17_3.txt"

# Запис даних у TF17_1.txt
file1_read_write = file_open(file_name1, "w+")
if file1_read_write:
    file1_read_write.write(string1 + "\n" + string2 + "\n" + string3)
    print("Data was added to TF17_1.txt successfully!")

    # Переміщення курсора на початок файлу для читання
    file1_read_write.seek(0)

    # Розбиття тексу з TF17_1.txt на цифри і букви
    number_string = ""
    char_string = ""
    for line in file1_read_write:
        for char in line:
            if char.isdigit():
                number_string += char + " "
            elif char.isalpha():
                char_string += char + " "

    file1_read_write.close()
    print("File", file_name1, "was closed!")

    # Запис цифр у TF17_2.txt
    file2_write = file_open(file_name2, "w")
    if file2_write:
        file2_write.write(number_string.strip() + "\n")
        file2_write.close()
        print("File", file_name2, "was closed!")

    # Запис букв у TF17_3.txt
    file3_write = file_open(file_name3, "w")
    if file3_write:
        file3_write.write(char_string.strip() + "\n")
        file3_write.close()
        print("File", file_name3, "was closed!")

    # Відкриття TF17_3.txt для читання і запис по 10 символів у TF17_2.txt
    file3_read = file_open(file_name3, "r")
    file2_append = file_open(file_name2, "a")

    if file3_read and file2_append:
        char_string = ""
        count = 0
        for char in file3_read.read():
            if char != " ":
                char_string += char + " "
                count += 1
            if count == 10:
                file2_append.write(char_string.strip() + "\n")
                char_string = ""
                count = 0

        if char_string:
            file2_append.write(char_string.strip() + "\n")

        file3_read.close()
        print("File", file_name3, "was closed!")

        file2_append.close()
        print("File", file_name2, "was closed!")

    # Читаємо і виводимо вміст TF17_2.txt
    file2_read = file_open(file_name2, "r")
    if file2_read:
        print("\nTF17_2.txt")
        print(file2_read.read())
        file2_read.close()
        print("File", file_name2, "was closed!")
