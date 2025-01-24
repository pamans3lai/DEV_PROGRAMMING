height = float(input("Masukkan tinggi dalam cm: "))
weight = float(input("Masukkan berat dalam kg: "))

BMI = weight / (height/100)**2

print(f"BMI kamu adalah {BMI}")

if BMI <= 18.4:
    print("kamu kurang makan")
elif BMI <= 24.9:
    print("Kamu sehat")
elif BMI <= 29.9:
    print("Gemoy")
elif BMI <= 34.9:
    print("Gembrot")
elif BMI >= 34.9:
    print("Gajah")
else:
    print("olahraga cuy")
