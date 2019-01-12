import numpy as np

students = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]


np.random.shuffle(students)

for i in range(len(students)):
    if i % 2 == 0:
        student_one = students[i]
        student_two = students[i + 1]
        print(student_one, student_two)
