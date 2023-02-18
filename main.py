from tkinter import *
from random import *


def bubble_sort(canvas, bars, delay):
    n = len(bars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if bars[j] > bars[j + 1]:
                bars[j], bars[j + 1] = bars[j + 1], bars[j]
                canvas.delete("all")
                draw_bars(canvas, bars, 800, 400, j + 1)
                canvas.update()
                canvas.after(delay)
        canvas.delete("all")
        draw_bars(canvas, bars, 800, 400)
        canvas.update()
        canvas.after(delay)

def selection_sort(canvas, bars, delay):
    n = len(bars)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if bars[j] < bars[min_index]:
                min_index = j
        if min_index != i:
            bars[i], bars[min_index] = bars[min_index], bars[i]
            canvas.delete("all")
            draw_bars(canvas, bars, 800, 400, i)
            canvas.update()
            canvas.after(delay)
    canvas.delete("all")
    draw_bars(canvas, bars, 800, 400)
    canvas.update()
    canvas.after(delay)


def random_list(size):
    i = 1
    tab = []
    while (i <= size):
        tab.append(i)
        i += 1
    shuffle(tab)
    return tab


def draw_bars(canvas, bars, width, height, green_index=None):
    bar_width = width // len(bars)
    max_value = max(bars)
    for i, value in enumerate(bars):
        x0 = i * bar_width
        y0 = height
        x1 = x0 + bar_width
        y1 = height - (value / max_value) * height
        fill_color = 'blue'
        if i == green_index:
            fill_color = 'green'
        canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color)
        canvas.create_text((x0 + x1) / 2, y1 - 10, text=str(value))


def sort():
    algChoice = listbox.get(listbox.curselection())
    bars = random_list(50)
    if algChoice == "Bubble sort":
        bubble_sort(canvas, bars, 100)
    elif algChoice == "Selection sort":
        selection_sort(canvas, bars, 100)



window = Tk()
window.geometry("1200x650")  # Setting size of the window
window.title("Sort visualizer")

# Adding icon
icon = PhotoImage(file='img/icon.png')
window.iconphoto(True, icon)

# setting background color
window.config(background="#4c4d49")

# Make the window not resizable
window.wm_resizable(False, False)

label = Label(window, text="Sort visualizer", font=('Arial', 20, 'bold'), bg='#4c4d49')
label.place(x=10, y=10)

listbox = Listbox(window, bg="white")
listbox.place(x=30, y=120)

listbox.insert(0, "Bubble sort")
listbox.insert(1, "Selection sort")
listbox.insert(2, "Merge sort")
listbox.insert(3, "Quick sort")
listbox.insert(4, "Insertion sort")

scale1 = Scale(window, from_=10, to=100)
scale1.place(x=35,y=350)

scale_label1 = Label(window, text="Elements",bg="#4c4d49")
scale_label1.place(x=30,y=320)

scale2 = Scale(window, from_=1, to=30)
scale2.place(x=110,y=350)

scale_label2 = Label(window, text="Delay",bg="#4c4d49")
scale_label2.place(x=105,y=320)

canvas = Canvas(window, width=800, height=400)
canvas.place(x=200, y=120)

sort_button = Button(window, text="Sort", width=20, height=3, command=sort)
sort_button.place(x=500, y=550)

window.mainloop()
