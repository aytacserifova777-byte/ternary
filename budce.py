
gelir = float(input("Aylıq gəlirinizi daxil edin: "))
xerc = float(input("Aylıq xərclərinizi daxil edin: "))

if gelir < 0 or xerc < 0:
    print("Xəta! Mənfi məbləğ daxil etmək olmaz.")

else:
    qalan = gelir - xerc

    if xerc > gelir:
        print("Büdcə kəsiri var")

    elif gelir == 0:
        print("Gəlir 0 olduğu üçün qənaət faizi hesablana bilməz.")

    elif xerc >= gelir * 0.80:
        print("Xərclərə diqqət et")

    elif xerc >= gelir * 0.50:
        print("Büdcə normaldır")

    else:
        print("Yaxşı qənaət edirsiniz")

    print("Ayın sonunda qalan pul:", qalan, "AZN")

    if gelir > 0:
        faiz = (qalan / gelir) * 100
        print("Qənaət faizi:", faiz, "%")
    else:
        print("Qənaət faizi hesablana bilməz.")
