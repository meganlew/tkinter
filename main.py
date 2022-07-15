import tkinter as tk
import numpy as np
import tkmacosx as tkm
import matplotlib.pyplot as plt
from finiteSource_functions import ellipseSource
#import finiteSource_functions    # this runs that code and defines the function
#finiteSource_functions.ellipseSource()   # this calls the function ellipseSource() that is defined in the other file


#  Fault Rupture Type, Dropdown menu options
RuptureList = [
    "Normal",
    "Reverse",
    "Strike-Slip (Left-Lateral)",
    "Strike-Slip (Right-Lateral)",
    "Thrust"
]
# Rupture Area Shape
ShapeList = [
    "Ellipse",
    "Rectangle"
]
# Source Time Function
SourceList = [
    "Gaussian",
    "Ricker",
    "Triangle",
    "Brune",
    "Brune Smoothed",
    "Liu"
]

root = tk.Tk()

root.title("Rupture Generator")

# setting the windows size
root.geometry("900x400")


# variables in the first column
scenario_name = tk.StringVar()  # scenario name (str)
earthquake_mag = tk.DoubleVar()  # earthquake magnitude (float)
seismic_moment = tk.DoubleVar()  # seismic moment (float)

# variables in the second column
fault_rupture = tk.StringVar()  # fault rupture type (str menu)
strike_degrees = tk.DoubleVar()  # strike(degrees) (float)
dip_degrees = tk.DoubleVar()  # dip(degrees) (float)
rake_degrees = tk.DoubleVar()  # rake(degrees) (float)
centroid_x = tk.DoubleVar()  # slip centroid,x (float)
centroid_y = tk.DoubleVar()  # slip centroid,y (float)
centroid_z = tk.DoubleVar()  # slip centroid,z (float)
rupture_area = tk.StringVar()  # rupture area shape (str menu)
aspect_ratio = tk.DoubleVar()  # aspect ratio (float)

# variables in the third column
hypocenter_x = tk.DoubleVar()  # hypocenter location, x (float)
hypocenter_y = tk.DoubleVar()  # hypocenter location, y (float)
hypocenter_z = tk.DoubleVar()  # hypocenter location, z (float)
rupture_velocity = tk.DoubleVar()  # rupture velocity(m/s) (float)
source_time = tk.StringVar()  # source time function (menu)
boolean1 = tk.BooleanVar()
boolean2 = tk.BooleanVar()

# set default as first index in the list
fault_rupture.set(RuptureList[0])
rupture_area.set(ShapeList[0])
source_time.set(SourceList[0])


