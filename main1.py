'''
Currency converter - Written in Python 3.10 by Brendyn Mullikin

GitHub: https://github.com/bmullikin717

Basic currency converter using tkinter in python. Just made a basic GUI grid layout, and used dictionaries to hold the exchange rates for
each currency to calculate each conversion. Exchange rates do change so if you need to update them, I got the exchange rates from 
here: https://www.x-rates.com/

I just used currencies that seemed the most relevant, but you can always add currencies pretty easily by just adding to the currencies
list and making a dictionary for that currencies exchange rates. Then add another 'elif' statement and you're good.

Wrote in-line since it's easier for me when using GUI libraries. Feel free to use any parts of the code for yourself, but it wouldn't hurt to
show a little credit ;). Happy coding folks! Appreciate you checking it out!
'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font

# Constants
WIDTH = 1000
HEIGHT = 500
BG = '#8099ad'

# List of currencies available
currencies = ['US Dollars', 'Euros', 'Mexican Pesos', 'Japanese Yen', 'British Pounds', 'Australian Dollars', 'Canadian Dollars']

# Dictionaries holding the exchange rates for each currency
us_rates = {'Euros': 0.874, 'Mexican Pesos': 20.428, 'Japanese Yen': 115.80, 'British Pounds': 0.74, 'Australian Dollars': 1.39,
                'Canadian Dollars': 1.27}

euro_rates = {'US Dollars': 1.143472, 'Mexican Pesos': 23.359189, 'Japanese Yen': 132.407738, 'British Pounds': 0.842425, 
                'Australian Dollars': 1.587473, 'Canadian Dollars': 1.448490}

peso_rates = {'US Dollars': 0.048954, 'Euros': 0.042820, 'Japanese Yen': 5.669073, 'British Pounds': 0.036074, 
                'Australian Dollars': 0.067972, 'Canadian Dollars': 0.062008}

yen_rates = {'US Dollars': 0.008634, 'Euros': 0.007553, 'Mexican Pesos': 0.176382, 'British Pounds': 0.006363, 
                'Australian Dollars': 0.011990, 'Canadian Dollars': 0.010937}

british_rates = {'US Dollars': 1.357058, 'Euros': 1.186947, 'Mexican Pesos': 27.717694, 'Japanese Yen': 157.172100, 
                'Australian Dollars': 1.884199, 'Canadian Dollars': 1.718898}

australian_rates = {'US Dollars': 0.720227, 'Euros': 0.630000, 'Mexican Pesos': 14.709876, 'British Pounds': 0.530690, 
                'Japanese Yen': 83.411232, 'Canadian Dollars': 0.912265}

canadian_rates = {'US Dollars': 0.789502, 'Euros': 0.690584, 'Mexican Pesos': 16.125750, 'British Pounds': 0.581725, 
                'Australian Dollars': 1.096202, 'Japanese Yen': 91.434142}


# Root window
root = tk.Tk()
root.title("Currency Converter")

# Values to open window to the center of the screen
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws // 2) - (WIDTH // 2)
y = (hs // 2) - (HEIGHT // 2)
root.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, x, y))
root.configure(background=BG)

# Converting currency function
def convert(value, curr1, curr2):
    # Don't try to calculate if curr1 and curr2 are the same
    if curr1 == curr2:
        return

    # Conversion: Output = input value * exchange rate
    # Get value to convert, what currency to convert from and access the exchange rate from dictionary of currency
    # we're converting to
    if curr1 == 'US Dollars':
        exec_rate = us_rates[curr2]
    elif curr1 == 'Euros':
        exec_rate = euro_rates[curr2]
    elif curr1 == 'Mexican Pesos':
        exec_rate = peso_rates[curr2]
    elif curr1 == 'Japanese Yen':
        exec_rate = yen_rates[curr2]
    elif curr1 == 'British Pounds':
        exec_rate = british_rates[curr2]
    elif curr1 == 'Australian Dollars':
        exec_rate = australian_rates[curr2]
    elif curr1 == 'Canadian Dollars':
        exec_rate = canadian_rates[curr2]
    else:
        return
    
    newValue = float(value) * float(exec_rate)
    
    # Update output label to converted currency value
    output.configure(text=f'{round(newValue, 2)}  {curr2}')


# Heading label
head_label = Label(root, text='Currency Conversion', bg=BG, font=('Consolas', 40), anchor='center')
head_label.grid(row=0, column=0, columnspan=2, padx=(WIDTH // 2) - (577 // 2))

# First dropdown menu
first_dropdown = ttk.Combobox(root, values=currencies, font=('Consolas', 20))
first_dropdown.grid(row=1, column=0, pady=100)

# Value entry
entry = Entry(root, borderwidth=3, font=('Consolas', 20))
entry.grid(row=1, column=1, pady=100)

# Second Dropdown menu
second_dropdown = ttk.Combobox(root, values=currencies, font=('Consolas', 20))
second_dropdown.grid(row=2, column=0)

# Output label
output = Label(root, font=('Consolas', 25, 'italic'), bg=BG)
output.grid(row=2, column=1)

# Convert Button
convert_btn = Button(root, text='Convert', borderwidth=3, relief='raised', fg='black', font=('Consolas', 20, 'bold'), \
                command=lambda: convert(entry.get(), first_dropdown.get(), second_dropdown.get())) # Sending values for each widget to conversion function
convert_btn.grid(row=3, column=0, columnspan=2, pady=20)

# Mainloop to run GUI
root.mainloop()