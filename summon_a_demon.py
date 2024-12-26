import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import re # this is used in the validation.

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

            # Update the image_label with the image and text
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep reference to avoid garbage collection
            self.image_label.config(text="It's Showtime!!")

            # Launch video after 3 seconds
            self.root.after(3000, self.launch_video)
            
        except FileNotFoundError:
            messagebox.showerror("Error", "beetlejuice.jpg not found in the current directory.")
            self.image_label.config(text="Image file not found!")

    def launch_video(self):
        video_url = "https://www.youtube.com/watch?v=ErHL4qwwyxw"
        webbrowser.open(video_url)

    # Validation code is commented out for future use.
    # def validate_lyrics(self):
    #     lyrics = self.phrase_entry.get()
    #     print(f"User input for lyrics: '{lyrics}'")
    #     expected_phrases = [
    #         "Hey, folks! Begging your pardon!",
    #         "Scuse me! Sorry to barge in!",
    #         "Now let's skip the tears and start on the whole",
    #         "Y'know, 'being dead' thing",
    #         "You're doomed! Enjoy the singing",
    #         "The sword of Damocles is swinging",
    #         "And if I hear your cell phone ringing",
    #         "I'll kill you myself",
    #         "The whole 'being dead' thing!",
    #         "Death can get a person stressed",
    #         "We should have carpe'd way more diems",
    #         "Now we're never gonna see 'em!",
    #         "I can show you what comes next",
    #         "So don't be freaked",
    #         "Stay in your seats",
    #         "I do this bullshit, like, eight times a week",
    #         "So just relax, you'll be fine",
    #         "Drink your fifty-dollar wine",
    #         "And take a breath!",
    #         "You're",
    #         "You're gonna be fine",
    #         "On the other side",
    #         "DIE! YOU'RE ALL GONNA DIE!",
    #         "YOU'RE ALL GONNA DIE!",
    #         "I'll",
    #         "I'll be your guide",
    #         "To the other side",
    #         "Well in full disclosure: it's a show about death!",
    #         "Everybody gets on fine here",
    #         "Like Rodgers, Hart, and Hammerstein here",
    #         "The women's bathroom has no line here",
    #         "Just pee where you want",
    #         "The whole 'being dead' thing!",
    #         "You're just gonna love the folks here",
    #         "Yeah, I know you're woke, but you can take a joke here",
    #         "And every show I do, like, a TON of coke here",
    #         "The whole—",
    #         "PAH-HAH! The whole 'being dead' thing!",
    #         "Nobody is bullet-proof",
    #         "I work out, I eat clean!",
    #         "Jesus, pass the Dramamine",
    #         "Time to face the brutal truth: (Dies Illa)",
    #         "Cause we're all on a hit list",
    #         "Might not live 'till Christmas",
    #         "Choke to death on Triscuits",
    #         "Hey, that's just statistics",
    #         "So take a little break here",
    #         "Kinda like a wake here",
    #         "The scenery is fake here",
    #         "But there's a giant snake here!",
    #         "Ha ha ha",
    #         "You're",
    #         "You're gonna be fine—thank you!",
    #         "On the other side—how you doin'?",
    #         "Oh, not good!",
    #         "Ba-be-ba-ba-be-bo-boo-bap-boop!",
    #         "Seriously, though, this is a show about—",
    #         "Death is taboo, but it's hardly something new",
    #         "There's nothing medical professionals could do",
    #         "cept maybe just bill you",
    #         "If you die while listening to this album, it's still gonna keep playing.",
    #         "There's no destiny or fate",
    #         "Just a terrifying wait",
    #         "Filled with people that you hate",
    #         "And on a certain date, the Universe kills you!",
    #         "That's the thing with life:",
    #         "No one makes it out alive",
    #         "Toss that body in the pit",
    #         "Gosh, it's awful, ain't it tragic?",
    #         "Blah-blah, Bible, Jesus magic",
    #         "When you're dead, who gives a shit?",
    #         "No pilates, no more yoga!",
    #         "Namaste, you freakin' posers",
    #         "From the cradle to cremation (Dies Irae)",
    #         "Death just needs a little conversation!",
    #         "I have mastered the art (Dies Irae)",
    #         "Of tearing convention apart (Dies Irae)",
    #         "So, how about we all make a start (Dies Irae)",
    #         "On the whole 'being dead' thing!",
    #         "God, I hope you're ready for a show about death!"
    #         ]
    #     # Regex to check if any of the expected phrases appears, allowing for case variations and partial matches:
    #     if any(re.search(r'\b' + re.escape(phrase) + r'\b', lyrics, re.IGNORECASE) for phrase in expected_phrases):
    #          messagebox.showinfo("Validation", "Congratulations! Your summoning is validated.")
    #          video_url = "https://www.youtube.com/watch?v=ErHL4qwwyxw"
    #          webbrowser.open(video_url)
    #     else:
    #        messagebox.showwarning("Validation", "Sorry, the summoning is not validated.")
    #     self.phrase_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BeetlejuiceApp(root)
    root.mainloop()
