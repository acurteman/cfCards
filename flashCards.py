from tkinter import *

root = Tk()

# Creating frame for all entry fields and buttons
entryFrame = Frame(root, width=500, height=300)

setName = NONE

# Creating all entry widgets
wordLabel = Label(entryFrame, text="Word:")
defLabel = Label(entryFrame, text='Definition:')
curSetLabel = Label(entryFrame, text='Current Set: ')
curSetNameLabel = Label(entryFrame, text=setName)
wordEntry = Entry(entryFrame)
defEntry = Entry(entryFrame)
addEntryButton = Button(entryFrame, text='Add Entry')

# Placing all entry widgets
wordLabel.grid(row=0, column=0, sticky=W)
defLabel.grid(row=0, column=1, sticky=W)
wordEntry.grid(row=1, column=0)
defEntry.grid(row=1, column=1)
addEntryButton.grid(columnspan=2, row=3)

# Placing entry frame
entryFrame.pack()

#newSetButton = Button(entryFrame, text='Create New Set', command=createSet)

root.mainloop()