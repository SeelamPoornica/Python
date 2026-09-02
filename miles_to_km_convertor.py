import tkinter as tk

window=tk.Tk()
window.title("Mile to Km Converter")
window.geometry("300x200")
window.config(padx=20,pady=20)

miles=tk.Entry()
miles.grid(row=1,column=2)
t1=tk.Label(text="Miles")
t1.grid(row=1,column=3)

t3=tk.Label(text="is equal to")
t3.grid(row=2,column=1)
km = tk.Label(text="0")
km.grid(row=2,column=2)
t2=tk.Label(text="Km")
t2.grid(row=2,column=3)

def clicked():
    val=int(miles.get())
    val=val*1.6
    km.config(text=str(round(val, 3)))

cal=tk.Button(text="Calculate",command=clicked)
cal.grid(row=3,column=2)

window.mainloop()
