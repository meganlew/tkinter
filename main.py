import tkinter as tk
import numpy as np
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
seismic_moment = tk.DoubleVar()

# set default as first index in the list
fault_rupture.set(OptionList[0])


# defining a function that will
# print them on the screen when button is clicked
def submit():
    earthquake = earthquake_mag.get()
    fault = fault_name.get()
    rupture = fault_rupture.get()
    seismic = seismic_moment.get()

    print("Earthquake Magnitude: " + str(earthquake))
    print("Fault Name: " + fault)
    print("Fault Rupture Type: " + rupture)
    print("Seismic Moment: " + str(seismic))

    earthquake_mag.set("")
    fault_name.set("")
    fault_rupture.set("")
    seismic_moment.set("")

    # Mw = 10.0 ** (1.5 * earthquake + 9.05)
    # print("MwtoM0: " + str(Mw))

    # def MwtoM0(Mw):
       #  return 10.0 ** (1.5 * Mw + 9.05)

    def MwtoM0():
        # earthquake magnitude to seismic moment
        Mw = 10.0 ** (1.5 * earthquake + 9.05)
        print("MwtoM0: " + str(Mw))
    MwtoM0()

    #def M0toMw(M0):
       # return (np.log10(M0) - 9.05) / 1.5;

    def M0toMw():
        # seismic moment to earthquake magnitude
        M0 = (np.log10(seismic) - 9.05) / 1.5;
        print("M0toMw: " + str(M0))
    M0toMw()

    # def M0tofc(M0, dSig=3.0 * 1.0e6, kBrune=0.38, Vs=3000.0):
       # return kBrune * Vs * np.power(((16.0 / 7.0) * dSig / M0), (1.0 / 3.0))

    def M0tofc(dSig=3.0 * 1.0e6, kBrune=0.38, Vs=3000.0):
        # earthquake magnitude to corner frequency
        print("M0tofc: " + str(kBrune * Vs * np.power(((16.0 / 7.0) * dSig / seismic), (1.0 / 3.0))))
    M0tofc()

    # def MwtoRW(Mw, author='wellscoppersmith', faulttype='All'):
    # return 10.0 ** (-1.01 + 0.32 * Mw)

    def MwtoRW(author='wellscoppersmith', faulttype='All'):
        print("MwtoRW: " + str(10.0 ** (-1.01 + 0.32 * earthquake)))
    MwtoRW()

    # def MwtoRLD(Mw, author='wellscoppersmith', faulttype='All'):
    # return 10.0 ** (-2.44 + 0.59 * Mw)

    def MwtoRLD(author='wellscoppersmith', faulttype='All'):
        print("MwtoRLD: " + str(10.0 ** (-2.44 + 0.59 * earthquake)))
    MwtoRLD()

    # def MwtoRA(Mw, author='wellscoppersmith', faulttype='All'):
    # return 10.0 ** (-3.49 + 0.91 * Mw)

    def MwtoRA(author='wellscoppersmith', faulttype='All'):
        # magnitude to area of fault path that slipped
        print("MwtoRA: " + str(10.0 ** (-3.49 + 0.91 * earthquake)))
    MwtoRA()


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

# creating a label for seismic moment type
seismic_label = tk.Label(root, text='Seismic Moment', font=('calibre', 10, 'bold'))

# creating an entry for seismic moment type
seismic_entry = tk.Entry(root, textvariable=seismic_moment, font=('calibre', 10, 'normal'))


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
seismic_label.grid(row=3, column=0)
seismic_entry.grid(row=3, column=1)
sub_btn.grid(row=4, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()


