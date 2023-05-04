teams = ["Man U", "Chelsea", "New Castle", "Liverpool"]
for team in teams:
    print(team.upper())
    print("We will win the title this season")
print("EPL is entertaining!")

numbers = [1,2,4,6,8]
total = 0
for number in numbers:
    total += number
print(total)

triples = [["a","b","c","d"], ["1","2","3","4"], ["he","hike","fake"]]
for list in triples:
    for element in list:
        print(element, end=' ')
    print('I just finished one of the inner loops')
print('Now this is outside bother for loops')

