#2) დაწერეთ რა არის ფუნქცია, რისთვის ვიყენებთ, რამდენი ტიპის არსებობს, რა არის პარამეტრები, არგუმენტები და დაბრუნება (return)
#ეს არის კოდი, რომელსაც შეუძლია კონკრეტული ამოცანის შესრულება და მისი ბევრჯერ გამოყენება.
#ვიყენებთ - კოდის organization-ისთვის,ხელმეორედ გამოყენებისთვის,კოდის გადახარისხებისთვის (reuse) და მარტივად მართვისთვის.
#ტიპები - Built-in functions. User-defined functions.
#პარამეტრები — ფუნქციის გამოცხადების დროს მითითებული ცვლადები, რომლებიც ფუნქციის "მონაცემების მიღების" გზა არიან.
#არგუმენტები — რეალურად გადაცემული მნიშვნელობები ფუნქციის გამოძახებისას.
#Return — ფუნქციის შედეგის დაბრუნების გზა. ფუნქცია რაღაც შედეგს გამოიტანს, რომელსაც შემდეგ შეგვიძლია სხვა კოდში გამოვიყენოთ.

#3) შექმენით ფუნქცია greetings, რომელიც არ მიიღებს არგუმენტებს და დაბეჭდავს მისალმების ტექსტს.
def greetings():
    print("Hello! Welcome to the program.")
#4) შექმენით ფუნქცია რომელიც მიიღებს რიცხვს (int) და სიტყვას (string) პარამეტრებად, ფუნქციამ მიღებული სიტყვა უნდა დაბეჭდოს იმდენჯერ რამდენიც არის რიცხვის არგუმენტი.
def repeat_word(times, word):
    for _ in range(times):
        print(word)

#5) შექმენით ფუნქცია რომელიც მიიღებს x და y კორდინატს, შემდეგ კი გადაცემული კორდინატების ადგილას დახაზავს კვადრატს, დავალების შესასრულებლად გამოიყენეთ მოდული: from turtle import *.
from turtle import *

def draw_square_at(x, y):
    penup()
    goto(x, y)
    pendown()
    for _ in range(4):
        forward(100)
        right(90)

draw_square_at(50, 50)
done()


#6) შექმენით ფუნქცია calculate_area, რომელსაც გადაეცემა ორი რიცხვი — სიგრძე და სიგანე. ფუნქციამ უნდა გამოთვალოს მართკუთხედის ფართობი და return-ით დააბრუნოს შედეგი ისე, რომ შემდეგ მისი გამოყენება შეიძლებოდეს სხვა ადგილას, მაგალითად, დაბეჭდვაში.

def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 3)
print("Area:", result)


#7) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს რიცხვს და დააბრუნებს მის ფაქტორიალს. n რიცხვის ფაქტოირალი არის ყველა მთელი დადებითი რიცხვის ნამრავლი 1-იდან n-ის ჩათვლით

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))
