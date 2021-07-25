# made by @sandrzejewskipl on github

# import modules
import requests, time, os, sys
from tkinter import *
import datetime as dt
from datetime import datetime
    
# User-Agent
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'


# Gui
class GUI:
    def __init__(self, window):
        global A1, A2, A3, A4, E1, E2, E3, E4, we2, P, E6, E7, PP
        
        try:
            GUI.removethis1()
        except Exception:
            pass
        try:
            GUI.removethis2()
        except Exception:
            pass
        try:
            GUI.removebegin()
        except Exception:
            pass
        A1 = Label(window,text='Target')
        A1.place(x=10,y=10)
        E1 = Entry(window, bd =5)
        E1.place(x=10,y=30)
        
        A2 = Label(window,text='Bearer Key')
        A2.place(x=250,y=10)
        E2 = Entry(window, bd =5)
        E2.place(x=250,y=30)
        
        E6 = Label(window,text='Time of Availability')
        E6.place(x=10,y=60)
        P = Entry(window, bd =5)
        P.place(x=10,y=80)
        P.insert(0, dt.datetime.now().strftime("%H:%M:%S"))
        
        E7 = Label(window,text='Delay after release time')
        E7.place(x=250,y=60)
        PP = Entry(window, bd =5)
        PP.place(x=250,y=80)

        
        we2 = Button(window,text='Insert Info',command=GUI.insertinfo)
        we2.place(x=165, y=40)
        
    # Removes the begin button
    def removebegin():
        we.destroy()
        
    # Updates info
    def insertinfo():
        global username, password, profileid, auth, we

        # Inputs
        username = E1.get() # Target

        toke = E2.get() # Bearer Key

        auth = 'Bearer ' + toke

        # Don't have empty lines
        if username == '':
            print('Missing Target Username!')
        elif toke == '':
            print('Missing Bearer Key!')
        else:
            we = Button(window,text='Begin',command=GUI.name)
            we.place(x=175, y=100)

    # Change the name
    def name():
        try:
            TimeOfAvailability = P.get()
            h = TimeOfAvailability.split(':')[0]
            m = TimeOfAvailability.split(':')[1]
            s = TimeOfAvailability.split(':')[2]
            if m == '00' and s == '00':
                if int(h) < 11:
                    hh = int(h) - 1
                    hh = '0' + str(hh)
                else:
                    hh = int(h) - 1
                    hh = str(hh)
                date = hh + ':59:59'
            elif s == '00':
                if int(m) < 11:
                    mm = int(m) - 1
                    mm = '0' +  str(mm)
                else:
                    mm = int(m) - 1
                    mm = str(mm)
                date = h + ':' + mm + ':59'
                
            else:
                if int(s) < 11:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + '0' + str(ss)
                else:
                    ss = int(s) - 1
                    date = h + ':' + m + ':' + str(ss)
            
            while True:
                # Grab the time right now
                now = dt.datetime.now().strftime("%H:%M:%S")
                    
                if now == date:
                    if '.' in PP.get():
                        time.sleep(float(PP.get()))
                    else:
                        time.sleep(int(PP.get()))
                    # Change the username
                    for i in range(5):
                        s=requests.put(f'https://api.minecraftservices.com/minecraft/profile/name/{username}', headers={'Authorization': auth,'User-Agent': useragent})
                        if s.status_code == 200:
                            print(f'{username} is now yours!')
                            break
                        print(s.status_code)
                        print(s.text)
                    break

        except Exception as e:
            print(e)
                    
# Define parent
window=Tk()

# Define title
window.title('Minecraft NameSniper')

# Define size of 
window.geometry("400x150")
window.resizable(0,0)

# Run Program
root = GUI(window)
window.mainloop()