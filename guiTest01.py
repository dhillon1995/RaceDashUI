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
DES_logo=tk.Label(frame, text='DT1', font='ariel 18 bold', bg='#000000', fg='#626262')
DES_logo.place(relx=0.01, rely=0.91, relwidth=0.20, relheight=0.05)

#RPM Label
RPM_label = tk.Label(frame, text="RPM", font='ariel 18 bold', bg='#000000', fg='red')
RPM_label.place(relx=0.71, rely=0.01, relwidth=0.20, relheight=0.0)

#RPM Digits
RPM_digits = tk.Label(frame, font='ariel 48 bold', bg='#000000', fg='white')
RPM_digits.place(relx=0.68, rely=0.012, relwidth=0.10, relheight=0.08)


main_app.mainloop()