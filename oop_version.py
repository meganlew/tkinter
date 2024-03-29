import tkinter as tk
from tkinter import ttk, messagebox
import tkmacosx as tkm
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from finiteSource_functions import ellipseSource
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

class Win:
    def __init__(self, root):
        """Define window for the app"""
        self.root = root
        self.root.geometry("950x600")
        self.root.title("Welcome")
        title_label = tk.Label(self.root, text='Earthquake Modeling Tools', font=('calibre', 22))
        rupture_title = tk.Label(self.root, text='Rupture Generator', font=('calibre', 18))
        rupture_title1 = tk.Label(self.root, text='-Creates a set of subfaults with individual rupture', font=('calibre', 12))
        rupture_title2 = tk.Label(self.root, text='attributes based on user input.', font=('calibre', 12))
        rupture_title3 = tk.Label(self.root, text='-Visualizes in 2D and 3D', font=('calibre', 12))
        rupture_title4 = tk.Label(self.root, text='-Writes out subfaults attributes in different formats', font=('calibre', 12))
        geology_title = tk.Label(self.root, text='Geology Builder', font=('calibre', 18))
        geology_title1 = tk.Label(self.root, text='-Builds simple geologic structures and assigns', font=('calibre', 12))
        geology_title2 = tk.Label(self.root, text='attributes (e.g seismic velocity, density)', font=('calibre', 12))
        geology_title3 = tk.Label(self.root, text='-User defines structure type (e.g bimaterial fault,', font=('calibre', 12))
        geology_title4 = tk.Label(self.root, text='basin, stratigraphy) and can assign properties', font=('calibre', 12))
        seismogram_title = tk.Label(self.root, text='Seismogram Viewer', font=('calibre', 18))
        seismogram_title1 = tk.Label(self.root, text='-Displays seismograms for different combinations of seismic', font=('calibre', 12))
        seismogram_title2 = tk.Label(self.root, text='sources and recievers', font=('calibre', 12))
        seismogram_title3 = tk.Label(self.root, text='-Source-reciever paths are selected through clickable map', font=('calibre', 12))
        seismogram_title4 = tk.Label(self.root, text='interface', font=('calibre', 12))
        seismogram_title5 = tk.Label(self.root, text='-Computes synthetic-observed waveform performance', font=('calibre', 12))
        seismogram_title6 = tk.Label(self.root, text='metrics', font=('calibre', 12))

        self.image = Image.open('./assets/subfaults_mw4.5.png')
        self.resize_image = self.image.resize((250, 200))
        self.img = ImageTk.PhotoImage(self.resize_image)
        subfaults_image = ttk.Label(self.root, image=self.img)


        self.image1 = Image.open('./assets/hill.png')
        self.resize_image1 = self.image1.resize((250, 200))
        self.img1 = ImageTk.PhotoImage(self.resize_image1)
        hill_image = ttk.Label(self.root, image=self.img1)

        self.image2 = Image.open('./assets/Fig5_Jan2022.png')
        self.resize_image2 = self.image2.resize((250, 200))
        self.img2 = ImageTk.PhotoImage(self.resize_image2)
        fig_image = ttk.Label(self.root, image=self.img2)

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
        self.start_button = tkm.Button(self.root, text="Start",fg='white', background='#0089DB', activebackground='#5EA6F7',
                                       command=lambda: self.new_window(Win2)).grid(row=10, column=0)
        self.start_button1 = tkm.Button(self.root, text="Start", fg='white', background='#0089DB',
                                       activebackground='#5EA6F7',
                                       command=lambda: self.new_window(Win3)).grid(row=10, column=100)
        self.start_button2 = tkm.Button(self.root, text="Start", fg='white', background='#0089DB',
                                       activebackground='#5EA6F7',
                                       command=lambda: self.new_window(Win4)).grid(row=10, column=200)
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

    def on_exit(self):
        """When you click to exit, this function is called"""
        if messagebox.askyesno("Exit", "Do you want to quit the Welcome window?"):
            self.root.quit()

    def new_window(self, _class):
        try:
            if self.new.state() == "normal":
                self.new.focus()
        except:
            self.new = tk.Toplevel(self.root)
            _class(self.new)


