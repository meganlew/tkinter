import tkinter as tk
import numpy as np
import tkmacosx as tkm
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
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
root.geometry("950x600")

# variables in the first column
scenario_name = tk.StringVar()  # scenario name (str)
earthquake_mag = tk.DoubleVar()  # earthquake magnitude (float)
# seismic_moment = tk.DoubleVar()  # seismic moment (float)

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
boolean0 = tk.BooleanVar()
boolean1 = tk.BooleanVar()
boolean2 = tk.BooleanVar()
boolean3 = tk.BooleanVar()
boolean4 = tk.BooleanVar()

# set default as first index in the list
fault_rupture.set(RuptureList[0])
rupture_area.set(ShapeList[0])
source_time.set(SourceList[0])


def submit():
        main = tk.Toplevel(root)
        main.geometry("900x400")
        main.title("Rupture Generator")

        # first column
        scenario = scenario_name.get()
        Mw = earthquake_mag.get()
        # M0 = seismic_moment.get()

        # second column
        rupture = fault_rupture.get()
        strike = strike_degrees.get()
        dip = dip_degrees.get()
        rake = rake_degrees.get()
        centroidX = centroid_x.get()
        centroidY = centroid_y.get()
        centroidZ = centroid_z.get()
        area = rupture_area.get()
        aspectRatio = aspect_ratio.get()

        # third column
        hypoX = hypocenter_x.get()
        hypoY = hypocenter_y.get()
        hypoZ = hypocenter_z.get()
        velocity = rupture_velocity.get()
        time = source_time.get()
        bool0 = boolean0.get()
        bool1 = boolean1.get()
        bool2 = boolean2.get()
        bool3 = boolean3.get()
        bool4 = boolean4.get()

        ellipseSource(Mw, bool1, bool2, bool3, bool4)

        scenario_name.set("")
        earthquake_mag.set(4.5)
        fault_rupture.set("")
        # seismic_moment.set(1.2)
        strike_degrees.set(0.0)
        dip_degrees.set(90.0)
        rake_degrees.set(180.0)

        # label, entry, menu ( first column )
        # creating a label for fault name
        scenario_label = tk.Label(main, text='Scenario Name', font=('calibre', 10, 'bold'))
        # creating a entry for fault name
        scenario_entry = tk.Entry(main, textvariable=scenario_name, font=('calibre', 10, 'normal'))
        # creating a label for
        # earthquake mag using widget Label
        earthquake_label = tk.Label(main, text='Earthquake Magnitude', font=('calibre', 10, 'bold'))
        # creating a entry for input
        # earthquake mag using widget Entry
        earthquake_entry = tk.Entry(main, textvariable=earthquake_mag, font=('calibre', 10, 'normal'))
        # creating a label for seismic moment type
        # seismic_label = tk.Label(root, text='Seismic Moment', font=('calibre', 10, 'bold'))
        # # creating an entry for seismic moment type
        # seismic_entry = tk.Entry(root, textvariable=seismic_moment, font=('calibre', 10, 'normal'))

        # second column
        # creating a label for fault rupture type
        rupture_label = tk.Label(main, text='Fault Rupture Type', font=('calibre', 10, 'bold'))
        # creating menu for fault rupture type
        rupture_entry = tk.OptionMenu(main, fault_rupture, *RuptureList)
        strike_label = tk.Label(main, text='Strike (degrees)', font=('calibre', 10, 'bold'))
        strike_entry = tk.Entry(main, textvariable=strike_degrees, font=('calibre', 10, 'normal'))
        dip_label = tk.Label(main, text='Dip (degrees)', font=('calibre', 10, 'bold'))
        dip_entry = tk.Entry(main, textvariable=dip_degrees, font=('calibre', 10, 'normal'))
        rake_label = tk.Label(main, text='Rake (degrees)', font=('calibre', 10, 'bold'))
        rake_entry = tk.Entry(main, textvariable=rake_degrees, font=('calibre', 10, 'normal'))
        slipX_label = tk.Label(main, text='Slip Centroid, X', font=('calibre', 10, 'bold'))
        slipX_entry = tk.Entry(main, textvariable=centroid_x, font=('calibre', 10, 'normal'))
        slipY_label = tk.Label(main, text='Slip Centroid, Y', font=('calibre', 10, 'bold'))
        slipY_entry = tk.Entry(main, textvariable=centroid_y, font=('calibre', 10, 'normal'))
        slipZ_label = tk.Label(main, text='Slip Centroid, Z', font=('calibre', 10, 'bold'))
        slipZ_entry = tk.Entry(main, textvariable=centroid_z, font=('calibre', 10, 'normal'))
        area_label = tk.Label(main, text='Rupture Area Shape', font=('calibre', 10, 'bold'))
        area_entry = tk.OptionMenu(main, rupture_area, *ShapeList)
        ratio_label = tk.Label(main, text='Aspect ratio', font=('calibre', 10, 'bold'))
        ratio_entry = tk.Entry(main, textvariable=aspect_ratio, font=('calibre', 10, 'normal'))

        # third column
        hypocenterX_label = tk.Label(main, text='Hypocenter Location, X', font=('calibre', 10, 'bold'))
        hypocenterX_entry = tk.Entry(main, textvariable=hypocenter_x, font=('calibre', 10, 'normal'))
        hypocenterY_label = tk.Label(main, text='Hypocenter Location, Y', font=('calibre', 10, 'bold'))
        hypocenterY_entry = tk.Entry(main, textvariable=hypocenter_y, font=('calibre', 10, 'normal'))
        hypocenterZ_label = tk.Label(main, text='Hypocenter Location, Z', font=('calibre', 10, 'bold'))
        hypocenterZ_entry = tk.Entry(main, textvariable=hypocenter_z, font=('calibre', 10, 'normal'))
        velocity_label = tk.Label(main, text='Rupture Velocity (m/s)', font=('calibre', 10, 'bold'))
        velocity_entry = tk.Entry(main, textvariable=rupture_velocity, font=('calibre', 10, 'normal'))
        time_label = tk.Label(main, text='Source Time Function', font=('calibre', 10, 'bold'))
        time_entry = tk.OptionMenu(main, source_time, *SourceList)
        c0 = tk.Checkbutton(main, text='Show Report', variable=boolean0, onvalue=1, offvalue=0)
        c1 = tk.Checkbutton(main, text='Visualize 2D', variable=boolean1, onvalue=1, offvalue=0)
        c2 = tk.Checkbutton(main, text='Visualize 3D', variable=boolean2, onvalue=1, offvalue=0)
        c3 = tk.Checkbutton(main, text='Save File (Ascii List)', variable=boolean3, onvalue=1, offvalue=0)
        c4 = tk.Checkbutton(main, text='Save File (SW4 format)', variable=boolean4, onvalue=1, offvalue=0)

        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = tkm.Button(main, text='Submit', command=submit, fg='white', background='#5EA6F7')
        # quit button
        quit_button = tkm.Button(main, text='Quit', fg='white', background='#E4683C', command=root.quit)

        # placing the label and entry in
        # the required position using grid
        # method ( grid for first column)
        scenario_label.grid(row=0, column=0, sticky='w')
        scenario_entry.grid(row=0, column=1, sticky='w')
        earthquake_label.grid(row=1, column=0, sticky='w')
        earthquake_entry.grid(row=1, column=1, sticky='w')
        # seismic_label.grid(row=2, column=0)
        # seismic_entry.grid(row=2, column=1)

        # grid for second column
        rupture_label.grid(row=0, column=2, sticky='w')
        rupture_entry.grid(row=0, column=3, sticky='w')
        strike_label.grid(row=1, column=2, sticky='w')
        strike_entry.grid(row=1, column=3, sticky='w')
        dip_label.grid(row=2, column=2, sticky='w')
        dip_entry.grid(row=2, column=3, sticky='w')
        rake_label.grid(row=3, column=2, sticky='w')
        rake_entry.grid(row=3, column=3, sticky='w')
        slipX_label.grid(row=4, column=2, sticky='w')
        slipX_entry.grid(row=4, column=3, sticky='w')
        slipY_label.grid(row=5, column=2, sticky='w')
        slipY_entry.grid(row=5, column=3, sticky='w')
        slipZ_label.grid(row=6, column=2, sticky='w')
        slipZ_entry.grid(row=6, column=3, sticky='w')
        area_label.grid(row=7, column=2, sticky='w')
        area_entry.grid(row=7, column=3, sticky='w')
        ratio_label.grid(row=8, column=2, sticky='w')
        ratio_entry.grid(row=8, column=3, sticky='w')

        # grid for third column
        hypocenterX_label.grid(row=0, column=4, sticky='w')
        hypocenterX_entry.grid(row=0, column=5, sticky='w')
        hypocenterY_label.grid(row=1, column=4, sticky='w')
        hypocenterY_entry.grid(row=1, column=5, sticky='w')
        hypocenterZ_label.grid(row=2, column=4, sticky='w')
        hypocenterZ_entry.grid(row=2, column=5, sticky='w')
        velocity_label.grid(row=3, column=4, sticky='w')
        velocity_entry.grid(row=3, column=5, sticky='w')
        time_label.grid(row=4, column=4, sticky='w')
        time_entry.grid(row=4, column=5, sticky='w')
        c0.grid(row=5, column=4, sticky='w')
        c1.grid(row=6, column=4, sticky='w')
        c2.grid(row=7, column=4, sticky='w')
        c3.grid(row=8, column=4, sticky='w')
        c4.grid(row=9, column=4, sticky='w')
        sub_btn.grid(row=10, column=5)
        quit_button.grid(row=11, column=5)




