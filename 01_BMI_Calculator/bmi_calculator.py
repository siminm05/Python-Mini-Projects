'''
BMI Calculator
'''

def main():
    while True:
        user_weight = get_weight()
        if user_weight is None:
            return

        user_height = get_height()
        if user_height is None:
            return

        user_bmi = calculate_bmi(user_weight, user_height)
        user_result = get_bmi_result(user_bmi)

        # print("Your BMI is", user_bmi, "! You are", user_result, ".")
        print("Your BMI is ", user_bmi, "! You are ", user_result, ".", sep="")
        # print(f"Your BMI is {user_bmi}! You are {user_result}.")

        new_bmi = input("Would you like to calculate another BMI? (yes/no): ").lower().strip()

        if new_bmi == 'yes':
            continue
        elif new_bmi == 'no':
            print("Thank you!")
            break
        else:
            print("Invalid input")
            break

def get_weight():
    weight_unit = input("Enter weight unit (kg/lb): ").lower().strip()
    # lower() = converts the user input to 'kg' or 'lb'
    # strip() = removes any xtra spaces that the user might have entered

    if weight_unit not in ['lb', 'kg']:
        print('Invalid weight unit.')
        return None

    try:
        weight = float(input("Enter weight: "))
        if weight <= 0:
            print("Weight must be greater than 0")
            return None

        if weight_unit == "lb":
            weight *= 0.453593

    except ValueError:
        print("Weight must be a number")
        return None

    return weight

def get_height():
    height_unit = input("Enter height unit (m/cm/ft): ").lower().strip()

    if height_unit not in ['m', 'cm', 'ft']:
        print('Invalid height unit.')
        return None

    try:
        if height_unit == 'm':
            height = float(input("Enter height: "))
        elif height_unit == 'cm':
            height = float(input("Enter height: "))
            height = height/100
        else:
            feet = int(input("Enter Feet: "))
            if feet >= 0:
                inches = int(input("Enter Inches (0 to 11): "))
                if 0 <= inches <= 11:
                    total_inches = (feet * 12) + inches
                    height = total_inches * 0.0254
                else:
                    print("Invalid Inches input")
                    return None
            else:
                print("Invalid Feet input")
                return None

    except ValueError:
        print("Height must be a number")
        return None

    if height > 0:
        return height
    else:
        print("Height must be greater than 0")
        return None

def calculate_bmi(weight, height):
    return round(weight / (height * height), 1)

def get_bmi_result(bmi_value):
    if bmi_value < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi_value < 25:
        return "Normal Weight"
    elif 25 <= bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

main()
