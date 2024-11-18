import tkinter
import random

# -------------------------------------------------НАЗВИ КОЛЬОРІВ------------------------------------------------------|

orange = "#D65A31"
white = "#EEEEEE"
grey = "#393E46"
dark_grey = "#222831"
light_green = "#72BF78"
medium_grey = "#878b91"
light_grey = "#A6AEBF"
red = "#C40C0C"
black = "#000000"

# -------------------------------------------------ІГРОВЕ ПОЛЕ---------------------------------------------------------|

# Створення вікна програми

# Розміри вікна
global_width = 500
global_height = 500

# Задання параметрів вікна програми(розміри(мін, макс), назва, колір)
game_field = tkinter.Tk()
game_field.geometry(f"{global_width}x{global_height}")
game_field.minsize(global_width, global_height)
game_field.maxsize(global_width, global_height)
game_field.title("Minesweeper")
game_field.configure(background=grey)


# -------------------------------------------------ВЕРХНЯ ПАНЕЛЬ-------------------------------------------------------|


# Створення канвасу для верхньої панелі

# Розміри верхньої панелі
top_canvas_width = global_width
top_canvas_height = global_height / 4

# Задання параметрів верхньої панелі(розміри, колір, обведення)
top_canvas = tkinter.Canvas(
    game_field,
    background=dark_grey,
    width=top_canvas_width,
    height=top_canvas_height,
    highlightthickness=0
)

# Розміщення верхньої панелі у вікні програми
top_canvas.pack(fill="x", pady=0)

# -------------------------------------------------ТАЙМЕР--------------------------------------------------------------|

# Задання параметрів таймеру(текст, шрифт, розміри, колір, обведення)
timer_label = tkinter.Label(
    game_field,
    text="0 s",
    font=("Helvetica", 30, "bold"),
    background=orange,
    foreground=white,
    highlightthickness=1,
    highlightbackground=white,
    width=top_canvas_width // 100,
    height=1
)

# Змінні для роботи таймеру
seconds = 0
timer_id = None

# Оновлення таймера
def update_timer():
    global seconds, timer_id
    seconds += 0.1
    timer_label.config(text=f"{int(seconds)} s")

    timer_id = game_field.after(100, update_timer)

# Зупинка таймера
def stop_timer():
    global timer_id
    if timer_id is not None:
        game_field.after_cancel(timer_id)
        timer_id = None
        timer_label.config(text="0 s")

# -------------------------------------------------КІЛЬКІСТЬ ПРАПОРЦІВ-------------------------------------------------|

# Змінні для роботи лічильника
flags_number = 10
current_flags_number = flags_number

# Задання параметрів кількості прапорців(текст, шрифт, розміри, колір, обведення)
flags_number_label = tkinter.Label(
    game_field,
    text=str(flags_number),
    font=("Helvetica", 30, "bold"),
    background=orange,
    foreground=white,
    highlightthickness=1,
    highlightbackground=white,
    width=top_canvas_width // 100,
    height=1
)

# Оновлення кількості прапорців

# Видалення прапорця на ігровому полі(лічильник збільшується)
def flags_number_del():
    global current_flags_number
    if current_flags_number != flags_number:
        current_flags_number += 1
        flags_number_label.config(text=current_flags_number)
        return True
    else:
        return False
# Додавання прапорця на ігрове поле(лічильник зменшується)
def flags_number_add():
    global current_flags_number
    if current_flags_number != 0:
        current_flags_number -= 1
        flags_number_label.config(text=current_flags_number)
        return True
    else:
        return False


# -------------------------------------------------КНОПКА СТАРТ--------------------------------------------------------|

# Змінні для роботи функцій кнопки старт
is_enable_click = True
game_end_message = None
counter = 0

# Функції кнопки старт
def start_button_click():
    # Змінні для роботи
    global seconds, timer_id, current_flags_number, game_end_message, is_enable_click, mines, counter

    # Зупинка таймеру
    stop_timer()

    # Видалення повідомлення про кінець поточної гри
    if game_end_message:
        game_end_message.destroy()
    game_end_message = None

    # Скидання гри
    seconds = 0
    bottom_canvas.delete("all")  # Видалення сітки кнопок ігрового поля
    current_flags_number = flags_number  # Оновлення кількості невикористаних прапорців
    flags_number_label.config(text=current_flags_number)

    # Запуск гри
    create_buttons()  # Створення сітки ігрового поля
    mines = generate_mines(rows, cols, flags_number)  # Генерація розташування мін на полі
    update_timer()  # Запуск таймеру
    is_enable_click = True  # Доступ до натиснення кнопок на ігровому полі

    counter += 1
    print(counter)