# defining a function that will
# print them on the screen when button is clicked
def submit():
    ellipseSource()
    # first column
    scenario = scenario_name.get()
    MW = earthquake_mag.get()
    M0 = seismic_moment.get()

    # second column
    rupture = fault_rupture.get()
    strike = strike_degrees.get()
    dip = dip_degrees.get()
    rake = rake_degrees.get()
    slip_x = centroid_x.get()
    slip_y = centroid_y.get()
    slip_z = centroid_z.get()
    area = rupture_area.get()
    ratio = aspect_ratio.get()

    # third column
    location_x = hypocenter_x.get()
    location_y = hypocenter_y.get()
    location_z = hypocenter_z.get()
    velocity = rupture_velocity.get()
    time = source_time.get()
    bool1 = boolean1.get()
    bool2 = boolean2.get()

    print("Scenario Name: " + scenario)
    print("Earthquake Magnitude: " + str(MW))
    print("Seismic Moment: " + str(M0))

    print("Fault Rupture Type: " + rupture)
    print("Strike (degrees): " + str(strike))
    print("Dip (degrees): " + str(dip))
    print("Rake (degrees): " + str(rake))
    print("Slip Centroid, X: " + str(slip_x))
    print("Slip Centroid, Y: " + str(slip_y))
    print("Slip Centroid, Z: " + str(slip_z))
    print("Rupture Area Shape: " + area)
    print("Aspect Ratio: " + str(ratio))

    print("Hypocenter Location, X: " + str(location_x))
    print("Hypocenter Location, Y: " + str(location_y))
    print("Hypocenter Location, Z: " + str(location_z))
    print("Rupture Velocity (m/s): " + str(velocity))
    print("Source Time Function: " + time)

    scenario_name.set("")
    earthquake_mag.set(1.2)
    fault_rupture.set("")
    seismic_moment.set(1.2)

    dSig = 3.0 * 1.0e6
    kBrune = 0.38
    Vs = 3000.0
    # != not empty , == is empty
    # if (notEmpty(MW) & notEmpty(M0)

    if MW != 0.0 and M0 != 0.0:
        # earthquake magnitude to seismic moment
        MwtoM0 = 10.0 ** (1.5 * earthquake + 9.05)
        print("Ignoring user input from M0, calculating M0 from MW")
        print("MwtoM0: " + str(MwtoM0))
        # earthquake magnitude to corner frequency
        print("M0tofc: " + str(kBrune * Vs * np.power(((16.0 / 7.0) * dSig / MwtoM0), (1.0 / 3.0))))
        # earthquake magnitude to fault width
        print("MwtoRW: " + str(10.0 ** (-1.01 + 0.32 * MW)))
        # earthquake magnitude to fault length
        print("MwtoRLD: " + str(10.0 ** (-2.44 + 0.59 * MW)))
        # magnitude to area of fault path that slipped
        print("MwtoRA: " + str(10.0 ** (-3.49 + 0.91 * MW)))
        # elif (notEmpty(MW) & isEmpty (M0))
    elif MW != 0.0 and M0 == 0.0:
        MwtoM0 = 10.0 ** (1.5 * MW + 9.05)
        print("MwtoM0: " + str(MwtoM0))
        # earthquake magnitude to corner frequency
        print("M0tofc: " + str(kBrune * Vs * np.power(((16.0 / 7.0) * dSig / MwtoM0), (1.0 / 3.0))))
        # earthquake magnitude to fault width
        print("MwtoRW: " + str(10.0 ** (-1.01 + 0.32 * MW)))
        # earthquake magnitude to fault length
        print("MwtoRLD: " + str(10.0 ** (-2.44 + 0.59 * MW)))
        # magnitude to area of fault path that slipped
        print("MwtoRA: " + str(10.0 ** (-3.49 + 0.91 * MW)))
        # elif (isEmpty(MW) & notEmpty(M0))
    elif MW == 0.0 and M0 != 0.0:
        M0toMw = (np.log10(M0) - 9.05) / 1.5
        print("M0toMw: " + str(M0toMw))
        # seismic moment to corner frequency
        print("M0tofc: " + str(kBrune * Vs * np.power(((16.0 / 7.0) * dSig / M0), (1.0 / 3.0))))
    else:
        print("Error, no magnitude information given.")


