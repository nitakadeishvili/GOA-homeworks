#1) თითოეულ მეთოდზე: len, append, insert, pop, remove მეთოდებზე გააკეთეთ 3-3 მაგალითი. len ფუნქციაზე მოიყვანეთ string-ის მაგალითიც
list1 = [1, 2, 3]
print(len(list1))  

list2 = ['apple', 'banana', 'blueberry']
print(len(list2))  

list3 = []
print(len(list3))  

#stringის მაგალითი
text1 = "Hello"
print(len(text1))  

text2 = "Bonjour"
print(len(text2))  

text3 = ""
print(len(text3))  

#appendის მაგალითი
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  

numbers = [1, 2, 3]
numbers.append(4)
print(numbers) 

items = []
items.append('item1')
print(items)  

#insert 

names = ['David', 'Natia']
names.insert(1, 'Nita')
print(names)  

numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)  

letters = ['a', 'b', 'd']
letters.insert(2, 'c')
print(letters) 

#pop

colors = ['red', 'green', 'blue']
removed = colors.pop()
print(removed)     
print(colors)     

numbers = [1, 2, 3, 4]
removed = numbers.pop(1)
print(removed)    
print(numbers)    

fruits = ['apple', 'banana', 'bluerry']
removed = fruits.pop(0)
print(removed)     
print(fruits)     

#remove
letters = ['a', 'b', 'c', 'b']
letters.remove('b')
print(letters)  

fruits = ['apple', 'banana', 'blueberry']
fruits.remove('banana')
print(fruits)  

numbers = [1, 2, 3, 4, 2]
numbers.remove(2)
print(numbers)  

#2) შექმენით greet ფუნქცია რომელიც დაბეჭდავს ჯერ "Hello"-ს შემდეგ კი მის ქვემოთ "Welcome"-ს. ეს ფუნქცია 2-ჯერ გამოიძახეთ
def greet():
    print("Hello")
    print("Welcome")
greet()
greet()

#3) შექმენით ახალი new_greet ფუნქცია რომელსაც ექნება 2 პარამეტრი: first_name და last_name. ამ ფუნქციამ უნდა დაბეჭდოს შემდეგი ტექსტი: "Greetings [firstname] [lastname] ფუნქცია 2-ჯერ გამოიძახეთ და გადაეცით არგუმენტები. კომენტარებით ახსენით რა განსხვავებაა პარამაეტრებსა და არგუმენტებს შორის


def new_greet(first_name, last_name):
    print(f"Greetings {first_name} {last_name}")
new_greet("Nita", "Kadeishvili")
new_greet("Elene", "Tsulukidze")

