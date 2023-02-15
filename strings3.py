#Strings

lyrics = "cant eat cant wait cant drink cant sing my song"

lyrics = lyrics.lower()

c_lyrics = lyrics.count("c")
print(c_lyrics)

print("our lyrics has", c_lyrics, "c' in it", sep=" ")
#The sep function seperates values, you can also insert something is there to seperate them with
print("Our lyrics has" + str(c_lyrics) + "c's in it")
