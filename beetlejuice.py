import tkinter as tk
from PIL import Image, ImageTk

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
        new_window = tk.Toplevel(self.root)
        new_window.title("Beetlejuice")
        img = Image.open("beetlejuice.jpg")  # Ensure you have an image named beetlejuice.jpg in the same directory
        img = img.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(new_window, image=photo)
        img_label.image = photo  # Keep a reference to avoid garbage collection
        img_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BeetlejuiceApp(root)
    root.mainloop()
#this version is just making sure it works and doesn't override the other one, because i might bring back the lyrics lol
