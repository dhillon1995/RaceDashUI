import tkinter as tk


# --- Main application set up ---
main_app = tk.Tk()
main_app.title('DT1')
#width_value=main_app.winfo_screenwidth()
#height_value=main_app.winfo_screenheight()

width_value=main_app.winfo_screenwidth()
height_value=main_app.winfo_screenheight()
main_app.geometry("%dx%d-0-0" % (width_value, height_value))

# Frame setup
frame = tk.Frame(main_app, bg='#000000')
frame.place(relwidth=1, relheight=1)

# DES Logo
DES_logo=tk.Label(frame, text='TrackLink v0.1', font='ariel 18 bold', bg='#000000', fg='#626262')
DES_logo.place(relx=0.01, rely=0.81, relwidth=0.20, relheight=0.1)

#RPM Label
RPM_label = tk.Label(frame, text="RPM", font='ariel 20 bold', bg='#000000', fg='red')
RPM_label.place(relx=0.13, rely=0.18, relwidth=0.2, relheight=0.08)

#RPM Digits
RPM_digits = tk.Label(frame, font='ariel 52 ', bg='#000000', fg='white')
RPM_digits.place(relx=0.02, rely=0.2, relwidth=0.18, relheight=0.08)

RPMcount = 2000
RPM_digits['text'] = RPMcount

#SPEED Digits
SPEED_digits = tk.Label(frame, text="127", font='ariel 130 bold', bg='#000000', fg='white')
SPEED_digits.place(relx=0.34, rely=0.3, relwidth=0.3, relheight=0.3)

#SPEED Label
SPEED_label = tk.Label(frame, text="MPH", font='ariel 20 bold', bg='#000000', fg='red')
SPEED_label.place(relx=0.46, rely=0.55, relwidth=0.06, relheight=0.05)

#Canvas
my_canvas2 = tk.Canvas(frame, width = 1250, height = 120, background = '#000111', highlightthickness=0)
my_canvas2.place(x=10, y=10)

class Printer():
    count = 0
    upper_limit = 1250

    @staticmethod
    def add_count():
        if Printer.count < Printer.upper_limit :
            Printer.count += 4
            RPM_digits['text'] = Printer.count * 10
            print(Printer.count)
        else:
            Printer.count = 200
            RPM_digits['text'] = Printer.count * 10
            print(Printer.count)#

# Clear Canvas
        my_canvas2.delete("all")
# Create RPM Line/bar     
        if Printer.count > 1200 and Printer.count < Printer.upper_limit:
            rpm_fill = 'red'
        elif Printer.count > 1100 and Printer.count < 1200:
            rpm_fill = 'green'
        else:
            rpm_fill = 'orange'
        
        my_canvas2.create_line(5,5,Printer.count,5, width=240, fill=rpm_fill)
# Call for the loop to start again
        main_app.after(10,Printer.add_count)

Printer.add_count()

main_app.mainloop()
