Name= "Nita"
Age = 15
Height = 1.70
print(type(Name))
print(type(Age))
print(type(Height))

#მომხმარებელს შემოატანინეთ თავისი სიმაღლე, შემდეგ შემოატანინეთ წლების რაოდენობა, მიღებული ინფორმაცია შეინახეთ ცვლადში და გამოუთვალეთ მომხმარებელს სავაურდო სიმაღლე იმ წლების შემდეგ რაც მან შემოიტანა თუ დაუშვათ ყოველ წელს სიმაღლე იზრდება 0.5-ით

your_height=input("your height: ")
your_age=input("your age: ")

print(float(your_height))
print(int(your_age))
height_then= your_height + (your_age * 0.5)
print(height_then)