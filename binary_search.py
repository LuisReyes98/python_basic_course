#%%
import random

def binary_search(data, target , low, high):
  if low > high:
    return False
  mid = (low + high) // 2
  if target == data[mid]:
    return True
  elif target < data[mid]:
    return binary_search(data,target,low,mid - 1)
  else:
    return binary_search(data,target,mid + 1, high)

if __name__ == '__main__':
  data = [random.randint(0,100) for i in range(10)]

  data.sort() #ordena el arreglo y modifica la variable
  # sorted_data = sorted(data)# retorna un nuevo arreglo
  print(data)
  target = input("Que numero desea buscar?\n")
  found = binary_search( data, int(target) , 0 , len(data) - 1)
  print(found)