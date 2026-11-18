
tecrube = float(input("İş təcrübəsini daxil edin: "))
bal = float(input("Müsahibə balını daxil edin: "))

if tecrube < 0 or bal < 0 or bal > 100:
    print("Xəta! Məlumatları düzgün daxil edin.")

else:
    if bal >= 90:
        print("Güclü namizəd")

    elif tecrube >= 2 and bal >= 70:
        print("Növbəti mərhələyə dəvət olunur")

    else:
        print("Namizəd uyğun deyil")

    status = "İlkin mərhələni keçdi" if (bal >= 90 or (tecrube >= 2 and bal >= 70)) else "İlkin mərhələni keçmədi"

    print("Status:", status)