title_label = tk.Label(root, text='Earthquake Modeling Tools', font=('calibre', 22))
rupture_title = tk.Label(root, text='Rupture Generator', font=('calibre', 18))
rupture_title1 = tk.Label(root, text='-Creates a set of subfaults with individual rupture', font=('calibre', 12))
rupture_title2 = tk.Label(root, text='attributes based on user input.', font=('calibre', 12))
rupture_title3 = tk.Label(root, text='-Visualizes in 2D and 3D', font=('calibre', 12))
rupture_title4 = tk.Label(root, text='-Writes out subfaults attributes in different formats', font=('calibre', 12))
geology_title = tk.Label(root, text='Geology Builder', font=('calibre', 18))
geology_title1 = tk.Label(root, text='-Builds simple geologic structures and assigns', font=('calibre', 12))
geology_title2 = tk.Label(root, text='attributes (e.g seismic velocity, density)', font=('calibre', 12))
geology_title3 = tk.Label(root, text='-User defines structure type (e.g bimaterial fault,', font=('calibre', 12))
geology_title4 = tk.Label(root, text='basin, stratigraphy) and can assign properties', font=('calibre', 12))
seismogram_title = tk.Label(root, text='Seismogram Viewer', font=('calibre', 18))
seismogram_title1 = tk.Label(root, text='-Displays seismograms for different combinations of seismic', font=('calibre', 12))
seismogram_title2 = tk.Label(root, text='sources and recievers', font=('calibre', 12))
seismogram_title3 = tk.Label(root, text='-Source-reciever paths are selected through clickable map', font=('calibre', 12))
seismogram_title4 = tk.Label(root, text='interface', font=('calibre', 12))
seismogram_title5 = tk.Label(root, text='-Computes synthetic-observed waveform performance', font=('calibre', 12))
seismogram_title6 = tk.Label(root, text='metrics', font=('calibre', 12))
continue_btn = tkm.Button(root, text='Start', command=submit, fg='white', background='#0089DB', activebackground='#5EA6F7')
continue_btn1 = tkm.Button(root, text='Start', fg='white', background='#0089DB', activebackground='#5EA6F7')
continue_btn2 = tkm.Button(root, text='Start', fg='white', background='#0089DB', activebackground='#5EA6F7')


