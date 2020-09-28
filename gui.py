from tkinter import *
from tkinter import ttk
import random
import time
from Sort import bubblesort, quicksort, mergesort, insertionsort, selectionsort

root = Tk()
root.title("VisualAlgo")
root.geometry("1100x600+200+80")
root.config(bg="lightblue")
array = []
times = 0.0


def Generate_data(x, colorarr):

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
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarr[i])
        root.update()


def Start_Sort():
    disableButton()
    global array
    global times
    if not array:
        return
    if algo_menu.get() == "Quick Sort":
        start = time.time()
        quicksort(array, 0, len(array) - 1, Generate_data, speedscale.get())
        Generate_data(array, ["yellow" for x in range(len(array))])
        end = time.time()
    elif algo_menu.get() == "Bubble Sort":
        start = time.time()
        bubblesort(array, Generate_data, speedscale.get())
        end = time.time()
    elif algo_menu.get() == "Selection Sort":
        start = time.time()
        selectionsort(array, Generate_data, speedscale.get())
        end = time.time()
    elif algo_menu.get() == "Insertion Sort":
        start = time.time()
        insertionsort(array, Generate_data, speedscale.get())
        end = time.time()
    elif algo_menu.get() == "Choose algorithm":
        start = time.time()
        end = time.time()
    elif algo_menu.get() == "Merge Sort":
        start = time.time()
        mergesort(array, Generate_data, speedscale.get())
        Generate_data(array, ["lightgreen" for x in range(len(array))])
        end = time.time()
    enableButton()
    times = end - start
    timelabelans = Label(
        root,
        text=round(times, 3),
        font=("new Roman", 12, "italic bold"),
        bg="white",
        width=10,
        fg="black",
        relief=GROOVE,
        bd=5,
    )
    timelabelans.place(x=860, y=0)
    



def Algo_select():
    global array
    print("Algo:", select_algo.get())
    min = int(minvalue.get())
    max = int(maxvalue.get())
    size = int(sizevalue.get())

    array = []
    for _ in range(size):
        array.append(random.randrange(min, max + 1))
    Generate_data(array, ["red" for x in range(len(array))])


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


def disableButton():
    sizevalue.configure(state=DISABLED)
    maxvalue.configure(state=DISABLED)
    minvalue.configure(state=DISABLED)
    generate_button.configure(state=DISABLED)
    speedscale.configure(state=DISABLED)
    algo_menu.configure(state=DISABLED)
def enableButton():
    sizevalue.configure(state="normal")
    maxvalue.configure(state="normal")
    minvalue.configure(state="normal")
    generate_button.configure(state="normal")
    speedscale.configure(state="normal")
    algo_menu.configure(state="normal")   


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
    to=200,
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
    to=500,
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
    command=Start_Sort,
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
    digits=2,
    orient=HORIZONTAL,
    font=("arial", 14, "italic bold"),
    relief=GROOVE,
    bd=2,
    width=10,
)
speedscale.place(x=520, y=0)

timelabel = Label(
    root,
    text="Time (seconds) ",
    font=("new Roman", 12, "italic bold"),
    bg="orange",
    width=12,
    fg="black",
    relief=GROOVE,
    bd=5,
)


timelabel.place(x=750, y=0)

canvas = Canvas(root, width=1070, height=450, bg="black")
canvas.place(x=10, y=130)


root.mainloop()

