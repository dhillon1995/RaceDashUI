import tkinter as tk
from tkinter.constants import CENTER
from PIL import ImageTk,Image  

# --- Main application set up ---
main_app = tk.Tk()
main_app.title('DT1')
#width_value=main_app.winfo_screenwidth()
#height_value=main_app.winfo_screenheight()

width_value=main_app.winfo_screenwidth()
height_value=main_app.winfo_screenheight()
main_app.geometry("%dx%d-0-0" % (width_value, height_value))

# Frame setup
frame = tk.Frame(main_app, bg='black')
frame.place(relwidth=1, relheight=1)

# DES Logo
DES_logo=tk.Label(frame, text='DT1', font='ariel 18 bold', bg='#000000', fg='#626262')
DES_logo.place(relx=0.01, rely=0.91, relwidth=0.20, relheight=0.05)

#Canvas
my_canvas2 = tk.Canvas(frame, width = 800, height = 120, background = 'black', highlightthickness=0)
my_canvas2.place(x=10, y=10)

img = ImageTk.PhotoImage(Image.open(r'/home/pi/Desktop/TestDial1.png'))

my_canvas3 = tk.Canvas(frame, width = 1200, height = 820, background = 'black', highlightthickness=0)
my_canvas3.place(x=10, y=10)

my_canvas3.create_image(680, 406, anchor=CENTER, image=img, tags="logo")

        
class Dial():
    count = 200
    upper_limit = 359

    @staticmethod
    def add_Dialcount():
        if Dial.count < Dial.upper_limit :
            Dial.count -= 3
            print(Dial.count)
            CanvasCreate.canvas_Handling()
        else:
            Dial.count = 200
            print(Dial.count)
            CanvasCreate.canvas_Handling()

class CanvasCreate():
        @staticmethod
        def canvas_Handling():
                # Clear Canvas
                my_canvas3.delete("dial")
        # Create RPM Line/bar
                my_canvas3.create_arc(300,30,1060,800, extent=Dial.count, fill='#a15800', tags="dial") 
                my_canvas3.tag_raise("logo")
        # Call for the loop to start again
                main_app.after(10,Dial.add_Dialcount)


Dial.add_Dialcount()

main_app.mainloop()
