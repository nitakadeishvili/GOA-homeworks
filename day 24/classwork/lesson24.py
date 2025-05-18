#1) შექმენით სია რომელშიც ჩამოწერეთ თქვენთვის სასურველი ელემენტები, მინიმუმ 10
Brands=["Chanel","Dior","Cartier","Louis Vuitton","Yves Saint Laurent","Hermes","Burberry","Prada","VERSACE","GUCCI",]
#გამოიტანეთ სიაში არსებული მესამე ელემენტი
print(Brands(3))
#ჩაანაცვლეთ სიაში არსებული პირველი ელემენტი
Brands[0]="Tifanny & Co"
#დაბეჭდეთ 2-დან მე-5 ელემენტამდე
print(Brands[2:5])
#დაბეჭდეთ მეორე ელემენტიდან ყველა ელემენტი
print(Brands[2:])
#დაბეჭდეთ მეხუთე ელემენტამდე ყვეალფერი
print(Brands[:5])
#დაბეჭდეთ სია შემობრუნებულად
print(Brands[::-1])

# შექმენით სია რომელშიც ჩამოწერთ ისტორული ეპოქები, უნდა გქონდეთ მინიმუმ 5 ეპოქა. უარყოფითი ინდექსების საშვალებით გამოიტანეთ indexing და slicing მეთოდის საშვალებით ელემენტები
Historical_eras=["Bronze Age","Iron Age","Classical Antiquity","Middle Ages","Renaissance","Early Modern Period","Modern Period"]
#ბოლო სამი ელემენტი
print(Historical_eras[-3:])
#ბოლო ელემენტი
print(Historical_eras[-1:])
#მეორე ელემენტიდან ყველაფერი
print(Historical_eras[-2:])
#მესამე ელემენტამდე ყველაა ეპოქა
print(Historical_eras[:-3])


