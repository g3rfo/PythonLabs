import pandas as pd

old_list = [1, 2, 3, 4, 5]
new_list = [6, 7, 8, 9, 10]

df = pd.DataFrame({"Old list" : old_list, "New list" : new_list})
print(df)
print("\nСума першого листа:", df["Old list"].sum())
print("Мінімальне другого листа:", df["New list"].min())
print("Максимальне першого листа:", df["Old list"].max())
print("Середнє арифметичне другого листа:", df["New list"].mean())