#1) შექმენით sum ცვლადი რომელშიც შეინახავთ 1-იდან 20-მდე რიცხვების ჯამს, ამისთვის გამოიყენეთ for ციკლი და range ინსტრუქცია, საბოლოოდ ერთხელ დაბეჭედეთ ჯამი

sum = 0
for number in range (1,20):
    sum += number
print(sum)

#2) მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი პირველი რიცხვიდან მეორეს ჩათვლით არსებული ყველა რიცხვი დაბეჭდეთ

number1= int(input("enter first number: "))
number2=int(input("enter second number: "))

for number in range(number1,number2 + 1):
    print(number)

#3) შექმენით პროგრამა რომელიც მოხმარებელს შეეკითხება პაროლს სანამ სწორად არ ჩაწერს
password = "goa123"

while input ("enter password: ") != password:
    print("your password is wrong,try again")
print("your password is wrong")