class Win2:
    def __init__(self, root):
        print(app.new.state())
        self.root = root
        self.root.geometry("900x400")
        self.root.title("Rupture Generator")

        scenario_name.set("")
        earthquake_mag.set(4.5)
        fault_rupture.set("")
        # seismic_moment.set(1.2)
        strike_degrees.set(0.0)
        dip_degrees.set(90.0)
        rake_degrees.set(180.0)
        aspect_ratio.set(1.0)
        centroid_z.set(-10000.0)
        hypocenter_z.set(-10000.0)
        rupture_velocity.set(2500.0)

        # label, entry, menu ( first column )
        # creating a label for fault name
        scenario_label = tk.Label(self.root, text='Scenario Name', font=('calibre', 10, 'bold'))
        # creating a entry for fault name
        scenario_entry = tk.Entry(self.root, textvariable=scenario_name, font=('calibre', 10, 'normal'))
        # creating a label for
        # earthquake mag using widget Label
        earthquake_label = tk.Label(self.root, text='Earthquake Magnitude', font=('calibre', 10, 'bold'))
        # creating a entry for input
        # earthquake mag using widget Entry
        earthquake_entry = tk.Entry(self.root, textvariable=earthquake_mag, font=('calibre', 10, 'normal'))
        # creating a label for seismic moment type
        # seismic_label = tk.Label(root, text='Seismic Moment', font=('calibre', 10, 'bold'))
        # # creating an entry for seismic moment type
        # seismic_entry = tk.Entry(root, textvariable=seismic_moment, font=('calibre', 10, 'normal'))

        # second column
        # creating a label for fault rupture type
        rupture_label = tk.Label(self.root, text='Fault Rupture Type', font=('calibre', 10, 'bold'))
        # creating menu for fault rupture type
        rupture_entry = tk.OptionMenu(self.root, fault_rupture, *RuptureList)
        strike_label = tk.Label(self.root, text='Strike (degrees)', font=('calibre', 10, 'bold'))
        strike_entry = tk.Entry(self.root, textvariable=strike_degrees, font=('calibre', 10, 'normal'))
        dip_label = tk.Label(self.root, text='Dip (degrees)', font=('calibre', 10, 'bold'))
        dip_entry = tk.Entry(self.root, textvariable=dip_degrees, font=('calibre', 10, 'normal'))
        rake_label = tk.Label(self.root, text='Rake (degrees)', font=('calibre', 10, 'bold'))
        rake_entry = tk.Entry(self.root, textvariable=rake_degrees, font=('calibre', 10, 'normal'))
        slipX_label = tk.Label(self.root, text='Slip Centroid, X', font=('calibre', 10, 'bold'))
        slipX_entry = tk.Entry(self.root, textvariable=centroid_x, font=('calibre', 10, 'normal'))
        slipY_label = tk.Label(self.root, text='Slip Centroid, Y', font=('calibre', 10, 'bold'))
        slipY_entry = tk.Entry(self.root, textvariable=centroid_y, font=('calibre', 10, 'normal'))
        slipZ_label = tk.Label(self.root, text='Slip Centroid, Z', font=('calibre', 10, 'bold'))
        slipZ_entry = tk.Entry(self.root, textvariable=centroid_z, font=('calibre', 10, 'normal'))
        area_label = tk.Label(self.root, text='Rupture Area Shape', font=('calibre', 10, 'bold'))
        area_entry = tk.OptionMenu(self.root, rupture_area, *ShapeList)
        ratio_label = tk.Label(self.root, text='Aspect ratio', font=('calibre', 10, 'bold'))
        ratio_entry = tk.Entry(self.root, textvariable=aspect_ratio, font=('calibre', 10, 'normal'))

        # third column
        hypocenterX_label = tk.Label(self.root, text='Hypocenter Location, X', font=('calibre', 10, 'bold'))
        hypocenterX_entry = tk.Entry(self.root, textvariable=hypocenter_x, font=('calibre', 10, 'normal'))
        hypocenterY_label = tk.Label(self.root, text='Hypocenter Location, Y', font=('calibre', 10, 'bold'))
        hypocenterY_entry = tk.Entry(self.root, textvariable=hypocenter_y, font=('calibre', 10, 'normal'))
        hypocenterZ_label = tk.Label(self.root, text='Hypocenter Location, Z', font=('calibre', 10, 'bold'))
        hypocenterZ_entry = tk.Entry(self.root, textvariable=hypocenter_z, font=('calibre', 10, 'normal'))
        velocity_label = tk.Label(self.root, text='Rupture Velocity (m/s)', font=('calibre', 10, 'bold'))
        velocity_entry = tk.Entry(self.root, textvariable=rupture_velocity, font=('calibre', 10, 'normal'))
        time_label = tk.Label(self.root, text='Source Time Function', font=('calibre', 10, 'bold'))
        time_entry = tk.OptionMenu(self.root, source_time, *SourceList)
        filenameTXT_entry = tk.Entry(self.root, textvariable=filenameTXT, font=('calibre', 10, 'normal'))
        filenameSW4_entry = tk.Entry(self.root, textvariable=filenameSW4, font=('calibre', 10, 'normal'))
        c0 = tk.Checkbutton(self.root, text='Show Report', variable=boolean0, onvalue=1, offvalue=0)
        c1 = tk.Checkbutton(self.root, text='Visualize 2D', variable=boolean1, onvalue=1, offvalue=0)
        c2 = tk.Checkbutton(self.root, text='Visualize 3D', variable=boolean2, onvalue=1, offvalue=0)
        c3 = tk.Checkbutton(self.root, text='Save File (Ascii List)', variable=boolean3, onvalue=1, offvalue=0)
        c4 = tk.Checkbutton(self.root, text='Save File (SW4 format)', variable=boolean4, onvalue=1, offvalue=0)

        # ( grid for first column)
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
        filenameTXT_entry.grid(row=8, column=5)
        filenameSW4_entry.grid(row=9, column=5)

        self.start_button = tkm.Button(self.root, text="Submit", fg='white', background='#0089DB',
                                       activebackground='#5EA6F7',
                                       command=lambda: setup_rupture()).grid(row=10, column=5)

    def new_window1(self, _class):
        try:
            if self.new.state() == "normal":
                self.new.focus()
        except:
            self.new = tk.Toplevel(self.root)
            _class(self.new)


