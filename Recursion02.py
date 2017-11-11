def countdown(i):
  print i
  '''
  base case基线条件
  '''
  if i<=0 : 
    return
  '''
  recursive case递归条件
  '''
  else:
    countdown(i-1)
