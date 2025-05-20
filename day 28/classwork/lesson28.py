#1) პირდაპირ გამოიყენეთ string-ებზე lower, upper, capitalize, მეთოდები კომენტარებით დაწერეთ რა არის მეთოდი რით განსხვავდება ჩვეულებრივი ფუნქციისგან, რა არის dot ნოტაცია. ასევე გააკეთეთ 3 მაგალითი find მეთოდზე, აუცილებლად უნდა იყოს 3 შემთხვევა: error, -1, რაიმე პოზიციას (index)

#ობიექტზე მეთოდის გამოსაძახებლად
"Nita Kadeishvili".upper()  

#გამოაქვს მთელი სტრინგი პატარა ასოებით
text = "Nita Kadeishvili"
print(text.lower())  

#გამოაქვს მთელი სტრინი დიდი ასოებით
text = "Nita Kadeishvili"
print(text.upper())  

#პირველი ასო გამოაქვს დიდი ასოთი
text = "nita kadeishvili"
print(text.capitalize())  

#find() მეთოდი აბრუნებს სტრინგში ძებნილი ქვეწრების პირველივე მოძებნილ პოზიციას (index). თუ ვერ მოიძებნა — აბრუნებს -1, ხოლო თუ არგუმენტი არასწორია ხდება error.


#ქვეწერის პოზიციის დაბრუნება (index)
text = "Dancing"
print(text.find("g")) 

#ვერ მოიძებნა — აბრუნებს -1
text = "Dance"
print(text.find("z"))  

#error
text = "Example"
print(text.find(5))


