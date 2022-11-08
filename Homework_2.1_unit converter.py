#Unit converter + loop

print("Pozdrav! Ovdje možeš preračunati kilometre u milje.")
uvjet = "DA"

while uvjet != "NE":

    udaljenost_km = int(input("Unesi udaljenost u kilometrima: "))

    udaljenost_mi = (udaljenost_km) * 0.62
    print("Udaljenost u miljama iznosi: " + str(udaljenost_mi))

    uvjet = input("Želiš li novi izračun? Unesi DA ili NE: ")

print("Kraj programa")



