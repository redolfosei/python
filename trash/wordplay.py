from string import punctuation

class Wordplay:
    """This is to seive the words and output only lowercase words. all puncs. are out"""
    def __init__(self,words_input):
        for pun in punctuation:
            words_input = words_input.replace(pun,"") 
            
        self.words1 = words_input.split()    
        self.words = words_input.lower().split()
        print(f"words after operation: {self.words}")
        
    def words_with_length(self):
        #return "These are the length of words: ".format(len(self.words))
        #return f"These are the lenght of words: {len(self.words)}"
        print(f"These are the lenght of words: {len(self.words)}")
        
    def starts_with(self,string_passed):
        return [word for word in self.words if word[:len(string_passed)] == string_passed]
    
    def ends_with(self,string_passed):
        return [word for word in self.words if word[-1][:len(string_passed)] == string_passed]
    
    def palindromes(self,string_passed):
        string_passed = "".join(s for s in string_passed if s.isalnum())
        for i in range(len(string_passed) // 2):
            if string_passed[i] != string_passed[-i -1]:
                return False
            return True
        #return [word for word in self.words for i in range(len(word)) // 2] if word[i] != word[i] - word[-i-1]]
        #how can you do this with list comprehension?;
        
    def onlyL(self,letter):
        return [word for word in self.words1 if letter in word]
            
    def avoidsL(self,letter):
        return [word for word in self.words1 if letter not in word] 
    
    def avoidsLl(self):
        for word in self.words1:
            if 'L' not in word:
                if 'l' not in word:
                    return word
                return False

string_passed = "#^&*()This Learning have Lots of Lafts what shoudl be tested in %^the @ showers of code%comings"        
wp = Wordplay(string_passed)
wp.words_with_length()
print(wp.starts_with("t"))
print(wp.ends_with("l"))         
print(wp.palindromes("madamt"))
#print(wp.onlyL("L"))
print(wp.onlyL('L'))
#wp.onlyL()
print(wp.avoidsL('L'))
print(wp.avoidsLl())

        








# Write a class called Wordplay. It should have a field that holds a list of words. 
# The user of the class should pass the list of words they want to use to the class. 
# There should be the following methods:
# • words_with_length(length) — returns a list of all the words of length length 
# • starts_with(s) — returns a list of all the words that start with s
# • ends_with(s) — returns a list of all the words that end with s
# • palindromes() — returns a list of all the palindromes in the list
# • only(L) — returns a list of the words that contain only those letters in L
# • avoids(L) — returns a list of the words that contain none of the letters in L
# • avoids(L) — returns a list of the words that contain none of the letters in L or l

# Use Case 
#wordplay = WordPlay([racecar, boy , girls, children, toy, redolf, try, top, madam, civic])
# wordplay.words_with_length(3)
# wordplay.starts_with(t)
# wordplay.ends_with(y)