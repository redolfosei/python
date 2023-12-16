def palindrome_checker(words):
    words = words.lower()
    palindrome = True
    #reverse the words 
    rev_words = words[::-1]
    print(rev_words)
    
    if rev_words != words:
        palindrome = False

    if palindrome:
        print('The words entered are a palindrome')
    
    else:
        print('The words entered are not a palindrome')

#Example
palindrome_checker('Tacocat')