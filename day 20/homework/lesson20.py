#2) შექმენით პროგრამა რომელიც მომხმარებლისგან მიიღებს რიცხვს, შემდეგ დაადგენს დადებითია, უარყოფითი თუ ნული if-elif-else ის საშვალებით, თუ რიცხვი დადებითია შეამოწმეთ არის თუ არა ლუწი თუ არის დაბეჭდეთ "The number is positive and even." ხოლო სხვა შემთხვევაში დაბეჭდეთ "The number is positive and odd."
number = int(input("Enter a number: "))

if number > 0:
    
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#3) მომხმარებელს იქამდე შეეკითხეთ რიცხვები სანამ უარყოფით რიცხვს არ შემოიყვანს, while ციკლისა და input ინსტრუქციის საშვალებით, ასევე პირობითი განცხადებების დადებითობა/უარყოფითობის შესამოწმებლად, საბოლოოდ დაბეჭდეთ ყველა მიღებული დადებითი რიცხვის ჯამი
sum_positive = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
       
        break
    else:
        
        sum_positive += number


print("The sum of all positive numbers is:", sum_positive)

#შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ უარყოფითს არ შეიყვანს. დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების რაოდენობა გამოიყენეთ პირობითი განცხადებები
even_count = 0
odd_count = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        
        break
    else:
        
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1


print("Number of even numbers entered:", even_count)
print("Number of odd numbers entered:", odd_count)

#მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები
correct_pin = "1234"


attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")
    
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect PIN. Try again.")
        else:
            print("Access Denied")

#მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო

total = 0
count = 0

while True:
    number = int(input("Enter a number (-1 to stop): "))
    
    if number == -1:
        
        break
    else:
        total += number
        count += 1


if count > 0:
    average = total / count
    print("The average of the entered numbers is:", average)
else:
    print("No numbers were entered.")

# მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)

sentence = input("Enter a sentence: ")


vowel_count = 0
consonant_count = 0


vowels = "aeiouAEIOU"

for char in sentence:
    if char.isalpha():  
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1


print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

#შექმენი სია `fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]` და დაბეჭდე მესამე ელემენტი

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]


print(fruits[2])

#შექმენი სია `numbers = [10, 20, 30, 40, 50]`, შეცვალე მეორე ელემენტი 25-ით და დაბეჭდე განახლებული სია

numbers = [10, 20, 30, 40, 50]


numbers[1] = 25


print(numbers)

# მომხმარებელს შეაყვანინე ინდექსი (`0`-დან `4`-მდე) და დაბეჭდე შესაბამისი ელემენტი სიიდან `colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

index = int(input("Enter an index (0 to 4): "))


if 0 <= index <= 4:
    print("The color at index", index, "is", colors[index])
else:
    print("Invalid index. Please enter a number between 0 and 4.")

#შექმენი სია `animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]`, შეცვალე ბოლო ელემენტი "გემი"-თ და დაბეჭდე სია

animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]

animals[-1] = "გემი"

print(animals)

#მომხმარებელს შეაყვანინე ინდექსი და ახალი ფერი, შეცვალე ამ ინდექსზე არსებული ფერი სიაში `colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]` და დაბეჭდე განახლებული სია

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

index = int(input("Enter the index (0 to 3): "))
new_color = input("Enter the new color: ")

if 0 <= index < len(colors):
    colors[index] = new_color
    print("Updated list of colors:", colors)
else:
    print("Invalid index. Please enter an index between 0 and 3.")


