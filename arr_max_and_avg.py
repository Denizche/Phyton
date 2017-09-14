#arr max and average
#denis chechelev RT5-51
def arr_min(array):
  if len(array) == 0:
      return -1
  minim = array[0]
  for i in range(1, len(array)):
    current = array[i]
    if current < minim:
      minim = current
    
  return minim


def arr_avg(array):
  if len(array) == 0:
      return -1
  summ = 0
  for i in range(len(array)):
    summ += array[i]
  return summ / len(array)
  
  
def main():
  array1 = [-999,666,13,47,-27.7,-0.000001]
  array2 = []     
  print(array1)
  print('Минимальное значение: ')
  print(arr_min(array1))  
  print('Среднее значение: ')
  print(arr_avg(array1))
  print(array2)
  print('Минимальное значение: ')
  print(arr_min(array2))  
  print('Среднее значение: ')
  print(arr_avg(array2))
  return 0

print (__name__)
if __name__ == 'builtins': #builtins вместо __main__
  main()
