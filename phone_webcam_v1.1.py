import cv2
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import threading

# Global variables
running = False  
cap = None  

def start_stream(ip_address):
    """Start the webcam stream inside the Tkinter app."""
    global running, cap
    running = True  
    url = f"http://{ip_address}/video"
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        messagebox.showerror("Connection Error", "Could not connect to the webcam stream.")
        running = False
        return

    update_frame()

def update_frame():
    """Update the video feed inside the Tkinter window."""
    global cap, running
    if running and cap:
        ret, frame = cap.read()
        if ret:
            # Convert frame to RGB format for Tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            
            webcam_label.imgtk = imgtk  # Keep a reference
            webcam_label.configure(image=imgtk)

        # Schedule next frame update
        root.after(10, update_frame)

def start_camera():
    """Get IP from user input and start the stream in a new thread."""
    global running
    if running:
        messagebox.showinfo("Info", "Webcam is already running.")
        return
    
    ip_address = simpledialog.askstring("Input", "Enter the IP Address (e.g., 192.168.1.100:4747):")
    
    if ip_address:
        threading.Thread(target=start_stream, args=(ip_address,), daemon=True).start()

def stop_camera():
    """Stop the webcam stream."""
    global running, cap
    running = False  
    if cap:
        cap.release()
        cap = None  

    # Clear the webcam display
    webcam_label.configure(image="")

# Create the GUI
root = tk.Tk()
root.title("Phone Webcam App")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Use Your Phone as a Webcam", font=("Arial", 14)).pack(pady=10)

# Video feed label
webcam_label = tk.Label(frame)
webcam_label.pack()

# Buttons
tk.Button(frame, text="Start Webcam", command=start_camera, font=("Arial", 12)).pack(pady=5)
tk.Button(frame, text="Stop Webcam", command=stop_camera, font=("Arial", 12), fg="red").pack(pady=5)

root.mainloop()
