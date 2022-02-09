from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("661x551")
window.configure(bg = "#25414C")


canvas = Canvas(
    window,
    bg = "#25414C",
    height = 551,
    width = 661,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    330.0,
    275.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    193.25416564941406,
    34.01999855041504,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=485.339111328125,
    y=89.07831573486328,
    width=102.3941650390625,
    height=101.93497467041016
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=415.0824890136719,
    y=11.479166030883789,
    width=205.25173950195312,
    height=45.92120361328125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=18.825830459594727,
    y=235.36839294433594,
    width=141.69068908691406,
    height=31.814132690429688
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=167.46212768554688,
    y=235.36839294433594,
    width=141.69070434570312,
    height=31.814132690429688
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=464.6766357421875,
    y=235.55245971679688,
    width=141.690673828125,
    height=31.814117431640625
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=315.9066467285156,
    y=235.0933074951172,
    width=141.69070434570312,
    height=31.814132690429688
)

canvas.create_text(
    25.30841064453125,
    94.85446166992188,
    anchor="nw",
    text="Jour:",
    fill="#000000",
    font=("Montserrat SemiBold", 16 * -1)
)

canvas.create_text(
    25.30841064453125,
    142.13107299804688,
    anchor="nw",
    text="Heure de debut:",
    fill="#000000",
    font=("Montserrat SemiBold", 16 * -1)
)

canvas.create_text(
    25.30841064453125,
    189.40769958496094,
    anchor="nw",
    text="Description:",
    fill="#000000",
    font=("Montserrat SemiBold", 16 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=10.560832023620605,
    y=525.7457885742188,
    width=19.744163513183594,
    height=19.744140625
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=34.896663665771484,
    y=525.7457885742188,
    width=19.74416732788086,
    height=19.744140625
)

canvas.create_text(
    59.6916618347168,
    527.1233520507812,
    anchor="nw",
    text="2022 ALL RIGHTS ARE RESERVED TO YASSINE EL HAADAD",
    fill="#FFFFFF",
    font=("Kanit SemiBold", 11 * -1)
)

canvas.create_rectangle(
    25.254165649414062,
    288.3566589355469,
    628.1399688720703,
    500.032470703125,
    fill="#C4C4C4",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    285.7546691894531,
    104.64236831665039,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFC190",
    highlightthickness=0,
)
entry_1.place(
    x=189.21815395355225,
    y=88.59519958496094,
    width=193.07303047180176,
    height=30.094337463378906
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    285.7546691894531,
    152.29759216308594,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFC190",
    highlightthickness=0
)
entry_2.place(
    x=189.21815395355225,
    y=136.25042724609375,
    width=193.07303047180176,
    height=30.094329833984375
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    286.72723388671875,
    199.95282745361328,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFC190",
    highlightthickness=0
)
entry_3.place(
    x=190.19071865081787,
    y=183.90565490722656,
    width=193.07303047180176,
    height=30.094345092773438
)
window.resizable(False, False)
window.mainloop()
