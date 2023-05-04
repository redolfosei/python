#Sorting function and len() 

alphabets = ["A","D","F","B","C","E"]

print(alphabets)
sorted(alphabets) #temporal sorting
print(alphabets)
print(sorted(alphabets))
print(sorted(alphabets,reverse=True)) #sorts in reverse order

grades = [10,90,40,100,70]
print(grades)
print(sorted(grades))
print(grades)

print()

#the len() fnction returns an interget that represents the length of a list
interger_length = len(grades)
print(type(interger_length))
print(interger_length)

print()

removed_grade = grades.pop()
print("The removed grade is " + str(removed_grade))
print(grades)

print()

#.sort() .reverse() method permenantly sorts a list, 
print(alphabets)
alphabets.sort() #permenantly sorted
print(alphabets) 
alphabets.sort(reverse=True)
print(alphabets)

#sorting methods sorts alphabetical alphabets first before the lower ones
