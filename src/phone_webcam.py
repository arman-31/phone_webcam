import cv2
import tkinter as tk
from tkinter import simpledialog, messagebox
import threading

# Global flag to control webcam stream
running = False  

def start_stream(ip_address):
    """Connect to the phone camera stream and display it as a webcam."""
    global running
    running = True  # Start the webcam stream
    
    url = f"http://{ip_address}/video"
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        messagebox.showerror("Connection Error", "Could not connect to the webcam stream.")
        return

    while running:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Could not read frame.")
            break

        cv2.imshow("Phone Webcam", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

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
    global running
    running = False  # This will stop the loop in `start_stream`
    cv2.destroyAllWindows()

# Create the GUI
root = tk.Tk()
root.title("Phone Webcam App")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Use Your Phone as a Webcam", font=("Arial", 14)).pack(pady=10)
tk.Button(frame, text="Start Webcam", command=start_camera, font=("Arial", 12)).pack(pady=5)
tk.Button(frame, text="Stop Webcam", command=stop_camera, font=("Arial", 12), fg="red").pack(pady=5)

root.mainloop()
