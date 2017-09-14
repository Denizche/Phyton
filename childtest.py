#arr max and average
#denis chechelev RT5-51
  
  
def check_age(inp_data):
  for i in inp_data:
    if i['age'] > 18:
      return True
  return False    


def print_workers_with_kids(workers):
  for x in workers:
      if check_age(x.get('children', [])):
         print(x['name'])
        
         
def main():
  ivan = {
  "name" : "Иван Петрович" ,
  "age" : 34 ,
  "children" : [{
  "name" : "Вася" ,
  "age" : 20 ,
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
  print_workers_with_kids(workers)
  return 0
  

if __name__ == 'builtins': #builtins вместо __main__
  main()
