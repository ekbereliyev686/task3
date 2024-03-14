# Tapşırıq 1: 

# İstifadəçidən boyu ilə bağlı məlumat alan və ona tövsiyə olunan ideal cəki aralığını göstərən proqram hazırlayın.    
# 
# Beden kitle indeksi sonucuna göre:

# 19’un altında ise aşırı zayıflık
# 19 – 25 arasında ise ideal (normal) kilo
# 25 – 30 arası ise hafif şişman
# 30 – 35 arası ise şişman
# 35 ‘in üzerinde ise obez grubunda kabul edilir. 


height=int(input("Boyunuzu daxil edin :"))
weight=int(input("Cekisinizi daxil edin :"))
bki=(weight/(height/100)**2)
if bki<19:
    print(f'Siz cok zeifsiniz ideal cekiniz {int(19*(height/100)**2)} kq olmalidir')
elif bki>19 and bki<=25:
    print(f'Siz  normalsiz ideal cekiniz {int(19*(height/100)**2)} kq olmalidir')
elif bki >25 and bki <=30:
    print(f'Siz biraz kilolusunuz ideal cekiniz {int(25*(height/100)**2)} kq olmalidir')
elif bki> 30 and bki<35:
    print(f'Siz kilolosunuz ideal cekiniz {int(30*(height/100)**2)} kq olmalidir')
else:
    print(f'Siz obezsiniz ideal cekiniz {(35*(height/100)**2)} kq olmalidir')


# Tapşırıq 2: 

# Tapşırıq: Onlayn mağaza üçün alış-veriş səbəti sistemini simulyasiya edən proqram hazırlayın. İstifadəçilərə səbətinə əşyalar əlavə etməyə, vergilər(18% ədv ümumi qiymetin üzərinə gəlməlidir) daxil olmaqla ümumi dəyəri hesablamağa kömək edir. əgər ümumi qiymət (ədv daxil) 50 azn dən çox olarsa istifadəciyə ən sonra 10 azn lik kupon qazandınız mesajını verin. əgər ümumi qiymət (ədv daxil) 100 azn dən çox olarsa istifadəciyə ən sonra 15 azn lik kupon qazandınız mesajını verin. İstifadəçi səbətə 5 dəfə məhsul əlavə edə bilər.

empty=[]
total=0
for i in range(5):
    product=input("Aldiginiz mehsulun adini daxil edin :")
    price=int(input("Aldiginiz mehsulun qiymetini daxil edin : "))
    total+=price
    
    basket={
        "product":product,
        "price":price,
        "total":total,
        
    }
    empty.append(basket)
print(empty)
sum=round(total/100*18+total)
vat=round(total/100*18)
print(f'Odemeli oldugunuz mebleb  {total}  ,Qazandiginiz EDV {vat}')
if sum>100:
    print("Hormetli musteri siz 100 azn kecdiyiniz ucun bizden 15 azn lik kupon qazandiniz ....TEBRIKLER.." )
elif sum>50:
    print("Hormetli musteri siz 50 azn kecdiyiniz ucun bizden 10 azn lik kupon qazandiniz ....TEBRIKLER.." )




# Tapşırıq 3: 

# Müştəriyə səyahətin ümumi dəyərini hesablamaq üçün nəqliyyat şirkətinə Python proqramı yazın. İstifadəçidən səyahət məsafəsini və nəqliyyat vasitəsinin növünü (məsələn, avtomobil, yük maşını, avtobus) daxil etməyi təklif edin. Verilən məsafəyə və nəqliyyat vasitəsinin növünə əsaslanaraq ümumi dəyəri hesablayın (avtomobillərin hər km üçün 0,50 dollar, yük maşınlarının hər km üçün 1,00 dollar, avtobusların hər km üçün qiyməti 2,00 dollar).

car_price=0.5
lorry_price=1
bus_price=2
transportation=int(input(""" Istifade etmek istediyiniz neqliyyati secin 

1.Avtomobil
2.Yuk masini
3.Avtobus

  :"""))
distance=int(input("Gedeceyiniz  mesafeni daxil edin :"))

if transportation==1:
    print(f"Seyahetin qiymeti {distance * car_price} dollar")
elif transportation==1:
    print(f"Seyahetin qiymeti {distance * lorry_price} dollar")
else:
    print(f"Seyahetin qiymeti {distance * bus_price} dollar")