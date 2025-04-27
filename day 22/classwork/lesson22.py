#1) შექმენით სია რომელშიც ჩამოწერეთ მინიმუმ 10 პროგრამირების ენას, ის ენა რომელიც ყველაზე ნაკელბად გსურთ რომ შეისწავლოთ ჩაანაცვლეთ ახალი ენით რომლის სწავლასაც ისურვებდით

languages=["python","java","C","C++","C#","Swift","Rust","Applescript","APT","Alef"]

languages[6]="Kotlin"

print(languages)

#2) შექმენით ცივი სასმელების სია აქედან ერთ-ერთი ელემენტი უნდა ეწეროს ცვლადის სახით, შემდეგ მომხმარებელს შემოტანინეთ 1 ცივი სასმელი რომელსაც დაამატებთ თქვენს მაცივარში. შემდეგ მომხარებელს უნდა შემოატანინოთ არჩევანი ამ სასმელებიდან და სიიდან ელემენტის წამოღების indexing method-ის საშვალებით გამოუტანეთ ეს სასმელი. შექმენით ცვლადი რომელშიც შეინახავთ თქვენს სახელს, გამოიტანეთ ამ სტრინგიდან თქვენთვის სასურველი 3 სიმბოლო

persons_drink=input("enter your fav drink:")
drinker= "pepsi"
drinks=["Coca-Cola","Fanta","Natakhtaris limonati",drinker,persons_drink]
choice=int(input("enter your choice: "))

print(drinks[choice])

#3) შექმენით სია რომელშიც ჩამოწერეთ სპორტის სახეობებს (მინიმუმ 10 სახეობა), აქედან slicing-ის გამოყენებით ამოჭერით და დაბეჭდეთ:
1-5
3-8
-2-0
4-0
#შემობრუნებული სია

sports=["basketball","football","tennis","swimming","volleyball","cricket","hockey","baseball","table tennis","baseball"]
print(sports[0:5])
print(sports[3:8])
print(sports[-2:0])
print(sports[4:0])