# creates a new window popup
    window = tk.Toplevel(root)
    window.geometry("900x400")
    window.title("Rupture Generator Results")
    # labels for first column
    scenario_text = tk.Label(window, text='Scenario Name', font=('calibre', 12, 'bold'))
    text_scenario = tk.Label(window, text=scenario, font=('calibre', 12))
    earthquake_text = tk.Label(window, text='Earthquake Magnitude', font=('calibre', 12, 'bold'))
    text_earthquake = tk.Label(window, text=MW, font=('calibre', 12))
    seismic_text = tk.Label(window, text='Seismic Moment', font=('calibre', 12, 'bold'))
    text_seismic = tk.Label(window, text=M0, font=('calibre', 12))
    # labels for the second column
    rupture_text = tk.Label(window, text='Fault Rupture Type', font=('calibre', 12, 'bold'))
    text_rupture = tk.Label(window, text=rupture, font=('calibre', 12))
    strike_text = tk.Label(window, text='Strike (degrees) ', font=('calibre', 12, 'bold'))
    text_strike = tk.Label(window, text=strike, font=('calibre', 12))
    dip_text = tk.Label(window, text='Dip (degrees)', font=('calibre', 12, 'bold'))
    text_dip = tk.Label(window, text=dip, font=('calibre', 12))
    rake_text = tk.Label(window, text='Rake (degrees)', font=('calibre', 12, 'bold'))
    text_rake = tk.Label(window, text=rake, font=('calibre', 12))
    slipX_text = tk.Label(window, text='Slip Centroid, X', font=('calibre', 12, 'bold'))
    text_slipX = tk.Label(window, text=slip_x, font=('calibre', 12))
    slipY_text = tk.Label(window, text='Slip Centroid, Y', font=('calibre', 12, 'bold'))
    text_slipY = tk.Label(window, text=slip_y, font=('calibre', 12))
    slipZ_text = tk.Label(window, text='Slip Centroid, X', font=('calibre', 12, 'bold'))
    text_slipZ = tk.Label(window, text=slip_z, font=('calibre', 12))
    area_text = tk.Label(window, text='Rupture Area Shape', font=('calibre', 12, 'bold'))
    text_area = tk.Label(window, text=area, font=('calibre', 12))
    ratio_text = tk.Label(window, text='Rupture Area Shape', font=('calibre', 12, 'bold'))
    text_ratio = tk.Label(window, text=ratio, font=('calibre', 12))
    # labels for third column
    hypocenterX_text = tk.Label(window, text='Hypocenter location, X', font=('calibre', 12, 'bold'))
    text_hypocenterX = tk.Label(window, text=location_x, font=('calibre', 12))
    hypocenterY_text = tk.Label(window, text='Hypocenter location, Y', font=('calibre', 12, 'bold'))
    text_hypocenterY = tk.Label(window, text=location_y, font=('calibre', 12))
    hypocenterZ_text = tk.Label(window, text='Hypocenter location, Z', font=('calibre', 12, 'bold'))
    text_hypocenterZ = tk.Label(window, text=location_z, font=('calibre', 12))
    velocity_text = tk.Label(window, text='Rupture Velocity (m/s)', font=('calibre', 12, 'bold'))
    text_velocity = tk.Label(window, text=velocity, font=('calibre', 12))
    time_text = tk.Label(window, text='Source Time Function', font=('calibre', 12, 'bold'))
    text_time = tk.Label(window, text=time, font=('calibre', 12))

    # grid to display first column of inputs received from user
    scenario_text.grid(row=0, column=0)
    text_scenario.grid(row=0, column=1)
    earthquake_text.grid(row=1, column=0)
    text_earthquake.grid(row=1, column=1)
    seismic_text.grid(row=2, column=0)
    text_seismic.grid(row=2, column=1)
    # second column grid
    rupture_text.grid(row=0, column=2)
    text_rupture.grid(row=0, column=3)
    strike_text.grid(row=1, column=2)
    text_strike.grid(row=1, column=3)
    dip_text.grid(row=2, column=2)
    text_dip.grid(row=2, column=3)
    rake_text.grid(row=3, column=2)
    text_rake.grid(row=3, column=3)
    slipX_text.grid(row=4, column=2)
    text_slipX.grid(row=4, column=3)
    slipY_text.grid(row=5, column=2)
    text_slipY.grid(row=5, column=3)
    slipZ_text.grid(row=6, column=2)
    text_slipZ.grid(row=6, column=3)
    area_text.grid(row=7, column=2)
    text_area.grid(row=7, column=3)
    ratio_text.grid(row=8, column=2)
    text_ratio.grid(row=8, column=3)
    # third column grid
    hypocenterX_text.grid(row=0, column=4)
    text_hypocenterX.grid(row=0, column=5)
    hypocenterY_text.grid(row=1, column=4)
    text_hypocenterY.grid(row=1, column=5)
    hypocenterZ_text.grid(row=2, column=4)
    text_hypocenterZ.grid(row=2, column=5)
    velocity_text.grid(row=3, column=4)
    text_velocity.grid(row=3, column=5)
    time_text.grid(row=4, column=4)
    text_time.grid(row=4, column=5)


# label, entry, menu ( first column )
# creating a label for fault name
scenario_label = tk.Label(root, text='Scenario Name', font=('calibre', 10, 'bold'))
# creating a entry for fault name
scenario_entry = tk.Entry(root, textvariable=scenario_name, font=('calibre', 10, 'normal'))
# creating a label for
# earthquake mag using widget Label
earthquake_label = tk.Label(root, text='Earthquake Magnitude', font=('calibre', 10, 'bold'))
# creating a entry for input
# earthquake mag using widget Entry
earthquake_entry = tk.Entry(root, textvariable=earthquake_mag, font=('calibre', 10, 'normal'))
# creating a label for seismic moment type
seismic_label = tk.Label(root, text='Seismic Moment', font=('calibre', 10, 'bold'))
# creating an entry for seismic moment type
seismic_entry = tk.Entry(root, textvariable=seismic_moment, font=('calibre', 10, 'normal'))