def setup_rupture():
        scenario = scenario_name.get()
        Mw = earthquake_mag.get()

        rupture = fault_rupture.get()
        strike = strike_degrees.get()
        dip = dip_degrees.get()
        rake = rake_degrees.get()
        centroidX = centroid_x.get()
        centroidY = centroid_y.get()
        centroidZ = centroid_z.get()
        area = rupture_area.get()
        aspectRatio = aspect_ratio.get()

        hypoX = hypocenter_x.get()
        hypoY = hypocenter_y.get()
        hypoZ = hypocenter_z.get()
        vrup = rupture_velocity.get()
        time = source_time.get()
        bool0 = boolean0.get()
        bool1 = boolean1.get()
        bool2 = boolean2.get()
        bool3 = boolean3.get()
        bool4 = boolean4.get()
        fileTXT = filenameTXT.get()
        fileSW4 = filenameSW4.get()

        ellipseSource(Mw, strike, dip, rake, centroidX, centroidY, centroidZ, aspectRatio, hypoX, hypoY, hypoZ, vrup,
                      bool1, bool2, bool3, bool4, fileTXT, fileSW4)

        if bool0:
            window = tk.Toplevel(root)
            window.geometry("2000x2000")
            window.title("Rupture Generator Results")
            canvas = FigureCanvasTkAgg(fig, master=window)
            plot_widget = canvas.get_tk_widget()
            plot_widget.grid(row=9, column=7)
            # plot_widget.figure(figsize=(1, 1))
            # fig = Figure(dpi=50)

            # frame2 = tk.Frame(window)
            # canvas2 = FigureCanvasTkAgg(fig, master=window)
            # plot_widget2 = canvas2.get_tk_widget()
            # plot_widget2.grid(row=8, column=7)

            toolbarFrame = tk.Frame(master=window)
            toolbarFrame.grid(row=10, column=7)
            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

            # labels for first column
            scenario_text = tk.Label(window, text='Scenario Name', font=('calibre', 12, 'bold'), anchor='w')
            text_scenario = tk.Label(window, text=scenario, font=('calibre', 12), anchor='w')
            earthquake_text = tk.Label(window, text='Earthquake Magnitude', font=('calibre', 12, 'bold'))
            text_earthquake = tk.Label(window, text=Mw, font=('calibre', 12))
            # seismic_text = tk.Label(window, text='Seismic Moment', font=('calibre', 12, 'bold'))
            # text_seismic = tk.Label(window, text=M0, font=('calibre', 12))
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
            text_slipX = tk.Label(window, text=centroidX, font=('calibre', 12))
            slipY_text = tk.Label(window, text='Slip Centroid, Y', font=('calibre', 12, 'bold'))
            text_slipY = tk.Label(window, text=centroidY, font=('calibre', 12))
            slipZ_text = tk.Label(window, text='Slip Centroid, X', font=('calibre', 12, 'bold'))
            text_slipZ = tk.Label(window, text=centroidZ, font=('calibre', 12))
            area_text = tk.Label(window, text='Rupture Area Shape', font=('calibre', 12, 'bold'))
            text_area = tk.Label(window, text=area, font=('calibre', 12))
            ratio_text = tk.Label(window, text='Rupture Area Shape', font=('calibre', 12, 'bold'))
            text_ratio = tk.Label(window, text=aspectRatio, font=('calibre', 12))
            # labels for third column
            hypocenterX_text = tk.Label(window, text='Hypocenter location, X', font=('calibre', 12, 'bold'))
            text_hypocenterX = tk.Label(window, text=hypoX, font=('calibre', 12))
            hypocenterY_text = tk.Label(window, text='Hypocenter location, Y', font=('calibre', 12, 'bold'))
            text_hypocenterY = tk.Label(window, text=hypoY, font=('calibre', 12))
            hypocenterZ_text = tk.Label(window, text='Hypocenter location, Z', font=('calibre', 12, 'bold'))
            text_hypocenterZ = tk.Label(window, text=hypoZ, font=('calibre', 12))
            velocity_text = tk.Label(window, text='Rupture Velocity (m/s)', font=('calibre', 12, 'bold'))
            text_velocity = tk.Label(window, text=vrup, font=('calibre', 12))
            time_text = tk.Label(window, text='Source Time Function', font=('calibre', 12, 'bold'))
            text_time = tk.Label(window, text=time, font=('calibre', 12))

            # grid to display first column of inputs received from user
            scenario_text.grid(row=0, column=0)
            text_scenario.grid(row=0, column=1)
            earthquake_text.grid(row=1, column=0)
            text_earthquake.grid(row=1, column=1)
            # seismic_text.grid(row=2, column=0)
            # text_seismic.grid(row=2, column=1)
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

