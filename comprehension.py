
#%% Comprehension with array
data = range(100)##Array from 0 to 99
pares = [numero for numero in data if numero % 2 == 0 ]
pares

#%% Comprehension con diccionarios 
stundent_uid = [1,2,3]
students = ['Luis','Jose','Rogelio']
students_with_uid = {uid: student for uid,
                     student in zip(stundent_uid, students)}
students_with_uid

#%% Set comprehension
import random
random_numbers = []
for i in range(10):
  random_numbers.append(random.randint(1,3))
print(random_numbers)

not_repeated = {number for number in random_numbers} #esto es un set ya que un set se puede inicializar tambien con las llaves

print(not_repeated)
