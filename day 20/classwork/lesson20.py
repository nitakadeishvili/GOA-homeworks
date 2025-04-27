#2) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ თუ ეს რიცხვი დადებითია დაბეჭდეთ ეს და კიდევ შეამოწმეთ ლუწია თუ კენტი, ხოლო თუ არაა დადებითი მხოლოდ დაბეჭდეთ რომ უარყოფითია

num=int(input("enter your number:"))

if num>0:
    print("number positive")
    if num % 2 == 0:
       print("even")
    else:
        print("odd")
else:
    print("number is negative")

#3) შექმენით ბოსტენულის სია და დაბეჭდეთ მთლიანად, შემდეგ კი ამ სიაში ელემენტების პოზიციების საშვალებით დაბეჭდეთ თითეული სიის ელემენტი ცალ-ცალკე

Vegetables = ["cucumber","carrot","pepper","cabbage"]
print(Vegetables[0])
print(Vegetables[1])
print(Vegetables[2])
print(Vegetables[3])