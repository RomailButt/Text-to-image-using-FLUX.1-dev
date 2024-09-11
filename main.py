import tkinter as tk
from tkinter import ttk, filedialog
import requests
import io
from PIL import Image, ImageTk

# Global variable to store the PIL Image object
pil_image = None

# Function to query the model and display the image
def generate_image():
    global pil_image
    prompt = entry.get()
    width = int(width_entry.get() or 1080)  # Default to 1080 if input is empty
    height = int(height_entry.get() or 1080)  # Default to 1080 if input is empty
    payload = {"inputs": prompt}
    
    # Query the model
    try:
        image_bytes, response_headers = query(payload)
        
        # Check if the content type is correct
        if 'image/jpeg' in response_headers.get('Content-Type'):
            pil_image = Image.open(io.BytesIO(image_bytes))
            pil_image.thumbnail((width, height))  # Resize image to fit in the specified resolution
            img = ImageTk.PhotoImage(pil_image)  # Convert to PhotoImage for display
            image_label.config(image=img)
            image_label.image = img  # Keep a reference to avoid garbage collection
            result_label.config(text="")
        else:
            result_label.config(text="The response is not an image.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

def get_token():
    with open("token.txt", "r") as file:
        return file.read().strip()  # Reads the token and removes any extra spaces/newlines

def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
    token = get_token()  # Get token from the file
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}, {response.text}")
    
    return response.content, response.headers

# Function to save the image
def save_image():
    global pil_image
    if pil_image:
        # Open file dialog to select the save location
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if file_path:
            pil_image.save(file_path)
            result_label.config(text="Image saved successfully.")
    else:
        result_label.config(text="No image to save.")

# Create the main window
root = tk.Tk()
root.title("Image Generator")

# Create and pack widgets
frame = ttk.Frame(root, padding="10")
frame.pack(fill="both", expand=True)

entry = ttk.Entry(frame, width=50)
entry.pack(pady=10)

# Frame for resolution inputs
resolution_frame = ttk.Frame(frame)
resolution_frame.pack(pady=5)

width_label = ttk.Label(resolution_frame, text="Width:")
width_label.pack(side="left")
width_entry = ttk.Entry(resolution_frame, width=10)
width_entry.pack(side="left", padx=5)

height_label = ttk.Label(resolution_frame, text="Height:")
height_label.pack(side="left")
height_entry = ttk.Entry(resolution_frame, width=10)
height_entry.pack(side="left", padx=5)

# Frame for buttons
button_frame = ttk.Frame(frame)
button_frame.pack(pady=5)

generate_button = ttk.Button(button_frame, text="Generate Image", command=generate_image)
generate_button.pack(side="left")

download_button = ttk.Button(button_frame, text="Download Image", command=save_image)
download_button.pack(side="left", padx=5)

image_label = tk.Label(frame)
image_label.pack(pady=10)

result_label = ttk.Label(frame, text="")
result_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
