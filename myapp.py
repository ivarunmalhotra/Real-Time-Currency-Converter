import tkinter as tk
import datetime
import time
from tkinter import messagebox
from forex_python.converter import CurrencyRates, CurrencyCodes
#Program Starts

window=tk.Tk()

window.title("Real Time Currency Converter")

window.geometry("900x500")

window.configure(bg="#113c85")

#----CONVERSION FUNCTION
def conversion():
	cr=CurrencyRates()

	from_curr = entry1.get() #Currency to be converted
	to_curr = entry2.get()	 #Currency to be converted In
	value = amount.get()	 #Value to be converted

	if( value == ""):
		tk.messagebox.showinfo("Warning","No Amount Entered!")
	elif(from_curr =="" or to_curr ==""):
		tk.messagebox.showinfo("Warning","Currency not Entered!")
	else:
		new_amt = cr.convert(from_curr,to_curr,float(value))

		new_amount = float("{:.4f}".format(new_amt))

		#-----OVERWIRTING
		final_amt.delete(0, tk.END)

		#-----END RESULT
		final_amt.insert(0, str(value))
		final_amt.insert(10, str("  "))
		final_amt.insert(20, str(from_curr))
		final_amt.insert(10, str("  =  "))
		final_amt.insert(30, str(new_amount))
		final_amt.insert(40, str("  "))
		final_amt.insert(50, str(to_curr))

		curr_codes()

#-----CODES
def curr_codes():
	cn=CurrencyCodes()

	from_curr = entry1.get() #Currency to be converted
	to_curr = entry2.get()	 #Currency to be converted In

	new_code = cn.get_currency_name(from_curr)
	new_code1 = cn.get_currency_name(to_curr)

	final_codes.delete(0, tk.END)

	final_codes.insert(0, str(new_code))
	final_codes.insert(20, str(" to "))
	final_codes.insert(25, str(new_code1))
	final_codes.insert(45, str(" Conversion."))

#----CLEAR FUNCTION
def clear_all() :

	from_curr = entry1.get() #Currency to be converted
	to_curr = entry2.get()	 #Currency to be converted In
	value = amount.get()	 #Value to be converted
	
	if( value == "" and from_curr =="" and to_curr ==""):
		tk.messagebox.showinfo("Warning","No Amount Entered!")

	entry1.delete(0, tk.END)
	entry2.delete(0, tk.END)
	amount.delete(0, tk.END) 
	final_amt.delete(0, tk.END) 
	final_codes.delete(0, tk.END) 

#-----TIME
def show_time():
	text = time.strftime("%A %d %B %Y %H:%M:%S")
	label.config(text=text)
	label.after(200,show_time)

#-----LABEL 0
label = tk.Label(font=("Calibiri",15),bg="#113c85", fg="white")
label.grid(column=3, row=1)
show_time()

#-----LABEL 1
title = tk.Label(text="Currency Converter",  font=("Alternity",30), fg="white", bg="#113c85")

#-----LABEL 2 
label1 = tk.Label(text="Amount ", font=("Candara Bold",20), fg="white", bg="#113c85")
label2 = tk.Label(text="From ", font=("Candara Bold",20), fg="white", bg="#113c85")
label3 = tk.Label(text="To ", font=("Candara Bold",20), fg="white", bg="#113c85")

#-----MATRIX
label1.grid(row= 3, column=2)
label2.grid(row= 4, column=2)
label3.grid(row= 5, column=2)

#-----AMOUNT
amount = tk.Entry(font=("Candara Bold",15))

#-----ENTRY CURRENCIES
entry1 = tk.Entry(font=("Candara Bold",15))

entry2 = tk.Entry(font=("Candara Bold",15))

#-----BUTTON
convert_btn = tk.Button(text= "Convert", font=("Candara Bold",13), fg="black", bg="#fcb813",command=conversion)

delete_btn = tk.Button(text= "CLear All!", font=("Candara Bold",13), fg="white", bg="#D70000",command=clear_all)

#-----AMOUNT CONVERTED
final_amt = tk.Entry(font=("Sitka Display Bold Italic",30), fg="white", bg="#113c85", borderwidth=0) #FINAL RESULT
final_amt.grid(column=3, row=10, pady=5,ipadx=20)

#-----CODES
final_codes = tk.Entry(font=("Sitka Display Bold Italic",20), fg="white", bg="#113c85", borderwidth=0) #CURRENCY NAMES 
final_codes.grid(column=3, row=11, pady=20,ipadx=200)


#-----MATRIX FORMATION
title.grid(row= 0, column= 3)
amount.grid(row= 3, column= 3, padx=10, pady=10)
entry1.grid(row= 4, column= 3, padx=10, pady=10)
entry2.grid(row= 5, column= 3, padx=10, pady=15)
convert_btn.grid(row= 8, column= 3)
delete_btn.grid(row= 12, column= 3)

window.mainloop()