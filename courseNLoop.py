def course(i):
    switcher={
            "CSC1006":"Course 1006",
            "CSC1007":"Course 1007",
            "CSC1008":"Course 1008",
            "CSC1009":"Object-Oriented Programming",
            "CSC1010":"Course 1010",
            }
    return switcher.get(i,"Invalid input")

c = input('Enter course: ')

print("Course :" ,course(c))
for i in range(67,101,2):
    print(168-i);   