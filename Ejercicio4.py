#Partial
partial_1 = 50
partial_2 = 60
partial_3 = 80

partial_percentage = 0.55

#final exam
final_exam = 70

final_exam_percentage = 0.30

#final project
final_project = 65

final_project_percentage = 0.15

#partial average

partial_average = (partial_1 + partial_2 + partial_3) / 3

#grade

partial_grade = partial_average * partial_percentage

final_exam_grade = final_exam * final_exam_percentage

final_project_grade = final_project * final_project_percentage

final_grade = partial_grade + final_exam_grade + final_project_grade

print(partial_grade)
print(final_exam_grade)
print(final_project_grade)
print(final_grade)