# Задання параметрів кнопки старт(текст, шрифт, розміри, колір, обведення, функція при натисненні)
start_button = tkinter.Button(
    game_field,
    text="PLAY",
    font=("Helvetica", 30, "bold"),
    background=light_green,
    foreground=white,
    highlightthickness=1,
    highlightbackground=white,
    width=top_canvas_width // 80,
    height=1,
    command=start_button_click
)

# Додавання елементів(таймер, кількість доступних прапорців, кнопки PLAY) у канвас
top_canvas.create_window(top_canvas_width // 2 + top_canvas_width // 3, top_canvas_height // 2, window=timer_label,anchor="center")
top_canvas.create_window(top_canvas_width // 2 - top_canvas_width // 3, top_canvas_height // 2,window=flags_number_label, anchor="center")
top_canvas.create_window(top_canvas_width // 2, top_canvas_height // 2, window=start_button, anchor="center")


# -------------------------------------------------НИЖНЯ ПАНЕЛЬ--------------------------------------------------------|

# Створення канвасу для нижньої панелі

# Розміри нижньої панелі
bottom_canvas_width = global_width // 1.5
bottom_canvas_height = global_height // 1.5

# Задання параметрів нижньої панелі(розміри, колір, обведення)
bottom_canvas = tkinter.Canvas(
    game_field,
    background=dark_grey,
    width=bottom_canvas_width,
    height=bottom_canvas_height,
    highlightthickness=1
)

# Розміщення нижньої панелі у вікні програми
bottom_canvas.pack(padx=20, pady=20)

# -------------------------------------------------СІТКА КНОПОК--------------------------------------------------------|

# Розміри сітки та кнопок
rows, cols = 9, 9
button_size = 35  # Розмір кнопки
padding = 2  # Відступ між кнопками

# Центрування сітки на канвасі
x_offset = (bottom_canvas_width - (button_size + padding) * cols) // 2
y_offset = (bottom_canvas_height - (button_size + padding) * rows) // 2

# Створення кнопок у сітці
# Створення порожнього масиву кнопок
buttons = []

# Функція створення кнопок для ігрового поля
def create_buttons():
    # Масив кнопок
    global buttons

    # Очищення попереднього масиву, якщо такий існує
    if buttons:
        for row in buttons:
            for button in row:
                button.destroy()
    buttons = []

    # Заповнення масиву кнопками
    for row in range(rows):
        button_row = []
        for col in range(cols):
            # Обрахунок позицї фрейму для кнопки
            x = x_offset + col * (button_size + padding)
            y = y_offset + row * (button_size + padding)

            # Створення фрейму з фіксованими розмірами для кнопки
            frame = tkinter.Frame(bottom_canvas, width=button_size, height=button_size)
            frame.grid_propagate(False)  # Заборона змінювати розмір фрейму під вміст

            # Задання параметрів кнопки(текст, розміри, колір, обведення)
            button = tkinter.Button(
                frame,
                text="",
                font=("Helvetica", 25, "bold"),
                background=light_grey,
                foreground=white,
                width=button_size,
                height=button_size,
                highlightthickness=2,
                highlightbackground=medium_grey,
            )

            # Розміщення кнопки по розмірах фрейму
            button.place(relwidth=1, relheight=1)

            # Прив'язка подій до кнопки
            button.bind("<Button-1>", lambda e, r=row, c=col: left_click(e, r, c))  # Ліва кнопка миші
            button.bind("<Button-3>", lambda e, r=row, c=col: right_click(e, r, c))  # Права кнопка миші

            # Додавання фрейму з кнопкою на Canvas
            bottom_canvas.create_window(x + padding, y + padding, window=frame, anchor="nw")
            # Оновлення масиву кнопок
            button_row.append(button)
        # Оновлення масиву кнопок
        buttons.append(button_row)


# -------------------------------------------------ЛОГІКА ПРОГРАМИ-----------------------------------------------------|


# Створення порожнього масиву мін
mines = []

# Функція випадкового розміщення мін на полі
def generate_mines(rows, cols, number_of_mines):
    # Масив мін
    global mines

    # Заповнення масиву мін значенням False
    mines = [[False for _ in range(cols)] for _ in range(rows)]
    # Змінна кількості встановлених мін
    mines_planted = 0

    # Цикл рандомного встановлення мін, поки не досягнемо потрібної кількості
    while mines_planted < number_of_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if not mines[row][col]:  # Якщо клітинці ще немає міни
            mines[row][col] = True  # Надання комірці значення True(в цій комірці встановлено міну)
            mines_planted += 1  # Оновлення кількості встановлених мін
    return mines

# Функція для підрахунку кількості мін навколо клітинки
def count_adjacent_mines(row, col):
    # Змінна кількості мін навколо клітинки
    mine_count = 0

    # Цикл перевірки всіх комірок довколо вибраної на наявність міни
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i != row or j != col) and mines[i][j]:  # Якщо це не вибрана клітинка і значення масиву мін = True(в клітинці є міна)
                mine_count += 1  # Оновлення кількості мін навколо
    return mine_count

# Визначення кольору цифри в залежності від кількості мін навколо
def digit_color(mine_count):
    if mine_count == 1: return "#036ebe"
    elif mine_count == 2: return "#52803a"
    elif mine_count == 3: return "#C40C0C"
    elif mine_count == 4: return "#042160"
    elif mine_count == 5: return "#863707"
    elif mine_count == 6: return "#009b9b"
    elif mine_count == 7: return "#000000"
    elif mine_count == 8: return "#686D76"

# Функція відкриття порожніх клітинок
def open_empty_cells(row, col):
    # Змінна кількості невикористаних прапорців
    global current_flags_number

    # Поточна кнопка
    button = buttons[row][col]

    # Якщо клітинка вже відкрита, не обробляємо її
    if button.cget("state") == "disabled":
        return

    # Обрахунок кількості мін навколо клітинки
    mine_count = count_adjacent_mines(row, col)

    # Оновлення параметрів кнопки(текст, колір, доступність для взаємодії(недоступна))
    button.config(text="", state="disabled", disabledforeground=white)
    button.config(background=medium_grey)

    # Якщо мін навколо немає
    if mine_count == 0:
        # Перевіряємо всі сусідні клітинки
        for i in range(max(0, row - 1), min(rows, row + 2)):
            for j in range(max(0, col - 1), min(cols, col + 2)):
                if (i != row or j != col):
                    # Поточна кнопка для перевірки
                    neighbor_button = buttons[i][j]
                    # Якщо кнопка доступна для взаємодії
                    if neighbor_button.cget("state") != "disabled":
                        # Якщо колір кнопки зелений(на коміці встановлено прапорець)
                        if neighbor_button.cget("background") == light_green:
                            flags_number_del()  # Видалення прапорця
                        open_empty_cells(i, j)  # Рекурсивний виклик для відкриття сусідніх клітинок
    else:  # Якщо є міни поруч
        # Оновлення параметрів кнопки(текст = кількості мін навколо, колір = відповідно від кількості мін навколо)
        button.config(text=str(mine_count), disabledforeground=digit_color(mine_count))

# Функція перевірки на виграш у грі
def is_won():
    # Цикл перевірки всіх комірок масиву кнопок
    for i in range(rows):
        for j in range(cols):
            # Поточна кнопка
            button = buttons[i][j]

            if mines[i][j]: # Якщо у клітинці є міна
                if button.cget("background") != light_green:  # Прапорець не стоїть на міні
                    return False
            else: # Якщо у клітинці немає міни
                if button.cget("state") != "disabled":  # Якщо клітинка доступна до взаємодії
                    return False
    return True  # Всі умови виграшу виконані

# Функція відкриття всіх мін
def open_all_mines(row, col):
    # Змінна масиву мін
    global mines
    # Цикл перебору всіх кнопок у масиві
    for i in range(rows):
        for j in range(cols):
            # Поточна кнопка
            button = buttons[i][j]
            # Якщо це міна і це не клітинка, на яку натиснули
            if mines[i][j] and (row != i or col != j):
                # Зміна параметрів кнопки(текст, колір, доступність)
                button.config(text="!", state="disabled", disabledforeground=black)
                button.config(background=grey)

# Функція виведення повідомлення про виграш
def win():
    # Змінні повідомлення про кінець гри і кількість секунд поточної гри
    global game_end_message, seconds

    # Зупинка таймеру
    stop_timer()

    # Зміна параметрів повідомлення про виграш(текст, шрифт, колір, обводка, розміри)
    game_end_message = tkinter.Label(
        game_field,
        text=f"You won!\nTime: {seconds} s",
        font=("Helvetica", 25, "bold"),
        background=light_green,
        foreground=white,
        highlightthickness=1,
        highlightbackground=white,
        width=top_canvas_width // 50,
        height=2
    )

    # Розміщення повідомлення про виграш у вікні програми
    game_end_message.place(relx=0.5, rely=0.6, anchor="center")

# Функція виведення повідомлення про програш
def lose():
    # Змінна повідомлення про кінець гри
    global game_end_message

    # Зупинка таймеру
    stop_timer()

    # Зміна параметрів повідомлення про виграш(текст, шрифт, колір, обводка, розміри)
    game_end_message = tkinter.Label(
        game_field,
        text="You lose!",
        font=("Helvetica", 25, "bold"),
        background=red,
        foreground=white,
        highlightthickness=1,
        highlightbackground=white,
        width=top_canvas_width // 150,
        height=1
    )

    # Розміщення повідомлення про виграш у вікні програми
    game_end_message.place(relx=0.5, rely=0.6, anchor="center")

# Функція обробка кліку лівою кнопкою (відкриття клітинки)
def left_click(event, row, col):
    # Змінні чи доступна взаємодія з кнопками і повідомлення про кінець гри
    global is_enable_click, game_end_message
    # Змінна поточної кнопки
    button = buttons[row][col]
    # Змінна кольору поточної кнопки
    current_color = button.cget("background")

    # Якщо поточна кнопка не прапорець, не відкрита і доступна для натиснення
    if current_color != light_green and current_color != medium_grey and is_enable_click:
        # Якщо поточна комірка містить міну
        if mines[row][col]:
            # Зміна параметрів поточної кнопки(текст, колір, доступність)
            button.config(text="!", state="disabled", disabledforeground=black)
            button.config(background=red)
            is_enable_click = False  # Взаємодія з кнопками не доступна

            # Відкриття всіх мін, окрім поточної
            open_all_mines(row, col)
            # Запуск дій функції програшу
            lose()
        else:  # В поточній комірці немає міни
            # Обрахунок кількості мін навколо
            mine_count = count_adjacent_mines(row, col)
            if mine_count > 0:  # Якщо навколо є хоча б одна міна
                # Зміна параметрів кнопки(текст = кількість мін навколо, доступність = недоступна, колір шрифту залежить від кількості мін навколо)
                button.config(text=str(mine_count), state="disabled", disabledforeground=digit_color(mine_count))
                button.config(background=medium_grey, highlightthickness=2)
            else:  # Якщо навколо немає мін
                open_empty_cells(row, col)  # Відкриваємо всі клітинки без мін навколо поточної і наступні
                # Зміна параметрів кнопки(доступність, колір шрифту, колір)
                button.config(state="disabled", disabledforeground=white)
                button.config(background=medium_grey)

            # Перевірка на виграш після відкриття клітинки
            if is_won():  # Якщо всі умови для виграшу виконані
                win()  # Запуск дій функції виграшу

# Функція обробки кліку правою кнопкою (встановлення/видалення прапорця)
def right_click(event, row, col):
    # Змінна чи доступна взаємодія з кнопками
    global is_enable_click
    # Змінна поточної кнопки
    button = buttons[row][col]
    # Змінна кольору поточної кнопки
    current_color = button.cget("background")

    if is_enable_click:  # Якщо можна натиснути на кнопку
        if current_color == light_green:  # Якщо колір кнопки = кольору прапорця
            action = flags_number_del()  # Змінна action, для перевірки, чи можна видалити прапорець(якщо так, то одразу видаляє)
            if action:  # Якщо прапорець видалили
                button.config(background=light_grey, text="")  # Зміна параметрів поточної кнопки(колір, текст)
        else:  # Якщо колір кнопки != кольору прапорця
            if current_color == light_grey:  # Якщо комірка ще не відкрита
                action = flags_number_add()  # Змінна action, для перевірки, чи можна додати прапорець(якщо так, то одразу додає)
                if action:  # Якщо прапорець додали
                    button.config(background=light_green, text="<|")   # Зміна параметрів поточної кнопки(колір, текст)

        # Перевірка на виграш після встановлення прапорця
        if is_won():  # Якщо всі умови для виграшу виконані
            win()  # Запуск дій функції виграшу

# -------------------------------------------------ЗАПУСК ПРОГРАМИ-----------------------------------------------------|
game_field.mainloop()  #Запуск циклу обробки подій взаємодії з вікном, поки його не закрито