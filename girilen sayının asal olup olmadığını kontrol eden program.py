from operator import truediv
import turtle


sayi=int(input("lütfen sayı giriniz: "))
prime=True

for i in range(2,sayi):
    if   sayi%i==0:
        prime=False
        break
if prime==False:
    print(f"{sayi} sayısı asal değildir")
else:
    print(f"{sayi} sayısı asaldır")



    

    


