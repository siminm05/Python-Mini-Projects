'''
BMI Calculator
'''
weight_unit = input("Enter weight unit (kg/lb): ").lower().strip()
#lower() = converts the user input to 'kg' or 'lb'
#strip() = removes any xtra spaces that the user might have entered

if weight_unit not in ['lb','kg']:
    print('Invalid weight input')
else:
    weight = float(input("Enter weight: "))
    if weight_unit == "lb": #converting weight - lb to kg
        # kg = lb * 0.453593
        weight = weight*0.453593

    height_unit = input("Enter height unit (m/cm/ft): ").lower().strip()
    if height_unit not in ['m','cm','ft']:
        print('Invalid height input')
    else:
        if height_unit == 'm':
            height = float(input("Enter height: "))
        elif height_unit == 'cm':
            height = float(input("Enter height: "))
            height = height / 100    #converting height - cm to m
        elif height_unit == 'ft':
            feet = int(input("Feet: "))
            inches = int(input("Inches: "))
            total_inches = (feet * 12) + inches   #converting height - feet to m
            height = total_inches * 0.0254

        bmi = round((weight/(height*height)),1)
        print(bmi)

        if bmi < 18.5:
            result = 'Underweight'
        elif (bmi >= 18.5) and (bmi < 25):
            result = "Normal Weight"
        elif (bmi >= 25) and (bmi < 30):
            result = "Overweight"
        else:
            result = "Obese"

        #print("Your BMI is", bmi, "! You are", result, ".")
        print("Your BMI is ", bmi, "! You are ", result, ".", sep="")
        #print(f"Your BMI is {bmi}! You are {result}.")
