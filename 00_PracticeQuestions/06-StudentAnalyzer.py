'''
Student Analyzer

Given: students = [
    {"name": "Ali", "age": 20, "marks": [80, 75, 90]},
    {"name": "Sara", "age": 21, "marks": [95, 88, 92]},
    {"name": "John", "age": 20, "marks": [60, 70, 65]},
    {"name": "Maya", "age": 22, "marks": [85, 90, 87]}
]

write a func that determines:
- each student's avg
- student with the highest and lowest avg
- the overall avg
- the highest and lowest individual mark
- students whose avg is below the overall avg
- how many students are above 20 years old
- a dictionary contained each student's name and avg
'''

def main():
    students = [
        {"name": "Ali", "age": 20, "marks": [80, 75, 90]},
        {"name": "Sara", "age": 21, "marks": [95, 88, 92]},
        {"name": "John", "age": 20, "marks": [60, 70, 65]},
        {"name": "Maya", "age": 22, "marks": [85, 90, 87]}
    ]
    output = soln(students)
    print(output)

def soln(students):
    details = {}
    num = 0
    for i in students:
        sum = 0
        for j in i["marks"]:
            sum += j
        i["avg"] = round(sum/len(i["marks"]),2)
        print("Name:", i["name"], "Avg:", i["avg"])


    overall_sum = 0
    highest, lowest = 0, 100
    highest_indi, lowest_indi = 0, 100
    for i in students:
        if i["avg"] > highest:
            highest = i["avg"]
        elif i["avg"] < lowest:
            lowest = i["avg"]

        overall_sum += i["avg"]
        overall_avg = overall_sum / len(students)

        for j in i["marks"]:
            if j > highest_indi:
                highest_indi = j
            elif j < lowest_indi:
                lowest_indi = j
        i["highest"] = highest_indi
        i["lowest"] = lowest_indi

    for i in students:
        if i["avg"] == highest:
            print("\nHighest Avg:", i["name"])
        elif i["avg"] == lowest:
            print("Lowest Avg:", i["name"])

    print("\nOverall avg:", overall_avg, "\n")

    for i in students:
        print("Name:",i["name"], "Highest Score:",i["highest"], "Lowest Score:",i["lowest"])

    counter = 0
    less_overall_avg = []
    details = {}
    for i in students:
        if i["avg"] < overall_avg:
            less_overall_avg.append(i["name"])
        if i["age"] > 20:
            counter += 1
        names = i["name"]
        avg = i["avg"]
        details[names] = avg
    print("\nStudents below the overall avg: ", less_overall_avg)
    print("\nStudents above the age 20: ", counter)
    print("\nDict with  names and avg:", details)

    return

main()
