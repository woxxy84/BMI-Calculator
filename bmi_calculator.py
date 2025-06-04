# bmi_calculator.py

def main():
    print("THIS PROGRAM WILL TELL YOUR BMI")

    mass = int(input("ENTER YOUR MASS (kg): "))
    height_cm = int(input("ENTER YOUR HEIGHT (cm): "))

    height_m = height_cm / 100
    bmi = mass / (height_m ** 2)

    print(f"Your BMI is {bmi:.2f}")

if __name__ == "__main__":
    main()
