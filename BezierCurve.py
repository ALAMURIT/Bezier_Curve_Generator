#alamurit
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
app = Tk()

#appProperties
app.title('Bezier Curve Generator')
app.geometry('720x360')

#printCoordinates function
def printCoordinates():
    print(coordinate_A_x.get(), coordinate_A_y.get(), '\n', coordinate_B_x.get(), coordinate_B_y.get(), '\n', coordinate_C_x.get(), coordinate_C_y.get())

#plot function
def plotCurve():
    #fig = Figure(figsize = (5,5), dpi = 100)
    X=[]
    Y=[]
    x1=coordinate_A_x.get()
    x2=coordinate_B_x.get()
    x3=coordinate_C_x.get()
    y1=coordinate_A_y.get()
    y2=coordinate_B_y.get()
    y3=coordinate_C_x.get()
    
    #refinement number
    n=100

    for i in range(1,n,1):
        t=i/n
        xC = (((1-t)**2)*x1)+(2*(1-t)*t*x2)+((t**2)*x3)
        yC = (((1-t)**2)*y1)+(2*(1-t)*t*y2)+((t**2)*y3)
        X.append(xC)
        Y.append(yC)
        fig = plt.figure(figsize=(5,5), dpi=50)
        plt.plot(X,Y)
        #fig.plt.plot(X,Y)
        #fig.plot(X,Y)
        canvas = FigureCanvasTkAgg(fig, master = app)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, column=0)
        plt.close()
        #plt.show()

#coordinate_A
coordinate_A_x = IntVar()
coordinate_A_y = IntVar()
coordinate_A_label = Label(app, text='Enter coordinates for point A', font=( 14))
coordinate_A_label.grid(row=0, column=0, sticky=W)

#X_coordinate_for_A
coordinate_A_entry_x = Entry(app, textvariable=coordinate_A_x)
coordinate_A_entry_x.grid(row=0, column=1)

#Y_coordinate_for_A
coordinate_A_entry_y = Entry(app, textvariable=coordinate_A_y)
coordinate_A_entry_y.grid(row=0, column=2)

#coordinate_B
coordinate_B_x = IntVar()
coordinate_B_y = IntVar()
coordinate_B_label = Label(app, text='Enter coordinates for point B', font=( 14))
coordinate_B_label.grid(row=1, column=0, sticky=W)

#X_coordinate_for_B
coordinate_B_entry_x = Entry(app, textvariable=coordinate_B_x)
coordinate_B_entry_x.grid(row=1, column=1)

#Y_coordinate_for_B
coordinate_B_entry_y = Entry(app, textvariable=coordinate_B_y)
coordinate_B_entry_y.grid(row=1, column=2)

#coordinate_C
coordinate_C_x = IntVar()
coordinate_C_y = IntVar()
coordinate_C_label = Label(app, text='Enter coordinates for point C', font=( 14))
coordinate_C_label.grid(row=2, column=0, sticky=W)

#X_coordinate_for_C
coordinate_C_entry_x = Entry(app, textvariable=coordinate_C_x)
coordinate_C_entry_x.grid(row=2, column=1)

#Y_coordinate_for_C
coordinate_C_entry_y = Entry(app, textvariable=coordinate_C_y)
coordinate_C_entry_y.grid(row=2, column=2)

#buttons

#print A coordinates button
print_A_btn = Button(app, text='Print coordinates', width=18, height=2, command=printCoordinates)
print_A_btn.grid(row=3, column=0)

#plot button
plot_graph_btn = Button(app, text='Plot Curve', width=18, height=2, command=plotCurve)
plot_graph_btn.grid(row=3, column=1)

#mainLoop
app.mainloop()
