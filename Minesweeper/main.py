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
# Створення ігрового поля

global_width = 500
global_height = 500

game_field = tkinter.Tk()
game_field.geometry(f"{global_width}x{global_height}")
game_field.minsize(global_width, global_height)
game_field.maxsize(global_width, global_height)
game_field.title("Minesweeper")
game_field.configure(background=grey)

# -------------------------------------------------ВЕРХНЯ ПАНЕЛЬ-------------------------------------------------------|

# Canvas
top_canvas_width = global_width
top_canvas_height = global_height / 4

top_canvas = tkinter.Canvas(
    game_field,
    background=dark_grey,
    width=top_canvas_width,
    height=top_canvas_height,
    highlightthickness=0
)
top_canvas.pack(fill="x", pady=0)

# -------------------------------------------------ТАЙМЕР--------------------------------------------------------------|

# Оновлення таймера------------------------------------------------------------------------------------------------|
seconds = 0
timer_id = None

def update_timer():
    global seconds
    seconds += 1
    timer_label.config(text=f"{seconds} s")
    global timer_id
    timer_id = game_field.after(1000, update_timer)

# Зупинка таймера
def stop_timer():
    global timer_id
    if timer_id is not None:
        game_field.after_cancel(timer_id)
        timer_id = None  # Очищаємо ідентифікатор таймера

# Таймер-----------------------------------------------------------------------------------------------------------|
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


# -------------------------------------------------КІЛЬКІСТЬ ПРАПОРЦІВ-------------------------------------------------|

flags_number = 10
current_flags_number = flags_number

# Кількість прапорців----------------------------------------------------------------------------------------------|
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

# Оновлення кількості прапорців------------------------------------------------------------------------------------|
def flags_number_del():
    global current_flags_number
    if current_flags_number != flags_number:
        current_flags_number += 1
        flags_number_label.config(text=current_flags_number)
        return True
    else:
        return False

def flags_number_add():
    global current_flags_number
    if current_flags_number != 0:
        current_flags_number -= 1
        flags_number_label.config(text=current_flags_number)
        return True
    else:
        return False


# -------------------------------------------------КНОПКА СТАРТ--------------------------------------------------------|
is_enable_click = True
game_end_message = None
# Функції кнопки старт---------------------------------------------------------------------------------------------|
def start_button_click():
    # Оновлення кількості прапорців
    global seconds, timer_id, current_flags_number, game_end_message, is_enable_click

    current_flags_number = flags_number
    flags_number_label.config(text=current_flags_number)
    create_buttons()

    # Повідомлення про прогаш
    if game_end_message:
        game_end_message.destroy()
    game_end_message = None

    # Запуск гри
    is_enable_click = True
    new_game()

    # Запуск таймера
    global seconds, timer_id
    if timer_id is not None:
        game_field.after_cancel(timer_id)
    seconds = 0
    timer_label.config(text="0 s")
    update_timer()


# Кнопка старт-----------------------------------------------------------------------------------------------------|
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

