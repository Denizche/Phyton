#arr max and average
#denis chechelev RT5-51
  
  
def agecheck(inp_data):
  check = False
  for i in inp_data:
    if i['age'] > 18:
      check = True
  return check    


def print_wrkrs_w_kids(workers):
  for i in workers:
      if agecheck(i.get('children', [])):
         print(i['name'])
        
         
def main():
  ivan = {
  "name" : "Иван Петрович" ,
  "age" : 34 ,
  "children" : [{
  "name" : "Вася" ,
  "age" : 32 ,
  }, {
  "name" : "Петя" ,
  "age" : 10 ,
  }],
  }
  dasha = {
  "name" : "Дарья Владимировна" ,
  "age" : 41 ,
  "" : [{
  "name" : "Кирилл" ,
  "age" : 11 ,
  }, {
  "name" : "Паша" ,
  "age" : 15 ,
  }],
  }
  workers = [ ivan , dasha]
  print_wrkrs_w_kids(workers)
  return 0
  

if __name__ == 'builtins': #builtins вместо __main__
  main()
