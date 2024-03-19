import webbrowser

def summon_beetlejuice_single_line():
    summon_count = 0
    while summon_count < 3:
        user_input = input("Summon Beetlejuice by saying his name three times (one line per summon): ")
        if user_input.lower() == "beetlejuice":
            summon_count += 1
            print("Beetlejuice!")
        else:
            print("That's not Beetlejuice's name!")
    print("Beetlejuice has been summoned!")
    return True

def validate_lyrics():
    lyrics = input("Please enter lyrics from 'The Whole Being Dead THING': ")
    expected_phrases = [
        "Hey, folks! Begging your pardon!",
        "'Scuse me! Sorry to barge in!",
        "Now let's skip the tears and start on the whole",
        "Y'know, 'being dead' thing",
        "You're doomed! Enjoy the singing",
        "The sword of Damocles is swinging",
        "And if I hear your cell phone ringing",
        "I'll kill you myself",
        "The whole 'being dead' thing!",
        "Death can get a person stressed",
        "\"We should have carpe'd way more diems",
        "Now we're never gonna see 'em!\"",
        "I can show you what comes next",
        "So don't be freaked",
        "Stay in your seats",
        "I do this bullshit, like, eight times a week",
        "So just relax, you'll be fine",
        "Drink your fifty-dollar wine",
        "And take a breath!",
        "You're",
        "You're gonna be fine",
        "On the other side",
        "DIE! YOU'RE ALL GONNA DIE!",
        "YOU'RE ALL GONNA DIE!",
        "I'll",
        "I'll be your guide",
        "To the other side",
        "Well in full disclosure: it's a show about death!",
        "Everybody gets on fine here",
        "Like Rodgers, Hart, and Hammerstein here",
        "The women's bathroom has no line here",
        "Just pee where you want",
        "The whole 'being dead' thing!",
        "You're just gonna love the folks here",
        "Yeah, I know you're woke, but you can take a joke here",
        "And every show I do, like, a TON of coke here",
        "The whole—",
        "[Snorts loudly.]",
        "PAH-HAH! The whole 'being dead' thing!",
        "Nobody is bullet-proof",
        "\"I work out, I eat clean!\"",
        "Jesus, pass the Dramamine",
        "Time to face the brutal truth: (Dies Illa)",
        "'Cause we're all on a hit list",
        "Might not live 'till Christmas",
        "Choke to death on Triscuits",
        "Hey, that's just statistics",
        "So take a little break here",
        "Kinda like a wake here",
        "The scenery is fake here",
        "But there's a giant snake here!",
        "Ha ha ha",
        "You're",
        "You're gonna be fine—thank you!",
        "On the other side—how you doin'?",
        "Oh, not good!",
        "Ba-be-ba-ba-be-bo-boo-bap-boop!",
        "Seriously, though, this is a show about—",
        "Death is taboo, but it's hardly something new",
        "There's nothing medical professionals could do",
        "'cept maybe just bill you",
        "If you die while listening to this album, it's still gonna keep playing.",
        "There's no destiny or fate",
        "Just a terrifying wait",
        "Filled with people that you hate",
        "And on a certain date, the Universe kills you!",
        "That's the thing with life:",
        "No one makes it out alive",
        "Toss that body in the pit",
        "\"Gosh, it's awful, ain't it tragic?\"",
        "\"Blah-blah, Bible, Jesus magic\"",
        "When you're dead, who gives a shit?",
        "\"No pilates, no more yoga!\"",
        "\"Namaste\", you freakin' posers",
        "From the cradle to cremation (Dies Irae)",
        "Death just needs a little conversation!",
        "I have mastered the art (Dies Irae)",
        "Of tearing convention apart (Dies Irae)",
        "So, how about we all make a start (Dies Irae)",
        "On the whole 'being dead' thing!",
        "God, I hope you're ready for a show about death!"
    ]
    return all(phrase.lower() in lyrics.lower() for phrase in expected_phrases)

# Call this function after Beetlejuice has been summoned three times
def play_beetlejuice_song():
    print("You've summoned Beetlejuice three times! Now let's validate your summoning with lyrics.")
    if validate_lyrics():
        print("Congratulations! Your summoning is validated.")
        # Open YouTube video of Beetlejuice Animatic 
        video_url = "https://www.youtube.com/watch?v=ErHL4qwwyxw"
        webbrowser.open(video_url)
    else:
        print("Sorry, the summoning is not validated. Please try again later.")

