# Import necessary modules
import customtkinter
import tkinter
import socket
from tkinter import Tk, PhotoImage
import time

# Set appearance mode and default color theme
a = 'Dark'
b = 'Light'
c = 'System'
customtkinter.set_appearance_mode(b)
customtkinter.set_default_color_theme('blue')

# Create the main Tkinter window
root = customtkinter.CTk()
root.geometry("250x300")
root.title("IpFINDER")
root.resizable(False, False)

# Load background image
# photo1 = PhotoImage(file="bg.png")
# global img
# img = customtkinter.CTkLabel(master=root, image=photo1)
# img.pack()

def landing():
    # Display landing frame with an image
    frame_landing = customtkinter.CTkFrame(master=root, width=250, height=300)
    frame_landing.pack()
    # photo2 = PhotoImage(file="land.png")
    # imgq = customtkinter.CTkLabel(master=frame_landing, image=photo2)
    # imgq.pack()
    time.sleep(0.9)
    frame_landing.destroy()
    spoof()

def find_ip():
    # Get domain from user input and display IP address
    domain = d_entry.get()
    if domain:
        ip_address = socket.gethostbyname(domain)
        ipadd = f"Address is: {ip_address}"
        ip_label.configure(text=ipadd)
    else:
        ip_label.configure(text="Enter a Domain")
        ip_label.place(x=10, y=5)

def spoof():
    # Create spoofing frame
    frame = customtkinter.CTkFrame(master=root, width=200, height=200,
                                   corner_radius=1, border_width=3)
    frame.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    # Add label and entry widget for domain input
    label = customtkinter.CTkLabel(master=frame, text="Enter Domain", font=('Courier New', 20))
    label.place(x=30, y=16)
    global d_entry
    d_entry = customtkinter.CTkEntry(master=frame, width=180, placeholder_text='Domain Here', show='')
    d_entry.place(x=10, y=80)

    # Add button to find IP address
    button = customtkinter.CTkButton(master=frame, width=180, corner_radius=6,
                                     text='FIND IP', hover_color='blue', command=find_ip)
    button.place(x=10, y=120)

    # Display IP address label
    frame1 = customtkinter.CTkFrame(master=root, width=200, height=50,
                                    corner_radius=1, border_width=3)
    frame1.place(relx=0.1, rely=0.755)
    global ip_label
    ip_label = customtkinter.CTkLabel(master=frame1, text="", font=('Arial', 14))
    ip_label.place(x=10, y=5)

# Start with the landing screen
landing()
root.mainloop()
