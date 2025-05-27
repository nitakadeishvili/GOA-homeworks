
#2) შემოიტანეთ სიტყვა input-ით და დაბეჭდეთ ის პატარა ასოებით
word = input("Enter a word: ")

print("პატარა ასოებით", word.lower())

#3) შემოიტანეთ ორი სიტყვა და შეადარეთ (print(word1 == word2) ისე, რომ არ ჰქონდეს მნიშვნელობა ასოების სიდიდეს (გამოიყენეთ lower)
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

print(word1.lower() == word2.lower())

#4) მოცემული სიაა: ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]. ყველა ელემენტი გადააკეთეთ პატარა ასოებად და დაბეჭდეთ (გამოიყენეთ for ციკლი)
countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for country in countries:
    print(country.lower())

#5) შემოიტანეთ სიტყვა input-ით და დაბეჭდეთ დიდი ასოებით
word = input("Enter a word: ")
print("Uppercase:", word.upper())

#6) მოცემული სიაა: ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]. ყველა ქვეყანა გადააკეთეთ დიდი ასოებად და დაბეჭდეთ
countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for country in countries:
    print(country.upper())
#7) შემოიტანეთ სიტყვა input-ით და შეამოწმეთ, არის თუ არა ის მთლიანად დიდი ასოებით
word = input("Enter a word: ")

if word.isupper():
    print("The word is in all uppercase letters.")
else:
    print("The word is not in all uppercase letters.")

#8) შემოიტანეთ წინადადება input-ით და გამოიყენეთ capitalize ისე, რომ მხოლოდ პირველი ასო დარჩეს დიდი
sentence = input("Enter sentence: ")
print(sentence.capitalize())

#9) მოცემული სტრინგია "gEoRGia". გადააკეთეთ ისე, რომ მხოლოდ პირველი ასო იყოს დიდი, დანარჩენი კი პატარა
word = "gEoRGia"
fixed_word = word.capitalize()
print(fixed_word)

#10) მოცემული სიაა: ["georgia", "aRMENIA", "greeCE"]. ყველა ელემენტს ჯერ გაუკეთეთ lower, შემდეგ capitalize და დაბეჭდეთ
countries = ["georgia", "aRMENIA", "greeCE"]

for country in countries:
    fixed_country = country.lower().capitalize()
    print(fixed_country)

#11) შემოიტანეთ სიტყვა input-ით და მოძებნეთ ასო a-ს პირველი პოზიცია
word = input("Enter a word: ")
position = word.find('a')

print("a position", position)

#12) მოცემული სტრინგია "I visited Georgia, Armenia and Greece". მოძებნეთ Armenia და დაბეჭდეთ მისი პოზიცია
text = "I visited Georgia, Armenia and Greece"
position = text.find("Armenia")

print("Armenia-ს position is:", position)

#13) შექმენით სტრინგი და შემოიტანეთ საძიებელი სიტყვა input-ით. თუ სიტყვა მოიძებნება find-ით, დაბეჭდეთ პოზიცია, სხვა შემთხვევაში კი დაბეჭდეთ word not found
text = "I visited Georgia, Armenia and Greece"
search_word = input("Enter search word: ")

position = text.find(search_word)

if position != -1:
    print("Words position:", position)
else:
    print("word not found")