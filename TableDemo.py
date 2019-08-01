from tkinter import *
import tkinter
import tkinter.messagebox
import sqlite3
import re

class MyGUI:
    
    def __init__(self):
        global db
        db = sqlite3.connect('C:/Users/Victor/Desktop/CITIES.db')
        global cursor
        cursor = db.cursor()
        
        self.window = tkinter.Tk()

        self.l1 = Label(self.window, text = 'SELECT ENTRY FROM DATABASE')
        self.l1.grid(row = 0, column = 0)

        self.l3 = Label(self.window, text = 'WHERE')
        self.l3.grid(row = 1, column = 0)

        self.l4 = Label(self.window, text = 'EQUALS')
        self.l4.grid(row = 1, column = 2)

        self.l5 = Label(self.window, text = 'INSERT AND UPDATE NEW ENTRIES BELOW')
        self.l5.grid(row = 2, column = 0)

        self.l6 = Label(self.window, text = 'CITY')
        self.l6.grid(row = 3, column = 0)
        self.l7 = Label(self.window, text = 'STATE')
        self.l7.grid(row = 3, column = 2)
        self.l8 = Label(self.window, text = 'COUNTY')
        self.l8.grid(row = 4, column = 0)
        self.l9 = Label(self.window, text = 'POPULATION')
        self.l9.grid(row = 4, column = 2)
        self.l10 = Label(self.window, text = 'DENSITY')
        self.l10.grid(row = 5, column = 0)

        #define entries
        self.where_text = StringVar()
        self.e2 = Entry(self.window, textvariable = self.where_text)
        self.e2.grid(row = 1, column = 1)

        self.equals_text = StringVar()
        self.e3 = Entry(self.window, textvariable = self.equals_text)
        self.e3.grid(row = 1, column = 3)

        self.city_text = StringVar()
        self.e4 = Entry(self.window, textvariable = self.city_text)
        self.e4.grid(row = 3, column = 1)

        self.state_text = StringVar()
        self.e5 = Entry(self.window, textvariable = self.state_text)
        self.e5.grid(row = 3, column = 3)

        self.county_text = StringVar()
        self.e6 = Entry(self.window, textvariable = self.county_text)
        self.e6.grid(row = 4, column = 1)

        self.population_text = StringVar()
        self.e7 = Entry(self.window, textvariable = self.population_text)
        self.e7.grid(row = 4, column = 3)

        self.density_text = StringVar()
        self.e8 = Entry(self.window, textvariable = self.density_text)
        self.e8.grid(row = 5, column = 1)
        

        #define listbox
        self.list1 = Listbox(self.window, height = 20, width = 95)
        self.list1.grid(row = 6, column = 0, rowspan = 6, columnspan = 2)

        #scroll bar
        self.sb1 = Scrollbar(self.window)
        self.sb1.grid(row = 2, column = 2, rowspan = 6)

        self.list1.configure(yscrollcommand = self.sb1.set)
        self.sb1.configure(command = self.list1.yview)

        #define buttons
        self.b1 = Button(self.window, text = "Search Entry", command = self.search, width = 12)
        self.b1.grid(row = 6, column = 3)

        self.b2 = Button(self.window, text = "Add Entry", command = self.add, width = 12)
        self.b2.grid(row = 7, column = 3)

        self.b3 = tkinter.Button(self.window, text = "Update Selected", command = self.update, width = 12)
        self.b3.grid(row = 8, column = 3)

        self.b4 = tkinter.Button(self.window, text = "Delete Selected", command = self.delete, width = 12)
        self.b4.grid(row = 9, column = 3)

        self.b5 = tkinter.Button(self.window, text = "Close", width = 12, command = self.window.destroy)
        self.b5.grid(row = 10, column = 3)

        tkinter.mainloop()

    def search(self):

        select_criteria = str(self.e3.get())

        def print_result():
            result = cursor.fetchall()
            if(result == []):
                tkinter.messagebox.showinfo('Response', 'No entries matched this criteria.')
            for i in range(len(result)): 
                arr = str(result[i])
                self.list1.insert(i, arr)
                
            db.commit()

        if(str(self.e2.get()) == "City"):
            cursor.execute("SELECT * FROM Cities WHERE City=?", (select_criteria,))
            print_result()

        if(str(self.e2.get()) == "State"):
            cursor.execute("SELECT * FROM Cities WHERE State=?", (select_criteria,))
            print_result()

        if(str(self.e2.get()) == "County"):
            cursor.execute("SELECT * FROM Cities WHERE County=?", (select_criteria,))
            print_result()
        
        if(str(self.e2.get()) == "Population"):
            cursor.execute("SELECT * FROM Cities WHERE Population =?", (select_criteria,))
            print_result()

        if(str(self.e2.get()) == "Density"):
            cursor.execute("SELECT * FROM Cities WHERE Density=?", (select_criteria,))
            print_result()
            
    def add(self):
        
        city = self.e4.get()
        state = self.e5.get()
        county = self.e6.get()
        population = int(self.e7.get())
        density = int(self.e8.get())

        cursor.execute("INSERT INTO Cities (City, State, County, Population, Density) VALUES (?,?,?,?,?)",
                       (city, state, county, population, density))
        db.commit()
        
        tkinter.messagebox.showinfo('Response', 'Entry added')

    def update(self):
        value = self.list1.get(self.list1.curselection())
        value = value[1:-1]
        value = value.replace(',','')
        value = value.replace("'", "")
        value = value.strip()

        city = value[0]

        cursor.execute('DELETE FROM Cities WHERE City=?', (city))
        db.commit()

        city = self.e4.get()
        state = self.e5.get()
        county = self.e6.get()
        population = int(self.e7.get())
        density = int(self.e8.get())

        cursor.execute("INSERT INTO Cities (City, State, County, Population, Density) VALUES (?,?,?,?,?)",
                       (city, state, county, population, density))
        db.commit()
        
        tkinter.messagebox.showinfo('Response', 'Entry updated')

        

    def delete(self):
        
        value = self.list1.get(self.list1.curselection())
        value = value[1:-1]
        value = value.replace(', ','')
        value = value.replace("'", "")
        value = value.strip()

        city = value[0]

        cursor.execute('DELETE FROM Cities WHERE City=?', (city))
        db.commit()
        
        tkinter.messagebox.showinfo('Response', 'Entry Deleted')

my_gui = MyGUI()



