# geology builder
class Win3():
    def __init__(self, root):
        print(app.new.state())
        self.root = root
        self.root.geometry("900x400")
        self.root.title("Geology Builder")
        text_label = tk.Label(self.root, text='Coming Soon', font=('calibre', 20, 'bold'))
        text_label.grid(row=0, column=1)

# seismogram viewer
class Win4():
    def __init__(self, root):
        print(app.new.state())
        self.root = root
        self.root.geometry("900x400")
        self.root.title("Seismogram Viewer")
        text_label = tk.Label(self.root, text='Coming Soon', font=('calibre', 20, 'bold'))
        text_label.grid(row=0, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Win(root)
    # fig = Figure(dpi=50)
    fig, ax = plt.subplots()
    # fig, axs = plt.subplots(2)


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
    filenameTXT = tk.StringVar()
    filenameTXT.set("subfaults.txt")
    filenameSW4 = tk.StringVar()
    filenameSW4.set("subfaults.sw4in")
    boolean0 = tk.BooleanVar()
    boolean1 = tk.BooleanVar()
    boolean2 = tk.BooleanVar()
    boolean3 = tk.BooleanVar()
    boolean4 = tk.BooleanVar()

    # set default as first index in the list
    fault_rupture.set(RuptureList[0])
    rupture_area.set(ShapeList[0])
    source_time.set(SourceList[0])

    root.mainloop()

