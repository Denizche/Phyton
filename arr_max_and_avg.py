#arr max and average
#denis chechelev RT5-51
def arr_min(array):
  minim = array[0]
  for i in range(1, len(array)):
    crnt = array[i]
    if crnt < minim:
      minim = crnt
  return minim

def arr_avg(array):
  sm = 0
  for i in range(len(array)):
    sm+=array[i]
  return sm / len(array)

array1 = [-999,666,13,47,-27.7,-0.000001]
array2 = [-0,1000,50,-50]     
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
