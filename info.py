import copy

def for_cicle_example(list_array):
    # range es mas eficiente en python3 ya que no genera toda la secuencia de golpe
    for i in range(1000):
        print('ciclo en la vuelta ' + i)
        if False:
            continue  # no ejecuta nada mas en este loop y se va a la siguiente iteracion
        if False:
            break  # se sale completamente del ciclo

    for el in list_array:
        print(el)

def while_example():
  n = 10
  while n > 0:
    n-=1


#Copiando una lista
hey = ['h','l','o']    

hey2 = copy.copy(hey)

def diccionarios():
  dictcio = {
    'hey' : 10,
    'he2y' : 10,
    'hedy' : 10,
    'hfey' : 10,
  }
  print(dictcio['hey'])
  for key in dictcio.keys():
    pass

  for value in dictcio.values():
    pass

  for key, value in dictcio.items():
    pass
