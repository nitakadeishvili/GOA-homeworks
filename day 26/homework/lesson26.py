#დაწერეთ პროგრამა, რომელიც ითხოვს ორ რიცხვს მომხმარებლისგან. შემოაყვანინეთ მომხმარებელს დაწყების და დასრულების რიცხვი. თუ მეორე რიცხვი ნაკლებია პირველზე, გამოუტანეთ შეტყობინება: არასწორი შუალედი. სხვა შემთხვევაში დაბეჭდეთ ყველა რიცხვი მოცემულ შუალედში ჩათვლით და იპოვეთ ამ რიცხვების ჯამი. გამოიყენეთ for ციკლი, if-else პირობა, input ფუნქცია, და int ტიპში გადაყვანა

start = int(input("Input number: "))
end = int(input("Input last number: "))

if end < start:
    print("არასწორი შუალედი")
else:
    total = 0
    print("რიცხვები მოცემულ შუალედში:")
    for num in range(start, end + 1):
        print(num)
        total += num
    print("რიცხვების ჯამი:", total)

#შექმენით პროგრამა რომელშიც გექნებათ ხილის სია კალათა (list), შემდეგ მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი (input), დაადეკლარირეთ ცვლადი რომელიც დაადგენს არის თუ არა ხილი კალათაში (variable) fruit_in_basket რომლის მნიშვნელობა თავიდან იქნება False, for ციკლის საშვალებით (for loop) განიხილეთ კალათა და პირობითი განცხადების საშვალებით (if-else) შეადარეთ მომხარებლის საყვარელ ხილს, თუ ისინი ტოლი იქნება fruit_in_basket ცვლადის მნიშვნელობა შეცვალეთ True boolean-ით, საბოლოოდ პირობითი განცხადების საშვალებით (if-else) შეამოწმეთ მომხმარებლის საყვარელი ხილი არის თუ არა კალათაში fruit_in_basket, თუ არის დაუბეჭდეთ 'Good choice' თუ არ არის 'Fruit not in basket'

basket = ["apple", "banana", "pear", "kiwi", "strawberry"]

favorite_fruit = input("შეიყვანეთ თქვენი საყვარელი ხილი: ")

fruit_in_basket = False

for fruit in basket:
    if fruit == favorite_fruit:
        fruit_in_basket = True

if fruit_in_basket:
    print("Good choice")
else:
    print("Fruit not in basket")

#ახსენით კომენტარებით როგორ მუშაობს: lower, upper, capitalize მეთოდები

text = "Nita Kadeishvili"

# lower() — გადაიყვანს ყველა ასოს პატარა ასოდ
print(text.lower())  # შედეგი: "nita kadeishvili"

# upper() — გადაიყვანს ყველა ასოს დიდ ასოდ
print(text.upper())  # შედეგი: "NITA KADEISHVILI"

# capitalize() — მხოლოდ პირველ სიმბოლოს აქცევს დიდად, დანარჩენს პატარად
print(text.capitalize())  # შედეგი: "Nita kadeishvili"

#შექმენით პროგრამა, რომელიც მოხმარებელს მოსთხოვს წინდადების შეყვანას, შემდეგ კი ამ წინადადებას სამჯერ დაბეჭდავს სხვადასხვა სახით: lower, upper, capitalize ფორმატებში

sentence = input("შეიყვანეთ წინადადება: ")

# დაბეჭდვა პატარა ასოებით
print("Lower", sentence.lower())

# დაბეჭდვა დიდი ასოებით
print("Upper", sentence.upper())

# მხოლოდ პირველი სიტყვა დიდით, დანარჩენი პატარად
print("Capitalize:", sentence.capitalize())


