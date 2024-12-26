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
        
        self.label = tk.Label(root, text="Welcome to the Beetlejuice summoning script!\nTo summon Beetlejuice, say his name three times.")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)
        
        self.submit_button = tk.Button(root, text="Summon Beetlejuice", command=self.summon_beetlejuice)
        self.submit_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
        self.validate_button = tk.Button(root, text="Validate Summoning", command=self.validate_lyrics, state=tk.DISABLED)
        self.validate_button.pack(pady=10)
        
    def summon_beetlejuice(self):
        user_input = self.entry.get()
        if user_input.lower() == "beetlejuice":
            self.summon_count += 1
            self.result_label.config(text=f"Beetlejuice! ({self.summon_count}/3)")
            if self.summon_count == 3:
                self.result_label.config(text="Beetlejuice has been summoned successfully!")
                self.show_beetlejuice_face()
                self.validate_button.config(state=tk.NORMAL)
        else:
            self.result_label.config(text="That's not Beetlejuice's name! Try again.")
        self.entry.delete(0, tk.END)
    
    def show_beetlejuice_face(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Beetlejuice")
        try:
            img = Image.open("beetlejuice.jpg")  # Ensure you have an image named beetlejuice.jpg in the same directory
            img = img.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(new_window, image=photo)
            img_label.image = photo  # Keep a reference to avoid garbage collection
            img_label.pack()
        except FileNotFoundError:
            messagebox.showerror("Error", "beetlejuice.jpg not found in the current directory.")
            label = tk.Label(new_window, text="Image file not found")
            label.pack()


    def validate_lyrics(self):
        def check_lyrics():
            lyrics = lyrics_entry.get()
            expected_phrase = "Hey, folks! Begging your pardon!" # Changed to a single expected phrase

            if expected_phrase.lower() in lyrics.lower():
                messagebox.showinfo("Validation", "Congratulations! Your summoning is validated.")
                video_url = "https://www.youtube.com/watch?v=ErHL4qwwyxw"
                webbrowser.open(video_url)
            else:
                messagebox.showwarning("Validation", f"Sorry, the summoning is not validated. Expected phrase: {expected_phrase}")
            lyrics_entry.delete(0, tk.END)
        
        lyrics_window = tk.Toplevel(self.root)
        lyrics_window.title("Validate Summoning")
        lyrics_label = tk.Label(lyrics_window, text="Enter the first phrase from 'The Whole Being Dead THING':") # Updated label
        lyrics_label.pack(pady=10)
        lyrics_entry = tk.Entry(lyrics_window, width=50)
        lyrics_entry.pack(pady=10)
        validate_button = tk.Button(lyrics_window, text="Validate", command=check_lyrics)
        validate_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BeetlejuiceApp(root)
    root.mainloop()
