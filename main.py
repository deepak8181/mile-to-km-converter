from tkinter import *


def mile_to_km():
    miles=float(miles_input.get())
    km=miles*1.60934
    result_km.config(text=f"{km}")
window=Tk()
window.title("Mile to km Converter")
window.config(padx=20, pady=20)
miles_input= Entry(width=7)
miles_input.grid(column=1, row=0)


miles_label= Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label=Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_km=Label(text="0")
result_km.grid(column=1, row=1)


km_label=Label(text="km")
km_label.grid(column=2, row=1)


calculate_button=Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)





















window.mainloop()

