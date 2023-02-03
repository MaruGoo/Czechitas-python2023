sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

#for soucastka in sklad:
#    print(soucastka)

kod_soucastky = input("Zadejte prosim kod soucastky: ")

if kod_soucastky in sklad:
    mnozstvi_soucastek = int(input("Zadejte prosim pozadovane mnozstvi soucastek: "))
    print(f"pozadovany kod_soucastky={kod_soucastky}, pozadovane mnozstvi_soucastek={mnozstvi_soucastek}, pocet soucastek typu {kod_soucastky} na sklade je {sklad[kod_soucastky]}")
    if mnozstvi_soucastek <= sklad[kod_soucastky]:
        print("Nakup byl uspesny")
        sklad[kod_soucastky] = sklad[kod_soucastky] - (mnozstvi_soucastek)
        print(f"Zbyva {sklad[kod_soucastky]} soucastek")
    else:
        print("Lze prodat pouze omezené množství kusů.")
        sklad.pop(kod_soucastky)
else:
    print("Polozka není v nabídce")




