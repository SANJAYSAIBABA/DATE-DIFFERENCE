
#**************************** import packeges**********************************************

from tkinter import *
from datetime import *
from calendar import *
from tkinter import messagebox
from dateutil import relativedelta


#****************************** for create center window **********************************
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

window = Tk()
window.title("Sai Infotech, Gandhinagar")
window.minsize(600, 600)
#window.iconbitmap(r"C:\Users\SAIBABA\Desktop\setup\saibaba.ico")
window.maxsize(600, 600)
center(window)
#**********************************for uset input ***************************************
heding = Label(window, text="DATA ENTRY MENU", font=("Areal", 20, "bold")).pack()
lable_1 = Label(window, text="Enter First Date in 'DD/MM/YYYY' Format      :", 
    font=("Areal", 16, "bold")).place(x=10, y=40)
lable_2 = Label(window, text="Enter Second Date in 'DD/MM/YYYY' Format :",   
    font=("Areal", 16, "bold")).place(x=10, y=80)
lable_3 = Label(window, text="Total Days between Fist Date & Last Date is :", 
    font=("Areal", 16, "bold")).place(x=10, y=120)
lable_4 = Label(window, text="Today your Age is :", 
    font=("Areal", 16, "bold")).place(x=10, y=160)
lable_5 = Label(window, text="Years,", 
    font=("Areal", 16, "bold")).place(x=280, y=160)
lable_6 = Label(window, text="Months,", 
    font=("Areal", 16, "bold")).place(x=390, y=160)
lable_7 = Label(window, text="Days.", 
    font=("Areal", 16, "bold")).place(x=520, y=160)
lable_8 = Label(window, text="If You Class 1 then your Retirement Date is  : ", 
    font=("Areal", 16, "bold")).place(x=10, y=200)
lable_9 = Label(window, text="If You Class 2 then your Retirement Date is  : ", 
    font=("Areal", 16, "bold")).place(x=10, y=240)
lable_10 = Label(window, text="If You Class 3 then your Retirement Date is  : ", 
    font=("Areal", 16, "bold")).place(x=10, y=280)
lable_10 = Label(window, text="If You Class 4 then your Retirement Date is  : ", 
    font=("Areal", 16, "bold")).place(x=10, y=320)
lable_11 = Label(window, text="If You I.A.S. Officer your Retirement Date is  : ", 
    font=("Areal", 16, "bold")).place(x=10, y=360)
t_date1 = StringVar()
t_date2 = StringVar()
t_date1.set('01/01/1001')
t_date2.set('31/12/9999')
entry = Entry (window, textvariable = t_date1, font=("Areal", 16, "bold"), width = 9).place(x=470, y=40)
entry2= Entry (window, textvariable = t_date2, font=("Areal", 16, "bold"), width = 9).place(x=470, y=80)

################################################## for valid date #######################################


def do_it():

    try:
        f_date = (t_date1.get())
        y1 = datetime.strptime(f_date, '%d/%m/%Y')
        newy1 = y1.strftime('%d/%m/%Y')        
    except:
        messagebox.showerror("Error", "Please Enter Correct First Date")
        return entry
    try:
        l_date = (t_date2.get())
        y2 = datetime.strptime(l_date, '%d/%m/%Y')
        newy2 = y2.strftime('%d/%m/%Y')
    except:
        messagebox.showerror("Error", "Please Enter Correct Second Date")
        return entry2


##########################################for date difference ##########################################


    delta = (y2 - y1)
    result = (delta.days + 1)

    leble_12=Label(window,font=("Areal",16,"bold"),width=8,text="00000000",anchor=E).place(x=470, y=120)
    leble_13=Label(window,font=("Areal",16,"bold"),width=8,text=result, anchor=E).place(x=470, y=120)


############################################ for last day of month and equal date diff######################

    date_1 = datetime.strptime(f_date, '%d/%m/%Y')
    date_2 = datetime.strptime(l_date, '%d/%m/%Y')  
      
    day, month, year = f_date.split('/')    
    
    tt = datetime.strptime(str(day)+str(month)+str(year),'%d%m%Y').date()
    addyear58 = datetime(tt.year+58, tt.month, tt.day)

    month_range = monthrange(addyear58.year, addyear58.month)
    last_day = month_range[1]   
    
    finaldate58 = datetime(addyear58.year, addyear58.month, last_day).date()
    convert58 = datetime.strftime(finaldate58, '%d/%m/%Y')  

    leble_14 = Label(window, font=("Areal", 16, "bold"), text=convert58).place(x=470, y=200)
    leble_15 = Label(window, font=("Areal", 16, "bold"), text=convert58).place(x=470, y=240)
    leble_16 = Label(window, font=("Areal", 16, "bold"), text=convert58).place(x=470, y=280)

    day, month, year = f_date.split('/')
    
    tt = datetime.strptime(str(day)+str(month)+str(year),'%d%m%Y').date()
    addyear60 = date(tt.year+60, tt.month, tt.day)

    month_range = monthrange(addyear60.year, addyear60.month)
    last_day = month_range[1]

    finaldate60 = datetime(addyear60.year, addyear60.month, last_day).date()
    convert60 = datetime.strftime(finaldate60, '%d/%m/%Y')

    leble_14 = Label(window, font=("Areal", 16, "bold"), text=convert60).place(x=470, y=320)
    leble_14 = Label(window, font=("Areal", 16, "bold"), text=convert60).place(x=470, y=360)  
    
    #This will find the difference between the two dates
    difference = relativedelta.relativedelta(date_2, date_1)
    years = difference.years
    months = difference.months
    days = difference.days

    lebleyearT = Label(window,font=("Areal",16,"bold"),width=4,text="0000", anchor=E).place(x=220,y=160)  # for clear screen
    leblemontT = Label(window,font=("Areal",16,"bold"),width=2,text="00",   anchor=E).place(x=355,y=160)	# for clear screen
    lebledayT  = Label(window,font=("Areal",16,"bold"),width=2,text="00",   anchor=E).place(x=485,y=160)	# for clear screen  
    
    
    lebleyear = Label(window,font=("Areal",16,"bold"),width=4,text=format(years,'>4'),anchor=E).place(x=220, y=160)   # for year output    
    leblemont = Label(window,font=("Areal",16,"bold"),width=2,text=format(months,'>2'),anchor=E).place(x=355, y=160)	# for month output
    lebleday  = Label(window,font=("Areal",16,"bold"),width=2,text=format(days,'>2'),anchor=E).place(x=485, y=160)  	# for day output 

work = Button(window, text = "Click me for Result", font=("Areal", 16, "bold"), 			#  for geting result
    width=20, heigh=2, bg="yellow", command = do_it).place (x=165, y= 475)



window.mainloop()

