from tkinter import *

window = Tk()
window.title("oi :)")
window.config(padx=20, pady=20)

def mile_to_km():
    km_result = float(miles_entry.get()) * 1.60934
    km_2_digit = f'{km_result:.2f}'
    result_label.config(text = km_2_digit)



# Entry
miles_entry = Entry(width= 10)
miles_entry.grid(column=1, row=0)

# Label: miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label: is equal to
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

# Label: <result>
result = 0
result_label = Label(text = result)
result_label.grid(column=1, row=1)

# Label: Km
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button: Calculate
calc_btn = Button(text="Calculate", command=mile_to_km)
calc_btn.grid(column=1, row=2)


window.mainloop()