import tkinter as tk
from tkinter import ttk
#Make the root widget
root = tk.Tk()

#Make the first notebook
tab = ttk.Notebook(root) #Create the notebook
tab.pack()

rupture = 'Rupture Generator' #concatenate term name
ruptureFrame = ttk.Frame(tab)   #create frame widget to go in program nb
tab.add(ruptureFrame, text=rupture)# add the newly created frame widget to the notebook


geology = 'Geology Builder' #concatenate term name
geologyFrame = ttk.Frame(tab)   #create frame widget to go in program nb
tab.add(geologyFrame, text=geology)# add the newly created frame widget to the notebook


seismogram = 'Seismogram Builder' #concatenate term name
seismogramFrame = ttk.Frame(tab)   #create frame widget to go in program nb
tab.add(seismogramFrame, text=seismogram)# add the newly created frame widget to the notebook

nbName = ttk.Notebook(geologyFrame)#Create the notebooks to go in each of the geology frames
nbName.pack()#pack the notebook


layeredModel = "Layered Model"#concatenate name
layered = ttk.Frame(nbName) #Create a  frame for the newly created term frame
nbName.add(layered, text=layeredModel)#add the frame to the new notebook

basinModel = "Basin Model"  # concatenate name
basin = ttk.Frame(nbName)  # Create a frame for the newly created term frame
nbName.add(basin, text=basinModel)  # add the frame to the new notebook

root.mainloop()

