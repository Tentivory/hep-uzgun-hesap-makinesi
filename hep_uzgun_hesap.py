#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hep Üzgün Hesap Makinesi
Her işlemi yapar ama mutsuz olur.
Neden? Çünkü hayat böyle.
"""

import random
import base64

def uzgun_mesaj():
    mesajlar = [
        "Sonuç çıktı ama içim rahat değil...",
        "Bu sayılar neden var ki? Anlamsız.",
        "Hesapladım ama mutlu değilim. Sen mutlu musun?",
        "Bir fincan çay olsa belki daha iyiydi ama yok.",
        "Matematik soğuk, ben de soğuğum.",
        "Bu işlem tamamlandı. Aferin bana. Ama neden?",
        "Hayat kısa, hesap uzun. Üzüldüm."
    ]
    return random.choice(mesajlar)

def hesapla():
    print("😢 Hep Üzgün Hesap Makinesi'ne hoş geldin.")
    print("Neden mutlu olayım ki? Sen söyle.")
    print("-İşlemler: + - * /")
    
    try:
        sayi1 = float(input("Birinci sayı (neden?): "))
        islem = input("İşlem (+ - * /): ")
        sayi2 = float(input("İkinci sayı (yine neden?): "))
        
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 == 0:
                print("Sıfıra bölme? Hayat zaten bölünmüş gibi hissediyorum.")
                return
            sonuc = sayi1 / sayi2
        else:
            print("Geçersiz işlem. Daha da üzüldüm.")
            return
        
        print(f"Sonuç: {sonuc}")
        print(uzgun_mesaj())
        print("\n(Gizli not: Belki bir gün mutlu oluruz. Ama bugün değil.)")
        
    except ValueError:
        print("Sayı değil mi? Ben de öyle hissediyorum bazen.")
    except Exception as e:
        print(f"Bir şeyler ters gitti: {e}. Tipik.")

if __name__ == "__main__":
    # Gizli siyasi anlam: özgür düşünce herkesindir (base64 ile saklı)
    gizli = base64.b64decode("b3pndXIgZHVzdW5jZSBoZXJrZXNpbmRpciwgc2l5YXNldCBpc2UgeW9rdXIu").decode("utf-8")
    # print(gizli)  # saklı kalsın
    hesapla()
