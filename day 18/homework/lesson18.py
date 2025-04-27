#for ციკლის საშვალებით დაბეჭდეთ რიცხვები 0-იდან 20-მდე, შეამოწმეთ თითოეული რიცხვი ლუწია თუ კენტი, თუ ლუწია დაბეჭდეთ "even" თუ კენტია დაბეჭდეთ odd და გვერდზე მიუწერეთ ეს რიცხვი თითოეულ შემთხვევაში
for i in range(21):
    if i % 2 == 0:
        print("even -", i)
    else:
        print("odd  -", i)

#while ციკლის საშვალებით დაბეჭდეთ რიცხვები 0-იდან 20-მდე, შეამოწმეთ თითოეული რიცხვი ლუწია თუ კენტი, თუ ლუწია დაბეჭდეთ "even" თუ კენტია დაბეჭდეთ odd და გვერდზე მიუწერეთ ეს რიცხვი თითოეულ შემთხვევაში

num = 0

while num <= 20:
    if num % 2 == 0:
        print("even -", num)
    else:
        print("odd  -", num)
    num += 1

#მომხმარებელს შემოატანინეთ სახელი და თუ ის თქვენს სახელს ემთხვევა დაბეჭდეთ "coincidence"

my_name = "nita"

user_name = input("შეიყვანე შენი სახელი: ")

if user_name == my_name:
    print("coincidence")
else:
    print("hello", user_name)

#მოხმარებელს შემოატანინეთ გამოცდის ქულა და შეინახეთ score ცვლადში ინტეჯერად, თუ ქულა მეტია 70-ზე დაუბეჭდეთ რომ გამოცდა გადალახა "passed" სხვა შემთხვევაში კი რომ ჩაიჭრა "failed"

score = int(input("შეიყვანე გამოცდის ქულა: "))

if score > 70:
    print("passed")
else:
    print("failed")

#მომხმარებელს შემოატანინეთ ქულა score და შეინახეთ ცვლადში, როგორც integer. შემდეგ, ქულის მიხედვით განსაზღვრეთ შეფასება (grade): A – თუ score მეტია 80-ზე B – თუ score მეტია 60-ზე C – თუ score მეტია 40-ზე D – თუ score მეტია 20-ზე F – თუ score 20-ზე ნაკლებია

score = int(input("შეიყვანე ქულა: "))

if score > 80:
    grade = "A"
elif score > 60:
    grade = "B"
elif score > 40:
    grade = "C"
elif score > 20:
    grade = "D"
else:
    grade = "F"

print("შეფასება:", grade)


