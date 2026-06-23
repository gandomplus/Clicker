import tkinter as tk
import json
import os

root = tk.Tk()
root.geometry("400x550")
root.title("Clicker Game")

# Загрузка сохранения
if os.path.exists("score.json"):
    with open("score.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        score = data["score"]
        power_click = data["power_click"]
else:
    score = 0
    power_click = 1

# Функция сохранения
def save_score():
    data = {
        "score": score,
        "power_click": power_click
    }

    with open("score.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def click():
    global score
    score += power_click
    label.configure(text=f"Points: {score}\nPower Click: {power_click}")
    save_score()

def theme(Theme):
    if Theme == "Dark":
        root.configure(bg="black")
        label.configure(bg="black", fg="white")
        win_label.configure(bg="black", fg="white")
        click_button.configure(bg="gray", fg="white")
        upgrade1_button.configure(bg="gray", fg="white")
        upgrade2_button.configure(bg="gray", fg="white")
        upgrade3_button.configure(bg="gray", fg="white")
        upgrade4_button.configure(bg="gray", fg="white")
        upgrade5_button.configure(bg="gray", fg="white")
        win_button.configure(bg="gray", fg="white")
    elif Theme == "Light":
        root.configure(bg="white")
        label.configure(bg="white", fg="black")
        win_label.configure(bg="white", fg="black")
        click_button.configure(bg="lightgray", fg="black")
        upgrade1_button.configure(bg="lightgray", fg="black")
        upgrade2_button.configure(bg="lightgray", fg="black")
        upgrade3_button.configure(bg="lightgray", fg="black")
        upgrade4_button.configure(bg="lightgray", fg="black")
        upgrade5_button.configure(bg="lightgray", fg="black")
        win_button.configure(bg="lightgray", fg="black")

def upgrade_1():
    global score, power_click
    if score >= 10:
        power_click += 1
        score -= 10
        label.configure(text=f"Points: {score}\nPower Click: {power_click}")
        save_score()
def upgrade_2():
    global score, power_click
    if score >= 50:
        power_click += 5
        score -= 50
        label.configure(text=f"Points: {score}\nPower Click: {power_click}")
        save_score()
def upgrade_3():
    global score, power_click
    if score >= 100:
        power_click += 10
        score -= 100
        label.configure(text=f"Points: {score}\nPower Click: {power_click}")
        save_score()
def upgrade_4():
    global score, power_click
    if score >= 10000:
        power_click += 1000
        score -= 10000
        label.configure(text=f"Points: {score}\nPower Click: {power_click}")
        save_score()
def upgrade_5():
    global score, power_click
    if score >= 1000000:
        power_click += 100000
        score -= 1000000
        label.configure(text=f"Points: {score}\nPower Click: {power_click}")
        save_score()

def win():
    global score
    if score >= 1000000000:
        win_label.configure(text="You win!")
        score = 0
        label.configure(text=f"Points: {score}\nPower Click: {power_click}")
    elif score <= 1000000000:
        win_label.configure(text="You lose!")
        score = 0
        label.configure(text=f"Points: {score}\nPower Click: {power_click}")
    save_score()

menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Dark", command=lambda: theme("Dark"))
theme_menu.add_command(label="Light", command=lambda: theme("Light"))
menubar.add_cascade(label="Theme", menu=theme_menu)

label = tk.Label(root, text=f"Points: {score}\nPower Click: {power_click}", font=("Arial", 20))
label.pack(pady=20)

click_button = tk.Button(root, text="Click Me!", command=click)
click_button.pack(pady=20)
upgrade1_button = tk.Button(root, text="Upgrade (10 points)", command=upgrade_1)
upgrade1_button.pack(pady=10)
upgrade2_button = tk.Button(root, text="Upgrade (50 points)", command=upgrade_2)
upgrade2_button.pack(pady=10)
upgrade3_button = tk.Button(root, text="Upgrade (100 points)", command=upgrade_3)
upgrade3_button.pack(pady=10)
upgrade4_button = tk.Button(root, text="Upgrade (10000 points)", command=upgrade_4)
upgrade4_button.pack(pady=10)
upgrade5_button = tk.Button(root, text="Upgrade (1000000 points)", command=upgrade_5)
upgrade5_button.pack(pady=10)
win_button = tk.Button(root, text="Check Win/Lose", command=win)
win_button.pack(pady=10)
win_label = tk.Label(root, text="Upgrade (1000000000 points)\n(Button Win/Lose)", font=("Arial", 20))
win_label.pack(pady=20)

theme("Light")

root.config(menu=menubar)
root.mainloop()