image = Image.open('./assets/subfaults_mw4.5.png')
resize_image = image.resize((250, 200))
img = ImageTk.PhotoImage(resize_image)
subfaults_image = ttk.Label(root, image=img)

image1 = Image.open('./assets/hill.png')
resize_image1 = image1.resize((250, 200))
img1 = ImageTk.PhotoImage(resize_image1)
hill_image = ttk.Label(root, image=img1)

image2 = Image.open('./assets/Fig5_Jan2022.png')
resize_image2 = image2.resize((250, 200))
img2 = ImageTk.PhotoImage(resize_image2)
fig_image = ttk.Label(root, image=img2)

title_label.grid(row=0, column=100, sticky='n')
rupture_title.grid(row=1, column=0, sticky='n')
subfaults_image.grid(row=2, column=0, sticky='n')
rupture_title1.grid(row=3, column=0, sticky='w')
rupture_title2.grid(row=4, column=0, sticky='w')
rupture_title3.grid(row=5, column=0, sticky='w')
rupture_title4.grid(row=6, column=0, sticky='w')
geology_title.grid(row=1, column=100)
hill_image.grid(row=2, column=100)
geology_title1.grid(row=3, column=100, sticky='w')
geology_title2.grid(row=4, column=100, sticky='w')
geology_title3.grid(row=5, column=100, sticky='w')
geology_title4.grid(row=6, column=100, sticky='w')
seismogram_title.grid(row=1, column=200, sticky='n')
fig_image.grid(row=2, column=200)
seismogram_title1.grid(row=3, column=200, sticky='w')
seismogram_title2.grid(row=4, column=200, sticky='w')
seismogram_title3.grid(row=5, column=200, sticky='w')
seismogram_title4.grid(row=6, column=200, sticky='w')
seismogram_title5.grid(row=7, column=200, sticky='w')
seismogram_title6.grid(row=8, column=200, sticky='w')
continue_btn.grid(row=10, column=0)
continue_btn1.grid(row=10, column=100)
continue_btn2.grid(row=10, column=200)
# performing an infinite loop
# for the window to display
root.mainloop()




