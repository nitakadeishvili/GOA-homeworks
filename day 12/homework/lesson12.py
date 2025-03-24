#2) გააკეთეთ 5-5 მაგალითი თთოეულ შედარების ოპერატორზე (>, >=, <, <=, ==, !=), გვერდზე კომენტარის საშვალებით მიუთითეთ თუ რომელ boolean მნიშვნელობას გამოიტანას, აიღეთ მრავალფეროვანი კომბინაციები, შეეცადეთ გქონდეთ ყველა ვარიანტი

#>
print(5>4)#true
print(86>47)#true
print(54>63)#false
print(34>45)#false
print(23>39)#false
#<
print(19<23)#true
print(34<47)#true
print(89<12)#false
print(23<12)#false
print(62<54)#false
#<=
print(5<=5)#true
print(23<=17)#false
print(54<=47)#false
print(84<=12)#false
print(1<=1)#true
#>=
print(23>=23)#true
print(88>=47)#true
print(57>=63)#false
print(32>=45)#false
print(90>=93)#false
#==
print(5==5)#true
print(87==34)#false
print(322==243)#false
print(545==434)#false
print(555==555)#true
#!=
print(343!=233)#true
print(343!=343)#false
print(845!=845)#false
print(3434!=3434)#false
print(232!=432) #true

#3) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ შედარების ოპერაციათა შედეგებს, შედარების ოპერაციას გვერდზე კომენტარის საშვალებით მიუწერეთ მისი შედეგი (boolean მნიშვნელობა) და ახსენით რა განსხვავებაა ოპერატორსა და ოპერაციას შორის

#ოპერატორი არის სიმბოლო ან სიტყვა, რომელიც ასრულებს გარკვეულ მოქმედებას ერთზე ან მეტ მონაცემზე ხოლო ოპერაცია არის პროცესი, რომელიც სრულდება ოპერატორის გამოყენებით.

variable1=345>23 #true
variable2=23<20 #false
variable3=6543>=65 #true
variable4=3434<=34 #false
variable5=55==55 #true



#4) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები

age = 17
is_student = True
result1 = age < 18 or is_student  

temperature = 35
cloudy = False
result2 = temperature > 30 and not cloudy 

age = 22
adult = True
result3 = age > 18 and adult

year = 3
score = 85
result4 = (year == 3) and score > 80 

today="Thursday"
weekend= False
result5= today != "Saturday" 