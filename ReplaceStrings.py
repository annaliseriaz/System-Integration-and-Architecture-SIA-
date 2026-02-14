print("Felicity Zoe O. Villa")
print("2BSIT-1")

print("Nouns")
noun1 = input("Enter the first noun: ")
noun2 = input("Enter the second noun: ")
noun3 = input("Enter the third noun: ")

print("--------------------------------")

print("Adjectives")
adjective1 = input("Enter the first adjectives: ")
adjective2 = input("Enter the second adjectives: ")
adjective3 = input("Enter the third adjectives: ")

print("---------------------------------")

print("Original Song")
original_song = ("""Slow down, slow down to the feeling
Wait up, wait there if you see me
Come by, come back to the moment
The moment

Did I tell you that I miss you?
Did I tell you that I miss you?

Hold on, hold on, we could stay here
Once more, once lost, it was so clear
I'm here, I'm yours for a moment
A moment

Did I tell you that I miss you?
Did I tell you that I miss you?""")

print(original_song)
print("-----------------------------------")

print("Edited Song")
edited_song = (original_song.replace("moment", noun1.upper()))
edited_song = (edited_song.replace("miss", noun2.upper()))
edited_song = (edited_song.replace("comeback", noun3.upper()))
edited_song = (edited_song.replace("stay", adjective1.upper()))
edited_song = (edited_song.replace("tell", adjective2.upper()))
edited_song = (edited_song.replace("clear", adjective3.upper()))

print(edited_song)
