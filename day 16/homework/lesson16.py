#2) for ციკლის საშვალებით გამოთვალეთ რიცხვების ჯამი 20-იდან 40-მდე
sum = 0
for i in range (20,41):
    sum += i
print("ჯამი 20-დან 40-მდეა", sum)

#3) for ციკლის საშვალებით გამოთვალეთ 10-იდან 50-ის ჩათვლით ყველა რიცხვის ჯამი

sum_all = 0

for number in range(10, 51):  # 51 იმიტომ, რომ ზედა ზღვარი range-ში არ შედის
    sum_all += number

print("10-დან 50-ის ჩათვლით რიცხვების ჯამია:", sum_all)

#4) for ციკლის საშვალებით გამოთვალეთ 20-იდან 100-მდე ყველა ლუწი რიცხვის ჯამი, საბოლოოდ დაბეჭდეთ შედეგი

sum_even = 0

for number in range(20, 101, 2):
    sum_even += number

print("ლუწი რიცხვების ჯამი 20-დან 100-მდე არის:", sum_even)

#for ციკლის საშვალებით გამოთვალეთ 7-ის ფაქტორიალი. რიცხვის ფაქტორიალი არის ყველა რიცხვის ნამრავლი ამ რიცხვიდან 1-მდე

factorial = 1

for number in range(1, 8):  
    factorial *= number

print("7-ის ფაქტორიალია:", factorial)

#while ციკლის საშვალებით დაბეჭდეთ რიცხვები 0-იდან 20-მდე

number = 0

while number <= 20:
    print(number)
    number += 1

#while ციკლის საშვალებით დაბეჭდეთ რიცხვები 10-იდან 30-ის ჩათვლით

number = 10

while number <=30:
    print(number)
    number += 1

#while ციკლის საშვალებით დაბეჭდეთ რიცხვები 15-იდან 80-მდე

number = 15

while number <=80:
    print(number)
    number += 1

#while ციკლის საშვალებით გამოიტანეთ რიცხვები 50-იდან 0-ჩათვლით

number = 50

while number >= 0:
    print(number)
    number -= 1

#while ციკლის საშვალებით გამოიტანეთ ყოველი მესამე რიცხვი 0-იდან 50-ის ჩათვლით

number = 0

while number <= 50:
    print(number)
    number += 3

#while ციკლის საშვალებით გამოიტანეთ ლუწი რიცხვები 0-იდან 50-ის ჩათვლით

number = 0

while number <= 50:
    print(number)
    number += 2

#while ციკლის საშვალებით გამოიტანეთ ყოველი მესამე რიცხვი 100-იდან 20-ის ჩათვლით

number = 100

while number >= 20:
    print(number)
    number -= 3

#შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს სანამ ის არ შემოიყვანს goabest123-ს

password = "goabest123"

while input("Enter password: ") != password:
    print("Your password is incorrect, please try again.")

print("Your password is correct!")

#შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა

PIN = 1234
user_input = int (input("Enter password: "))
attempt = 0

while PIN != user_input:
    input("enter password:")
    attempt += 1

print("your attempts: ", attempt)