# second column
# creating a label for fault rupture type
rupture_label = tk.Label(root, text='Fault Rupture Type', font=('calibre', 10, 'bold'))
# creating menu for fault rupture type
rupture_entry = tk.OptionMenu(root, fault_rupture, *RuptureList)
strike_label = tk.Label(root, text='Strike (degrees)', font=('calibre', 10, 'bold'))
strike_entry = tk.Entry(root, textvariable=strike_degrees, font=('calibre', 10, 'normal'))
dip_label = tk.Label(root, text='Dip (degrees)', font=('calibre', 10, 'bold'))
dip_entry = tk.Entry(root, textvariable=dip_degrees, font=('calibre', 10, 'normal'))
rake_label = tk.Label(root, text='Rake (degrees)', font=('calibre', 10, 'bold'))
rake_entry = tk.Entry(root, textvariable=rake_degrees, font=('calibre', 10, 'normal'))
slipX_label = tk.Label(root, text='Slip Centroid, X', font=('calibre', 10, 'bold'))
slipX_entry = tk.Entry(root, textvariable=centroid_x, font=('calibre', 10, 'normal'))
slipY_label = tk.Label(root, text='Slip Centroid, Y', font=('calibre', 10, 'bold'))
slipY_entry = tk.Entry(root, textvariable=centroid_y, font=('calibre', 10, 'normal'))
slipZ_label = tk.Label(root, text='Slip Centroid, Z', font=('calibre', 10, 'bold'))
slipZ_entry = tk.Entry(root, textvariable=centroid_z, font=('calibre', 10, 'normal'))
area_label = tk.Label(root, text='Rupture Area Shape', font=('calibre', 10, 'bold'))
area_entry = tk.OptionMenu(root, rupture_area, *ShapeList)
ratio_label = tk.Label(root, text='Aspect ratio', font=('calibre', 10, 'bold'))
ratio_entry = tk.Entry(root, textvariable=aspect_ratio, font=('calibre', 10, 'normal'))

# third column
hypocenterX_label = tk.Label(root, text='Hypocenter Location, X', font=('calibre', 10, 'bold'))
hypocenterX_entry = tk.Entry(root, textvariable=hypocenter_x, font=('calibre', 10, 'normal'))
hypocenterY_label = tk.Label(root, text='Hypocenter Location, Y', font=('calibre', 10, 'bold'))
hypocenterY_entry = tk.Entry(root, textvariable=hypocenter_y, font=('calibre', 10, 'normal'))
hypocenterZ_label = tk.Label(root, text='Hypocenter Location, Z', font=('calibre', 10, 'bold'))
hypocenterZ_entry = tk.Entry(root, textvariable=hypocenter_z, font=('calibre', 10, 'normal'))
velocity_label = tk.Label(root, text='Rupture Velocity (m/s)', font=('calibre', 10, 'bold'))
velocity_entry = tk.Entry(root, textvariable=rupture_velocity, font=('calibre', 10, 'normal'))
time_label = tk.Label(root, text='Source Time Function', font=('calibre', 10, 'bold'))
time_entry = tk.OptionMenu(root, source_time, *SourceList)
c1 = tk.Checkbutton(root, text='Visualize', variable=boolean1, onvalue=1, offvalue=0)
c2 = tk.Checkbutton(root, text='Save File', variable=boolean2, onvalue=1, offvalue=0)


# creating a button using the widget
# Button that will call the submit function
sub_btn = tkm.Button(root, text='Submit', command=submit, fg='white', background='#5EA6F7')
# quit button
quit_button = tkm.Button(root, text='Quit', fg='white', background='#E4683C', command=root.quit)

# placing the label and entry in
# the required position using grid
# method ( grid for first column)
scenario_label.grid(row=0, column=0)
scenario_entry.grid(row=0, column=1)
earthquake_label.grid(row=1, column=0)
earthquake_entry.grid(row=1, column=1)
seismic_label.grid(row=2, column=0)
seismic_entry.grid(row=2, column=1)

# grid for second column
rupture_label.grid(row=0, column=2)
rupture_entry.grid(row=0, column=3)
strike_label.grid(row=1, column=2)
strike_entry.grid(row=1, column=3)
dip_label.grid(row=2, column=2)
dip_entry.grid(row=2, column=3)
rake_label.grid(row=3, column=2)
rake_entry.grid(row=3, column=3)
slipX_label.grid(row=4, column=2)
slipX_entry.grid(row=4, column=3)
slipY_label.grid(row=5, column=2)
slipY_entry.grid(row=5, column=3)
slipZ_label.grid(row=6, column=2)
slipZ_entry.grid(row=6, column=3)
area_label.grid(row=7, column=2)
area_entry.grid(row=7, column=3)
ratio_label.grid(row=8, column=2)
ratio_entry.grid(row=8, column=3)

# grid for third column
hypocenterX_label.grid(row=0, column=4)
hypocenterX_entry.grid(row=0, column=5)
hypocenterY_label.grid(row=1, column=4)
hypocenterY_entry.grid(row=1, column=5)
hypocenterZ_label.grid(row=2, column=4)
hypocenterZ_entry.grid(row=2, column=5)
velocity_label.grid(row=3, column=4)
velocity_entry.grid(row=3, column=5)
time_label.grid(row=4, column=4)
time_entry.grid(row=4, column=5)
c1.grid(row=5, column=4)
c2.grid(row=6, column=4)
sub_btn.grid(row=7, column=5)
quit_button.grid(row=8, column=5)

# performing an infinite loop
# for the window to display
root.mainloop()













