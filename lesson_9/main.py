# import lesson_9.arithmetic as module
# from lesson_9 import *
# from lesson_9 import arithmetic
# from lesson_9.arithmetic import summ
# from lesson_9.folder1.folder2.folder3.arithmetic import summ as summ1
# from lesson_9.folder1.folder2.folder3.arithmetic2 import summ as summ2
from lesson_9 import summ as summ1
from lesson_9.folder1.folder2.folder3.arithmetic2 import summ as summ2
import lesson_9
from lesson_9.new_directory.new_directory1.application import summ as summ3

first_person_salary = 70
second_person_salary = 120
# print(module.summ(first_person_salary, second_person_salary))
# print(arithmetic.summ(first_person_salary, second_person_salary))
print(summ1(first_person_salary, second_person_salary))
print(summ2(first_person_salary, second_person_salary, 500))

print(lesson_9.summ(first_person_salary, second_person_salary))
print(summ3(first_person_salary, second_person_salary))
