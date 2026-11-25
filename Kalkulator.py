import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x650")
root.configure(bg="#202020")
root.resizable(False, False)

# Fungsi trigonometri dalam derajat
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    if x % 180 == 90:
        raise ValueError("Tan tidak terdefinisi")
    return math.tan(math.radians(x))

def fact(x):
    return math.factorial(int(x))

# Fungsi layar
def tekan(nilai):
    layar.insert(tk.END, nilai)

def hapus():
    layar.delete(0, tk.END)

def delete_satu():
    teks = layar.get()
    layar.delete(0, tk.END)
    layar.insert(0, teks[:-1])

# Fungsi perhitungan
def hitung():
    try:
        ekspresi = layar.get()

        fungsi = {
            "sin": sin,
            "cos": cos,
            "tan": tan,
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "fact": fact
        }

        hasil = eval(
            ekspresi,
            {"__builtins__": None},
            fungsi
        )

        layar.delete(0, tk.END)
        layar.insert(0, str(round(hasil, 8)))

    except:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")


# Judul
judul = tk.Label(
    root,
    text="SCIENTIFIC CALCULATOR",
    font=("Arial", 19, "bold"),
    bg="#202020",
    fg="white"
)
judul.pack(pady=15)

# Layar
layar = tk.Entry(
    root,
    font=("Arial", 25),
    justify="right",
    bg="white",
    fg="black",
    bd=5
)
layar.pack(padx=15, pady=15, fill="x", ipady=15)

# Daftar tombol
tombol = [
    ["7", "8", "9", "÷", "C"],
    ["4", "5", "6", "×", "⌫"],
    ["1", "2", "3", "-", "("],
    ["0", ".", "=", "+", ")"],
    ["sin(", "cos(", "tan(", "√", "x²"],
    ["log(", "ln(", "π", "^", "!"],
]

# Membuat tombol
frame = tk.Frame(root, bg="#202020")
frame.pack(expand=True, fill="both", padx=10, pady=10)

for i, baris in enumerate(tombol):
    for j, teks in enumerate(baris):

        def perintah(t=teks):
            if t == "C":
                hapus()
            elif t == "⌫":
                delete_satu()
            elif t == "=":
                hitung()
            elif t == "÷":
                tekan("/")
            elif t == "×":
                tekan("*")
            elif t == "√":
                tekan("sqrt(")
            elif t == "x²":
                tekan("**2")
            elif t == "π":
                tekan("pi")
            elif t == "^":
                tekan("**")
            elif t == "!":
                tekan("!")
            elif t == "log(":
                tekan("log(")
            elif t == "ln(":
                tekan("ln(")
            else:
                tekan(t)

        warna = "#454545"

        if teks in ["+", "-", "×", "÷", "="]:
            warna = "#1479C9"
        elif teks in ["C", "⌫"]:
            warna = "#C0392B"
        elif teks in ["sin(", "cos(", "tan(", "√",
                      "x²", "log(", "ln(", "π", "^", "!"]:
            warna = "#666666"

        btn = tk.Button(
            frame,
            text=teks,
            font=("Arial", 14, "bold"),
            bg=warna,
            fg="white",
            command=perintah
        )

        btn.grid(
            row=i,
            column=j,
            sticky="nsew",
            padx=3,
            pady=4
        )

for i in range(6):
    frame.rowconfigure(i, weight=1)

for j in range(5):
    frame.columnconfigure(j, weight=1)

root.mainloop()