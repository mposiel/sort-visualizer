from tkinter import *
from random import *
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort

def random_list():
    size = scale1.get()
    i = 1
    tab = []
    while (i <= size):
        tab.append(i)
        i += 1
    shuffle(tab)
    return tab


def draw_bars(canvas, bars, width, height, red_index=None, green_index=None):
    if not canvas.winfo_exists():
        return
    if green_index is not None and not isinstance(green_index, list):
        green_index = [green_index]
    canvas.delete("all")
    bar_width = width // len(bars)
    max_value = max(bars)
    for i, value in enumerate(bars):
        x0 = i * bar_width
        y0 = height
        x1 = x0 + bar_width
        y1 = height - (value / max_value) * height
        fill_color = 'blue'
        if i == red_index:
            fill_color = 'red'
        elif green_index and i in green_index:
            fill_color = 'green'
        canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color)
        canvas.create_text((x0 + x1) / 2, y1 + 10, text=str(value), fill="white")
    canvas.update()
    canvas.after(10)


def sort():
    if not listbox.curselection():
        return
    algChoice = listbox.get(listbox.curselection())
    bars = random_list()
    if algChoice == "Bubble sort":
        bubble_sort(canvas, bars, draw_bars, delay=scale2.get())
    elif algChoice == "Selection sort":
        selection_sort(canvas, bars, draw_bars, delay=scale2.get())
    elif algChoice == "Merge sort":
        merge_sort(canvas, bars, 0, len(bars) - 1, draw_bars, delay=scale2.get())
    elif algChoice == "Insertion sort":
        insertion_sort(canvas, bars, draw_bars, delay=scale2.get())



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
listbox.insert(3, "Insertion sort")

scale1 = Scale(window, from_=10, to=100)
scale1.place(x=35, y=350)

scale_label1 = Label(window, text="Elements", bg="#4c4d49")
scale_label1.place(x=30, y=320)

scale2 = Scale(window, from_=1, to=100)
scale2.place(x=110, y=350)

scale_label2 = Label(window, text="Delay", bg="#4c4d49")
scale_label2.place(x=105, y=320)

canvas = Canvas(window, width=800, height=400)
canvas.place(x=200, y=120)

sort_button = Button(window, text="Sort", width=20, height=3, command=sort)
sort_button.place(x=500, y=550)

window.mainloop()
