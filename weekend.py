# *Challenge for the Weekend* You are given a dictionary containing students and their test scores: students = { "John": {"math": 70, "english": 85, "science": 90}, "Mary": {"math": 95, "english": 88, "science": 76}, "Peter": {"math": 60, "english": 72, "science": 65}, "Jane": {"math": 88, "english": 91, "science": 89} } 
# *Task*: Write a Python program that: 
# 1. Finds the student with the highest average score 
# 2. Finds the student with the lowest science score 
# 3. Counts how many students scored above 80 in at least 2 subjects 
# 4. Creates a new dictionary that stores each student’s average score rounded to 2 decimal places 
# Your answer should look exactly like this: 
# Highest Average: Jane 
# Lowest Science Score: Peter 
# Students Above 80 in At Least 2 Subjects: 2 
# Average Scores: { "John": 81.67, "Mary": 86.33, "Peter": 65.67, "Jane": 89.33 }

students = { 
    "John": {"math": 70, "english": 85, "science": 90}, 
    "Mary": {"math": 95, "english": 88, "science": 76}, 
    "Peter": {"math": 60, "english": 72, "science": 65}, 
    "Jane": {"math": 88, "english": 91, "science": 89} 
} 

print("\n Finds the student with the highest average score")
highest_average = 0
top_average = " "

for student in students:
    average_score = sum(students[student].values()) / len(students[student])
    if average_score > highest_average:
        highest_average = average_score
        top_average = student

print(f"highest average: {top_average}")
print(f"average score:{highest_average:.2f}")

print("\n Finds the student with the lowest science score")
lowest_science_score = 100
lowest_science_student = " "
for student in students:
    science_score =  students[student]["science"]
    if science_score < lowest_science_score:
        lowest_science_score = science_score
        lowest_science_student = student

print(f"lowest science score: {lowest_science_student}")
print(f"science score:{lowest_science_score}")

print("\n Counts how many students scored above 80 in at least 2 subjects")
count = 0
students_above_80 = []

for student in students:
    scores = students[student]
    above_80_count = 0

    for score in scores.values():
        if score > 80:
            above_80_count += 1

    if above_80_count >= 2:
        count += 1
        students_above_80.append(student)

print(f"number of students above 80 in at least 2 subjects: {count}")
print(f"Names of students Above 80 in At Least 2 Subjects: {students_above_80}")

print("\n Creates a new dictionary that stores each student’s average score rounded to 2 decimal places")
average_scores = {}
for student in students:
    average_score = sum(students[student].values()) / len(students[student])
    average_scores[student] = round(average_score, 2)

print(f"Average Scores: {average_scores}")