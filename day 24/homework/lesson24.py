#მომხმარებელს შემოატანინეთ სიტყვა, შემდეგ if-ით შეამოწმეთ ეს სიტყვა თუ თავისი თავის ტოლია როდესაც შემოაბრუნებთ (slicing-ის დახმარებით), თუ ასეა დაბეჭდეთ რომ განსაკუთრებული (ასეთ სიტყვებს palindrome ჰქვია) სიტყვაა, სხვა შემთხვევაში კი დაბეჭდეთ რომ ჩვეულებრივი სიტყვაა.
word = input("Enter your word")
if word == word[::-1]:
    print("This is Palindrome")
else:
    print("This is normal")

#3) შექმენით სიტყვების სია, შემდეგ მის შემობრუნებულ ვერსიას გადაუარეთ for ციკლით, დაბეჭდეთ ყოველი მეორე ელემენტი (რომ გაიგოთ ყოველი მეორე აიღეთ ცვლადი რომელიც თავიდან 0 იქნება, ყოველ გამეორებაზე კი გაზრდით ერთით და შეამოწმეთ ლუწია თუ კენტი)

words = ["apple", "banana", "strawberry", "blueberry", "kiwi", "grape", "pineapple", "watermelon"]

reversed_words = words[::-1]

index = 0

for word in reversed_words:
    if index % 2 == 0:
        print(word)
    index += 1

#4) მომხმარებელს შემოატანინეთ სიტყვა და დაბეჭდეთ ის შებრუნებულად
word = input("input word:")

reverse = word[::-1]

print("reversed word:",reverse)



#5) შექმენით ცვლადი რომელშიც შეინახავთ თქვენთვის სასურველ string-ს, უნდა იყოს მინიმუმ 20 სიმბოლო, შემდეგ slicing-ის საშვალებით დაბეჭდეთ ეს string ხუთგვარად შემდეგი პირობებით:

text = "This is example of string"

print("First 5:", text[:5])

print("Last 4:", text[-4:])

print("4-10 symbols:", text[3:10])

print("Reversed:", text[::-1])

print("2nd symbols:", text[::2])