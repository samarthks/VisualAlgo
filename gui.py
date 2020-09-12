from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("VisualAlgo")
root.geometry("1100x600+200+80")
root.config(bg="#082A46")


def Generate_data(x):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 1070
    x_width = canvas_width / (len(x) + 1)
    offset = 10
    space_rect = 10
    new_data = [i / max(x) for i in x]

    for i, height in enumerate(new_data):
        x0 = i * x_width + offset + space_rect
        y0 = canvas_height - height * 400
        x1 = (i + 1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(
            x0 + 2,
            y0,
            anchor=SW,
            text=str(x[i]),
            font=("arial", 14, "bold"),
            fill="orange",
        )


def Algo_select():
    print("Algo:", select_algo.get())
    try:
        min = int(minvalue.get())
    except:
        min = 1
    try:
        max = int(maxvalue.get())
    except:
        max = 100

    try:
        size = int(sizevalue.get())
    except:
        size = 10

    if min < 0 or max > 100:
        min = 0
        max = 100
    if size > 80 or size < 3:
        size = 50
    if min > max:
        min, max = max, min

    array = []
    for i in range(size):
        array.append(random.randrange(min, max + 1))
    Generate_data(array)


select_algo = StringVar()
mainLabel = Label(
    root,
    text="Algorithm:",
    font=("new Roman", 16, "italic bold"),
    bg="yellow",
    width=10,
    fg="black",
    relief=GROOVE,
    bd=5,
)
mainLabel.place(x=0, y=0)

algo_menu = ttk.Combobox(
    root,
    state="readonly",
    width=15,
    font=("new Roman", 19, "italic bold"),
    textvariable=select_algo,
    values=[
        "Choose algorithm",
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort",
    ],
)
algo_menu.place(x=145, y=0)
algo_menu.current(0)

generate_button = Button(
    root,
    text="Generate data",
    bg="orange",
    font=("arial", 12, "italic bold"),
    relief=SUNKEN,
    activebackground="blue",
    activeforeground="white",
    bd=5,
    width=12,
    command=Algo_select,
)
generate_button.place(x=1000, y=60)
sizevaluelabel = Label(
    root,
    text="Size : ",
    font=("new Roman", 16, "italic bold"),
    bg="gray",
    width=10,
    fg="black",
    relief=GROOVE,
    bd=5,
)
sizevaluelabel.place(x=0, y=60)
sizevalue = Scale(
    root,
    from_=5,
    to=80,
    resolution=1,
    orient=HORIZONTAL,
    font=("arial", 14, "italic bold"),
    relief=GROOVE,
    bd=2,
    width=10,
)
sizevalue.place(x=120, y=60)

minvaluelabel = Label(
    root,
    text="Min Value : ",
    font=("new Roman", 16, "italic bold"),
    bg="gray",
    width=10,
    fg="black",
    relief=GROOVE,
    bd=5,
)
minvaluelabel.place(x=250, y=60)
minvalue = Scale(
    root,
    from_=0,
    to=10,
    resolution=1,
    orient=HORIZONTAL,
    font=("arial", 14, "italic bold"),
    relief=GROOVE,
    bd=2,
    width=10,
)
minvalue.place(x=370, y=60)

maxvaluelabel = Label(
    root,
    text="Max Value : ",
    font=("new Roman", 16, "italic bold"),
    bg="gray",
    width=10,
    fg="black",
    relief=GROOVE,
    bd=5,
)
maxvaluelabel.place(x=500, y=60)
maxvalue = Scale(
    root,
    from_=0,
    to=100,
    resolution=1,
    orient=HORIZONTAL,
    font=("arial", 14, "italic bold"),
    relief=GROOVE,
    bd=2,
    width=10,
)
maxvalue.place(x=620, y=60)


start_button = Button(
    root,
    text="Start Sorting",
    bg="gray",
    font=("arial", 12, "italic bold"),
    relief=SUNKEN,
    activebackground="blue",
    activeforeground="white",
    bd=5,
    width=12,
)
start_button.place(x=1000, y=0)

speedlabel = Label(
    root,
    text="Speed ",
    font=("new Roman", 12, "italic bold"),
    bg="orange",
    width=10,
    fg="black",
    relief=GROOVE,
    bd=5,
)
speedlabel.place(x=400, y=0)

speedscale = Scale(
    root,
    from_=0.1,
    to=5.0,
    resolution=0.5,
    length=200,
    digits=4,
    orient=HORIZONTAL,
    font=("arial", 14, "italic bold"),
    relief=GROOVE,
    bd=2,
    width=10,
)
speedscale.place(x=520, y=0)

timelabel = Label(
    root,
    text="Time",
    font=("new Roman", 12, "italic bold"),
    bg="orange",
    width=10,
    fg="black",
    relief=GROOVE,
    bd=5,
)
timelabel.place(x=750, y=0)

timelabelans = Label(
    root,
    text="total time",
    font=("new Roman", 12, "italic bold"),
    bg="white",
    width=10,
    fg="black",
    relief=GROOVE,
    bd=5,
)
timelabelans.place(x=860, y=0)
canvas = Canvas(root, width=1070, height=450, bg="black")
canvas.place(x=10, y=130)


root.mainloop()
