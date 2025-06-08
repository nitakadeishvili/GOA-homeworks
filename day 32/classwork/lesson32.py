#1) შექმენით ფუნქცია, greeting რომელიც დააბრუნებს მესიჯს "Hello world". ეს ფუნქია გამოიძახეთ და შეინახეთ ცვლადში, შემდეგ დაბეჭდეთ ცვლადის მნიშვნელობა. საბოლოოდ თქვენი სიტყვებით ახსნით რა განსხვავებაა return-სა და print-ს შორის

def say_hello():
    return "გამარჯობა"
print(say_hello)

#printს გამოაქვს მნიშვნელობა
#return ფუნქციის ნახვლად სხვა მნიშვნელობას ჩასვავს მნიშვნელობას 

#2) შექმენით ფუნქცია, რომელიც მიიღებს კვადრატის სიგრძეს თუ სიგრძე არ გადმოგეცემათ ივარაუდოთ რომ ის 10-ია, გამოთვლის მის ფართობსა და პერიმეტრს და დააბრუნებს ერთად. ეს ფუნქცია გამოიძახეთ მინიმუმ 2-ჯერ ერთხელ გადაეცით თქვენთვის სასურველი სიგრძე, მეორედ კი არაფერი გადასცეთ, ორივე შემთხვევაში შეინახეთ ფუნქციის დაბრუნებული მნიშვნელობები ცვლადებში: square_area1, square_perimeter1, square_area2, square_perimeter2

def square(length=10):
    area = length ** 2
    perimeter = 4 * length
    return area, perimeter


area1, perim1 = square()

area2, perim2 = square(6)

print("Call 1 - Area:", area1, "Perimeter:", perim1)
print("Call 2 - Area:", area2, "Perimeter:", perim2)
