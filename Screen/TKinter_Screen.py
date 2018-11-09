import tkinter
import os

mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry("640x480+300+300")
mainwindow['padx'] = 10

label = tkinter.Label(mainwindow, text="Tkinter Grid Demo")
label.grid(row=0,column=0,columnspan=3)

mainwindow.columnconfigure(0,weight=1)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2,weight=3)
mainwindow.columnconfigure(3,weight=1)
mainwindow.columnconfigure(4,weight=1)

mainwindow.rowconfigure(0,weight=1)
mainwindow.rowconfigure(1,weight=1)
mainwindow.rowconfigure(2,weight=1)
mainwindow.rowconfigure(3,weight=1)
mainwindow.rowconfigure(4,weight=1)

# Listbox on the left of main window
filelist = tkinter.Listbox(mainwindow)
filelist.grid(row=1,column=0,rowspan=2,sticky='nsew')
filelist.config(border=2,relief='sunken')
# populate the listbox with filelist from system32 folder
for zone in os.listdir('/Windows/System32'):
    filelist.insert(tkinter.END, zone)

# Add Scroll bar and connect that to the listbox
listscroll = tkinter.Scrollbar(mainwindow,orient=tkinter.VERTICAL,command=filelist.yview)
listscroll.grid(row=1,column=1,rowspan=2,sticky='nsw')
filelist['yscrollcommand']=listscroll.set

# Add Frame for Radio buttons
optionFrame = tkinter.LabelFrame(mainwindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

# Add Radio buttons within Option Frame
rbValue = tkinter.IntVar() #Radio button value can have only one value
rbValue.set(1) # set default value selected in radio button
# Add Radio buttons and map that to Radio button value above
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
# position Radio button within option frame by Grid
radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')
radio3.grid(row=2,column=0,sticky='w')

# Result Frame
resultFrame = tkinter.Frame(mainwindow)
resultFrame.grid(row=2,column=2,sticky='sew')
# Add Result label and Entry window
# resultLabel = tkinter.Label(mainwindow, text='Result')
# resultLabel.grid(row=2, column=2, sticky='nw')
# result = tkinter.Entry(mainwindow)
# result.grid(row=2, column=2, sticky='sw')

resultLabel = tkinter.Label(resultFrame, text='Result')
resultLabel.grid(row=0, column=0, sticky='w')
result = tkinter.Entry(resultFrame)
result.grid(row=1, column=0, sticky='w')

# Frame for time spinners
timeFrame = tkinter.LabelFrame(mainwindow,text='Time')
timeFrame.grid(row=3,column=0,sticky='new')
# Time Spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,60)))
secondSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,60)))
# Place Time Spinners within timeFrame
hourSpinner.grid(row=0,column=0)
tkinter.Label(timeFrame,text=':').grid(row=0,column=1)
minuteSpinner.grid(row=0,column=2)
tkinter.Label(timeFrame,text=':').grid(row=0,column=3)
secondSpinner.grid(row=0,column=4)
# Move timeFrame 36 places to right to center time spinners within it
timeFrame['padx'] = 36

# Frame for Date spinners
dateFrame = tkinter.Frame(mainwindow)
dateFrame.grid(row=4,column=0,sticky='new')
# Date Labels
dayLabel = tkinter.Label(dateFrame,text='Day')
monthLabel = tkinter.Label(dateFrame,text='Month')
yearLabel = tkinter.Label(dateFrame,text='Year')
# Place Date Labels within dateFrame
dayLabel.grid(row=0,column=0,sticky='w')
monthLabel.grid(row=0,column=1,sticky='w')
yearLabel.grid(row=0,column=2,sticky='w')
# Date Spinners
daySpinner = tkinter.Spinbox(dateFrame,width=2,from_=1,to=31)
monthSpinner = tkinter.Spinbox(dateFrame,width=3,values=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
yearSpinner = tkinter.Spinbox(dateFrame,width=4,from_=2000,to=2099)
# Place Date Spinners within dateFrame
daySpinner.grid(row=1,column=0)
monthSpinner.grid(row=1,column=1)
yearSpinner.grid(row=1,column=2)

# Add OK and Cancel Buttons
okButton = tkinter.Button(mainwindow,text='OK')
cancelButton = tkinter.Button(mainwindow,text='Cancel',command=mainwindow.quit)
okButton.grid(row=4,column=3,sticky='e')
cancelButton.grid(row=4,column=4,sticky='w')

mainwindow.mainloop()

print('Radion button value is {}'.format(rbValue.get()))
# print('Result from textbox is {}'.format(result.get()))

# print(result.pack)
