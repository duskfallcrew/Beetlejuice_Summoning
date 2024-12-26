import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

class BeetlejuiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Beetlejuice Summoning")
        self.summon_count = 0
        
        # Initial message
        self.label = tk.Label(root, text="Welcome to the Beetlejuice summoning script!\nTo summon Beetlejuice, say his name three times.", wraplength=300)
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)
        
        self.submit_button = tk.Button(root, text="Summon Beetlejuice", command=self.summon_beetlejuice)
        self.submit_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        # Add a label for the image display
        self.image_label = tk.Label(root, text="Summon Beetlejuice to see his face!", font=("Arial", 12))
        self.image_label.pack(pady=10)
        
    def summon_beetlejuice(self):
        user_input = self.entry.get()
        if user_input.lower() == "beetlejuice":
            self.summon_count += 1
            self.result_label.config(text=f"Beetlejuice! ({self.summon_count}/3)")
            if self.summon_count == 3:
                self.result_label.config(text="Beetlejuice has been summoned successfully!")
                self.show_beetlejuice_face()
        else:
            self.result_label.config(text="That's not Beetlejuice's name! Try again.")
        self.entry.delete(0, tk.END)

    def show_beetlejuice_face(self):
        try:
            # Get the directory of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the full path to the image file
            image_path = os.path.join(script_dir, "beetlejuice.jpg")
            img = Image.open(image_path)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            # Update the image_label with the image
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep reference to avoid garbage collection
            self.image_label.config(text="It's Showtime!!")
            self.root.after(3000, self.launch_video)  # Launch video after 3 seconds

        except FileNotFoundError:
            messagebox.showerror("Error", "beetlejuice.jpg not found in the current directory.")
            self.image_label.config(text="Image file not found!")

    def launch_video(self):
        video_url = "https://www.youtube.com/watch?v=ErHL4qwwyxw"
        webbrowser.open(video_url)

if __name__ == "__main__":
    root = tk.Tk()
    app = BeetlejuiceApp(root)
    root.mainloop()
