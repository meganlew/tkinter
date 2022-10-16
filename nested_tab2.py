import tkinter as tk, tkinter.ttk as ttk

root = tk.Tk()
root.geometry("1000x900")

status = tk.Frame(root)

left_tabs = ttk.Notebook(status)
tab_a = tk.Frame(left_tabs)
tab_b = tk.Frame(left_tabs)
left_tabs.add(tab_a, text="layered model")
left_tabs.add(tab_b, text="basin model")
left_tabs.grid(row=0, column=0, sticky="nsew")

right_tabs = ttk.Notebook(status)
tab_c = tk.Frame(right_tabs)
tab_d = tk.Frame(right_tabs)
tab_e = tk.Frame(right_tabs)
right_tabs.add(tab_c, text="Rupture Generator")
right_tabs.add(tab_d, text="Geology Builder")
right_tabs.add(tab_e, text="Seismogram Builder")
left_tabs.grid(row=0, column=0, sticky="nsew")
right_tabs.grid(row=0, column=1, sticky="nsew")

tk.Label(tab_a, text="text").pack()
tk.Label(tab_c, text="text").pack()

status.columnconfigure(0, weight=1, uniform="x")
status.columnconfigure(1, weight=1, uniform="x")
status.pack(fill=tk.X)

tk.mainloop()