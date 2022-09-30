import tkinter as tk, tkinter.ttk as ttk
import tkmacosx as tkm
import matplotlib.pyplot as plt
from finiteSource_functions import ellipseSource
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Main(tk.Tk):
    def __init__(self):
        # init a super
        tk.Tk.__init__(self)

        # make notebook fill display
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Notebook
        nb = ttk.Notebook(self)
        nb.grid(row=0, column=0, sticky='nswe')

        # keep a reference to the tabs
        self.rupture = Rupture(self)
        self.geology = Geology(self)
        self.seismogram = Seismogram(self)

        # tabs
        nb.add(self.rupture, text="Rupture Generator")
        nb.add(self.geology, text="Geology Builder")
        nb.add(self.seismogram, text="Seismogram Builder")

class Rupture(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
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

        # scenario = scenario_name.get()
        # Mw = earthquake_mag.get()
        #
        # rupture = fault_rupture.get()
        # strike = strike_degrees.get()
        # dip = dip_degrees.get()
        # rake = rake_degrees.get()
        # centroidX = centroid_x.get()
        # centroidY = centroid_y.get()
        # centroidZ = centroid_z.get()
        # area = rupture_area.get()
        # aspectRatio = aspect_ratio.get()
        #
        # hypoX = hypocenter_x.get()
        # hypoY = hypocenter_y.get()
        # hypoZ = hypocenter_z.get()
        # vrup = rupture_velocity.get()
        # time = source_time.get()
        # bool0 = boolean0.get()
        # bool1 = boolean1.get()
        # bool2 = boolean2.get()
        # bool3 = boolean3.get()
        # bool4 = boolean4.get()
        # fileTXT = filenameTXT.get()
        # fileSW4 = filenameSW4.get()
        #
        # ellipseSource(Mw, strike, dip, rake, centroidX, centroidY, centroidZ, aspectRatio, hypoX, hypoY, hypoZ, vrup,
        #               bool1, bool2, bool3, bool4, fileTXT, fileSW4)

        # label, entry, menu ( first column )
        # creating a label for fault name
        self.scenario_label = tk.Label(self, text='Scenario Name', font=('calibre', 10, 'bold'))
        # creating a entry for fault name
        self.scenario_entry = tk.Entry(self, textvariable=scenario_name, font=('calibre', 10, 'normal'))
        # creating a label for
        # earthquake mag using widget Label
        self.earthquake_label = tk.Label(self, text='Earthquake Magnitude', font=('calibre', 10, 'bold'))
        # creating a entry for input
        # earthquake mag using widget Entry
        self.earthquake_entry = tk.Entry(self, textvariable=earthquake_mag, font=('calibre', 10, 'normal'))
        # creating a label for seismic moment type
        # seismic_label = tk.Label(root, text='Seismic Moment', font=('calibre', 10, 'bold'))
        # # creating an entry for seismic moment type
        # seismic_entry = tk.Entry(root, textvariable=seismic_moment, font=('calibre', 10, 'normal'))

        # second column
        # creating a label for fault rupture type
        self.rupture_label = tk.Label(self, text='Fault Rupture Type', font=('calibre', 10, 'bold'))
        # creating menu for fault rupture type
        self.rupture_entry = tk.OptionMenu(self, fault_rupture, *RuptureList)
        self.strike_label = tk.Label(self, text='Strike (degrees)', font=('calibre', 10, 'bold'))
        self.strike_entry = tk.Entry(self, textvariable=strike_degrees, font=('calibre', 10, 'normal'))
        self.dip_label = tk.Label(self, text='Dip (degrees)', font=('calibre', 10, 'bold'))
        self.dip_entry = tk.Entry(self, textvariable=dip_degrees, font=('calibre', 10, 'normal'))
        self.rake_label = tk.Label(self, text='Rake (degrees)', font=('calibre', 10, 'bold'))
        self.rake_entry = tk.Entry(self, textvariable=rake_degrees, font=('calibre', 10, 'normal'))
        self.slipX_label = tk.Label(self, text='Slip Centroid, X', font=('calibre', 10, 'bold'))
        self.slipX_entry = tk.Entry(self, textvariable=centroid_x, font=('calibre', 10, 'normal'))
        self.slipY_label = tk.Label(self, text='Slip Centroid, Y', font=('calibre', 10, 'bold'))
        self.slipY_entry = tk.Entry(self, textvariable=centroid_y, font=('calibre', 10, 'normal'))
        self.slipZ_label = tk.Label(self, text='Slip Centroid, Z', font=('calibre', 10, 'bold'))
        self.slipZ_entry = tk.Entry(self, textvariable=centroid_z, font=('calibre', 10, 'normal'))
        self.area_label = tk.Label(self, text='Rupture Area Shape', font=('calibre', 10, 'bold'))
        self.area_entry = tk.OptionMenu(self, rupture_area, *ShapeList)
        self.ratio_label = tk.Label(self, text='Aspect ratio', font=('calibre', 10, 'bold'))
        self.ratio_entry = tk.Entry(self, textvariable=aspect_ratio, font=('calibre', 10, 'normal'))

        # third column
        self.hypocenterX_label = tk.Label(self, text='Hypocenter Location, X', font=('calibre', 10, 'bold'))
        self.hypocenterX_entry = tk.Entry(self, textvariable=hypocenter_x, font=('calibre', 10, 'normal'))
        self.hypocenterY_label = tk.Label(self, text='Hypocenter Location, Y', font=('calibre', 10, 'bold'))
        self.hypocenterY_entry = tk.Entry(self, textvariable=hypocenter_y, font=('calibre', 10, 'normal'))
        self.hypocenterZ_label = tk.Label(self, text='Hypocenter Location, Z', font=('calibre', 10, 'bold'))
        self.hypocenterZ_entry = tk.Entry(self, textvariable=hypocenter_z, font=('calibre', 10, 'normal'))
        self.velocity_label = tk.Label(self, text='Rupture Velocity (m/s)', font=('calibre', 10, 'bold'))
        self.velocity_entry = tk.Entry(self, textvariable=rupture_velocity, font=('calibre', 10, 'normal'))
        self.time_label = tk.Label(self, text='Source Time Function', font=('calibre', 10, 'bold'))
        self.time_entry = tk.OptionMenu(self, source_time, *SourceList)
        self.filenameTXT_entry = tk.Entry(self, textvariable=filenameTXT, font=('calibre', 10, 'normal'))
        self.filenameSW4_entry = tk.Entry(self, textvariable=filenameSW4, font=('calibre', 10, 'normal'))
        self.c0 = tk.Checkbutton(self, text='Show Report', variable=boolean0, onvalue=1, offvalue=0)
        self.c1 = tk.Checkbutton(self, text='Visualize 2D', variable=boolean1, onvalue=1, offvalue=0)
        self.c2 = tk.Checkbutton(self, text='Visualize 3D', variable=boolean2, onvalue=1, offvalue=0)
        self.c3 = tk.Checkbutton(self, text='Save File (Ascii List)', variable=boolean3, onvalue=1, offvalue=0)
        self.c4 = tk.Checkbutton(self, text='Save File (SW4 format)', variable=boolean4, onvalue=1, offvalue=0)

        # ( grid for first column)
        self.scenario_label.grid(row=0, column=0, sticky='w')
        self.scenario_entry.grid(row=0, column=1, sticky='w')
        self.earthquake_label.grid(row=1, column=0, sticky='w')
        self.earthquake_entry.grid(row=1, column=1, sticky='w')
        # seismic_label.grid(row=2, column=0)
        # seismic_entry.grid(row=2, column=1)

        # grid for second column
        self.rupture_label.grid(row=0, column=2, sticky='w')
        self.rupture_entry.grid(row=0, column=3, sticky='w')
        self.strike_label.grid(row=1, column=2, sticky='w')
        self.strike_entry.grid(row=1, column=3, sticky='w')
        self.dip_label.grid(row=2, column=2, sticky='w')
        self.dip_entry.grid(row=2, column=3, sticky='w')
        self.rake_label.grid(row=3, column=2, sticky='w')
        self.rake_entry.grid(row=3, column=3, sticky='w')
        self.slipX_label.grid(row=4, column=2, sticky='w')
        self.slipX_entry.grid(row=4, column=3, sticky='w')
        self.slipY_label.grid(row=5, column=2, sticky='w')
        self.slipY_entry.grid(row=5, column=3, sticky='w')
        self.slipZ_label.grid(row=6, column=2, sticky='w')
        self.slipZ_entry.grid(row=6, column=3, sticky='w')
        self.area_label.grid(row=7, column=2, sticky='w')
        self.area_entry.grid(row=7, column=3, sticky='w')
        self.ratio_label.grid(row=8, column=2, sticky='w')
        self.ratio_entry.grid(row=8, column=3, sticky='w')

        # grid for third column
        self.hypocenterX_label.grid(row=0, column=4, sticky='w')
        self.hypocenterX_entry.grid(row=0, column=5, sticky='w')
        self.hypocenterY_label.grid(row=1, column=4, sticky='w')
        self.hypocenterY_entry.grid(row=1, column=5, sticky='w')
        self.hypocenterZ_label.grid(row=2, column=4, sticky='w')
        self.hypocenterZ_entry.grid(row=2, column=5, sticky='w')
        self.velocity_label.grid(row=3, column=4, sticky='w')
        self.velocity_entry.grid(row=3, column=5, sticky='w')
        self.time_label.grid(row=4, column=4, sticky='w')
        self.time_entry.grid(row=4, column=5, sticky='w')
        self.c0.grid(row=5, column=4, sticky='w')
        self.c1.grid(row=6, column=4, sticky='w')
        self.c2.grid(row=7, column=4, sticky='w')
        self.c3.grid(row=8, column=4, sticky='w')
        self.c4.grid(row=9, column=4, sticky='w')
        self.filenameTXT_entry.grid(row=8, column=5)
        self.filenameSW4_entry.grid(row=9, column=5)
        self.start_button = tkm.Button(self, text="Submit", fg='white', background='#0089DB',
                                       activebackground='#5EA6F7',
                                       command=lambda: setup_rupture()).grid(row=10, column=5)

    # def setup_rupture(self):
    #     scenario = scenario_name.get()
    #     Mw = earthquake_mag.get()
    #
    #     rupture = fault_rupture.get()
    #     strike = strike_degrees.get()
    #     dip = dip_degrees.get()
    #     rake = rake_degrees.get()
    #     centroidX = centroid_x.get()
    #     centroidY = centroid_y.get()
    #     centroidZ = centroid_z.get()
    #     area = rupture_area.get()
    #     aspectRatio = aspect_ratio.get()
    #
    #     hypoX = hypocenter_x.get()
    #     hypoY = hypocenter_y.get()
    #     hypoZ = hypocenter_z.get()
    #     vrup = rupture_velocity.get()
    #     time = source_time.get()
    #     bool0 = boolean0.get()
    #     bool1 = boolean1.get()
    #     bool2 = boolean2.get()
    #     bool3 = boolean3.get()
    #     bool4 = boolean4.get()
    #     fileTXT = filenameTXT.get()
    #     fileSW4 = filenameSW4.get()
    #
    #     ellipseSource(Mw, strike, dip, rake, centroidX, centroidY, centroidZ, aspectRatio, hypoX, hypoY, hypoZ, vrup,
    #                   bool1, bool2, bool3, bool4, fileTXT, fileSW4)


class Geology(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.geology_label = tk.Label(self, text='Coming Soon')
        self.geology_label.grid(row=0, column=1)


class Seismogram(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.seismogram_label = tk.Label(self, text='Coming Soon')
        self.seismogram_label.grid(row=0, column=1)


if __name__ == "__main__":
    root = Main()
    root.geometry('950x600')
    root.title("Tab Version")
    root.mainloop()



