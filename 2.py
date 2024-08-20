import tkinter as ui
import time
import math

window = ui.Tk()
window.geometry("860x900")
def update_clock():
    hours =int(time.strftime("%I"))
    minutes =int(time.strftime("%M"))
    seconds =int(time.strftime("%S"))
    #seconds hand
    seconds_x = seconds_hand_len*math.sin(math.radians(seconds*6))+center_x
    seconds_y = -1 * (seconds_hand_len*math.cos(math.radians(seconds*6)))+centre_y
    Canvas.coords(seconds_hand,center_x,centre_y,seconds_x,seconds_y)
    #minutes hand
    minutes_x = minutes_hand_len*math.sin(math.radians(minutes*6))+center_x
    minutes_y = -1 * (minutes_hand_len*math.cos(math.radians(minutes*6)))+centre_y
    Canvas.coords(minutes_hand,center_x,centre_y,minutes_x,minutes_y)
    #hours hand
    hours_x = hours_hand_len*math.sin(math.radians(hours*30))+center_x
    hours_y = -1 * (hours_hand_len*math.cos(math.radians(hours*30)))+centre_y
    Canvas.coords(hours_hand,center_x,centre_y,hours_x,hours_y)

    window.after(1000,update_clock)

Canvas = ui.Canvas(window, width = 400, height= 400, bg ="white")
Canvas.pack(expand=True, fill='both')
#create background
bg = ui.PhotoImage(file='clock.png')
Canvas.create_image(430,400,image=bg)
#create clock hands
center_x = 425
centre_y = 400
seconds_hand_len = 195
minutes_hand_len =195
hours_hand_len =195
#breaking clock hands
seconds_hand = Canvas.create_line(180,80,230+seconds_hand_len,200+seconds_hand_len,width=1.5,fill='red')
minutes_hand = Canvas.create_line(180,180,230+minutes_hand_len,200+minutes_hand_len,width=3,fill='black')
hours_hand = Canvas.create_line(180,280,230+hours_hand_len,200+hours_hand_len,width=7,fill='black')



update_clock()
window.mainloop()
