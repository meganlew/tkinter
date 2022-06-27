import tkinter as tk

# Dropdown menu options
OptionList = [
    "Normal",
    "Reverse",
    "Strike-Slip (Left-Lateral)",
    "Strike-Slip (Right-Lateral)",
    "Thrust"
]

root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring variables
# for storing earthquake magnitude (float), fault name (str), fault rupture type(str)
earthquake_mag = tk.DoubleVar()
fault_name = tk.StringVar()
fault_rupture = tk.StringVar()

# set default as first index in the list
fault_rupture.set(OptionList[0])


# defining a function that will
# print them on the screen when button is clicked
def submit():
    earthquake = earthquake_mag.get()
    fault = fault_name.get()
    rupture = fault_rupture.get()

    print("Earthquake Magnitude: " + str(earthquake))
    print("Fault Name: " + fault)
    print("Fault Rupture Type: " + rupture)

    earthquake_mag.set("")
    fault_name.set("")
    fault_rupture.set("")


# creating a label for
# earthquake mag using widget Label
earthquake_label = tk.Label(root, text='Earthquake Magnitude', font=('calibre', 10, 'bold'))

# creating a entry for input
# earthquake mag using widget Entry
earthquake_entry = tk.Entry(root, textvariable=earthquake_mag, font=('calibre', 10, 'normal'))

# creating a label for fault name
fault_label = tk.Label(root, text='Fault Name', font=('calibre', 10, 'bold'))

# creating a entry for fault name
fault_entry = tk.Entry(root, textvariable=fault_name, font=('calibre', 10, 'normal'))

# creating a label for fault rupture type
rupture_label = tk.Label(root, text='Fault Rupture Type', font=('calibre', 10, 'bold'))

# creating an entry for fault rupture type
rupture_entry = tk.OptionMenu(root, fault_rupture, *OptionList)

# opt = tk.OptionMenu(root, fault_rupture, *OptionList)
# opt.config(width=90, font=('helvetica', 12))


# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
earthquake_label.grid(row=0, column=0)
earthquake_entry.grid(row=0, column=1)
fault_label.grid(row=1, column=0)
fault_entry.grid(row=1, column=1)
rupture_label.grid(row=2, column=0)
rupture_entry.grid(row=2, column=1)
sub_btn.grid(row=3, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
