#ფუნქცია არის პატარა პროგრამა, რომელსაც შენი კოდის შიგნით აკეთებ იმისთვის, რომ რაღაც საქმე გააკეთოს. როცა გინდა, ეს საქმე გააკეთოს — უბრალოდ ფუნქციას "იძახებ".

print() #— ბეჭდავს ეკრანზე

x = "5"
print(int(x))   # 5 (გადაქცევა Integerად(რიცხვად))

#2) შექმენით ერთი ცვლადი რომელშიც შეინახავთ თქვენს სრულ სახელსა და გვარს, ამ სიტყბების პირველი ასოები უნდა იყოს დიდი. შემდეგ for ციკლის მეშვეობით გადაურეთ თქვენს სრულ სახელს და შეამოწმეთ სახელის და გვარის პირველი ასოები თუ დიდი, მათთან აიღეთ კიდევ 3 სხვა დიდი სიმბოლო თქვენი სრული სახელიდან და შეამოწმეთ ასეთი თუ გხვდებათ თქვენი სახელიდან, თუ ასეა მაშინ result ცვლადს (რომელსაც შექმნით for ციკლის გამოყენებამდე და შეინახავთ ცარიელ სტრინგს) დაამატეთ ამ ასოების პატარა ვერსია მაგ: (თუ char == "A": result += "a" 

name = "Nita Kadeishvili"
result = ""
for symbol in name:
    if symbol == "N":
       result += "n"
    elif symbol == "I":
       result += "i"
    elif symbol == "T":
       result +="t"
    elif symbol == "A":
       result += "a"
    elif symbol == "K":
       result += "k"

print(result)