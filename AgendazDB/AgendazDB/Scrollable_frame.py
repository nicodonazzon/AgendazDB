import tkinter as tk
from tkinter import ttk

class Scrollable(tk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame, 
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16, height=500):

        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        scrollbar2 = tk.Scrollbar(frame, width=width,orient='horizontal')
        scrollbar2.pack(side=tk.BOTTOM, fill=tk.X, expand=False)

        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar2.set, height=height)
        self.canvas.pack(side=tk.LEFT, expand=True)

        scrollbar2.config(command=self.canvas.xview)
        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame)         

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)


    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)        

    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))


