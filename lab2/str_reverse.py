#arr max and average
#denis chechelev RT5-51
def str_reverse(inp_str):
  res = ""
  for i in range(len(inp_str)):
    res = inp_str[i] + res
  return res  
  
  
def main():
  hellostr = "Hello world"
  print(str_reverse(hellostr))
  return 0


if __name__ == 'builtins': #builtins вместо __main__
  main()