# Додавання елементів у канвас-------------------------------------------------------------------------------------|
top_canvas.create_window(top_canvas_width // 2 + top_canvas_width // 3, top_canvas_height // 2, window=timer_label,anchor="center")
top_canvas.create_window(top_canvas_width // 2 - top_canvas_width // 3, top_canvas_height // 2,window=flags_number_label, anchor="center")
top_canvas.create_window(top_canvas_width // 2, top_canvas_height // 2, window=start_button, anchor="center")


# -------------------------------------------------НИЖНЯ ПАНЕЛЬ--------------------------------------------------------|

# Canvas
bottom_canvas_width = global_width // 1.5
bottom_canvas_height = global_height // 1.5

bottom_canvas = tkinter.Canvas(
    game_field,
    background=dark_grey,
    width=bottom_canvas_width,
    height=bottom_canvas_height,
    highlightthickness=1
)
bottom_canvas.pack(padx=20, pady=20)


# -------------------------------------------------СІТКА КНОПОК--------------------------------------------------------|

# Розміри сітки та кнопок
rows, cols = 9, 9
button_size = 35  # Розмір кнопки
padding = 2  # Відступ між кнопками

# Центрування сітки на канвасі
x_offset = (bottom_canvas_width - (button_size + padding) * cols) // 2
y_offset = (bottom_canvas_height - (button_size + padding) * rows) // 2

# Створення кнопок у сітці-----------------------------------------------------------------------------------------|
buttons = []

def create_buttons():
    global buttons
    buttons = []  # Reset the buttons
    for row in range(rows):
        button_row = []
        for col in range(cols):
            # Позиція фрейму для кнопки
            x = x_offset + col * (button_size + padding)
            y = y_offset + row * (button_size + padding)

            # Створення фрейму з фіксованими розмірами для кнопки
            frame = tkinter.Frame(bottom_canvas, width=button_size, height=button_size)
            frame.grid_propagate(False)  # Забороняє змінювати розмір фрейму під вміст

            # Створення кнопки всередині фрейму
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
            button.place(relwidth=1, relheight=1)

            # Прив'язка подій до кнопки
            button.bind("<Button-1>", lambda e, r=row, c=col: left_click(e, r, c))  # Ліва кнопка миші
            button.bind("<Button-3>", lambda e, r=row, c=col: right_click(e, r, c))  # Права кнопка миші

            # Додавання фрейму з кнопкою на Canvas
            bottom_canvas.create_window(x + padding, y + padding, window=frame, anchor="nw")
            button_row.append(button)
        buttons.append(button_row)


# -------------------------------------------------ЛОГІКА ПРОГРАМИ-----------------------------------------------------|

# Визначення кольору цифри
def digit_color(mine_count):
    if mine_count == 1: return "#036ebe"
    elif mine_count == 2: return "#52803a"
    elif mine_count == 3: return "#C40C0C"
    elif mine_count == 4: return "#042160"
    elif mine_count == 5: return "#863707"
    elif mine_count == 6: return "#009b9b"
    elif mine_count == 7: return "#000000"
    elif mine_count == 8: return "#686D76"

# Обробка кліку лівою кнопкою (відкриття клітинки)-----------------------------------------------------------------|
def left_click(event, row, col):
    global is_enable_click, game_end_message
    button = buttons[row][col]
    current_color = button.cget("background")

    if current_color != light_green and current_color != medium_grey and is_enable_click:
        if mines[row][col]:
            open_all_mines()
            lose()
        else:
            mine_count = count_adjacent_mines(row, col)
            if mine_count > 0:
                button.config(text=str(mine_count), state="disabled", disabledforeground=digit_color(mine_count))
                button.config(background=medium_grey, highlightthickness=2)
            else:
                open_empty_cells(row, col)
                button.config(state="disabled", disabledforeground=white)
                button.config(background=medium_grey)

            # Перевірка на виграш після відкриття клітинки
            if is_won():
                win()

# Обробка кліку правою кнопкою (встановлення прапорця)-------------------------------------------------------------|
def right_click(event, row, col):
    global is_enable_click
    button = buttons[row][col]
    current_color = button.cget("background")

    if is_enable_click:
        if current_color == light_green:
            action = flags_number_del()
            if action:
                button.config(background=light_grey, text="")
        else:
            if current_color == light_grey:
                action = flags_number_add()
                if action:
                    button.config(background=light_green, text="<|")

        # Перевірка на виграш після встановлення прапорця
        if is_won():
            win()

# Створення масиву мін---------------------------------------------------------------------------------------------|
mines = [[]]
def generate_mines(rows, cols, number_of_mines):
    global mines
    mines = [[False for _ in range(cols)] for _ in range(rows)]
    mines_planted = 0

    while mines_planted < number_of_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if not mines[row][col]:  # Якщо в цій клітинці ще немає міни
            mines[row][col] = True
            mines_planted += 1
    return mines

# Функція для підрахунку кількості мін навколо клітинки------------------------------------------------------------|
def count_adjacent_mines(row, col):
    mine_count = 0
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i != row or j != col) and mines[i][j]:
                mine_count += 1
    return mine_count

# Функція відкриття порожніх клітинок-----------------------------------------------------------------------------|
def open_empty_cells(row, col):
    global current_flags_number
    # Якщо навколо немає мін, відкриваємо всі сусідні клітинки
    mine_count = count_adjacent_mines(row, col)
    button = buttons[row][col]
    button.config(text="", state="disabled", disabledforeground=white)
    button.config(background=medium_grey)

    if mine_count == 0:
        # Перевіряємо всі сусідні клітинки
        for i in range(max(0, row - 1), min(rows, row + 2)):
            for j in range(max(0, col - 1), min(cols, col + 2)):
                if (i != row or j != col):  # Перевіряємо сусідні клітинки
                    # Якщо клітинка не відкрита, відкриваємо її
                    neighbor_button = buttons[i][j]
                    if neighbor_button.cget("state") != "disabled":
                        if neighbor_button.cget("background") == light_green:
                            flags_number_del()
                        open_empty_cells(i, j)  # Рекурсивний виклик для відкриття сусідніх клітинок
    else:
        button.config(text=str(mine_count), disabledforeground=digit_color(mine_count))  # Якщо є міни поруч, виводимо кількість мін

# Функція перевірки на перемогу
def is_won():
    for i in range(rows):
        for j in range(cols):
            button = buttons[i][j]
            # Перевірка, що всі клітинки з мінами мають прапорці, і всі інші відкриті
            if mines[i][j]:
                if button.cget("background") != light_green:  # Прапорець не стоїть на міні
                    return False
            else:
                if button.cget("state") != "disabled":  # Не міна, але не відкрита
                    return False
    return True  # Всі умови виграшу виконані

# Функція відкриття всіх мін

def open_all_mines():
    global mines, is_enable_click
    for i in range(rows):
        for j in range(cols):
            if mines[i][j]:
                button = buttons[i][j]
                button.config(text="!", state="disabled", disabledforeground=black)
                button.config(background=red)
                is_enable_click = False

def win():
    global game_end_message

    # Зупинка таймера
    stop_timer()

    # Повідомлення про виграш
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
    game_end_message.place(relx=0.5, rely=0.6, anchor="center")

def lose():
    global game_end_message

    # Зупинка таймера
    stop_timer()

    # Повідомлення про прогаш
    game_end_message = tkinter.Label(
        game_field,
        text="You lose!",
        font=("Helvetica", 25, "bold"),
        background=red,
        foreground=white,
        highlightthickness=1,
        highlightbackground=white,
        width=top_canvas_width // 50,
        height=2
    )
    game_end_message.place(relx=0.5, rely=0.6, anchor="center")

def new_game():
    # Створення масиву з мінами
    global mines
    mines = generate_mines(rows, cols, flags_number)

# -------------------------------------------------ЗАПУСК ПРОГРАМИ-----------------------------------------------------|
game_field.mainloop()