def fibonacci_evens(max_term):
  last = 1
  current = 2
  running_sum = long()
for i in 1:maxterm:
  if current == max_term:
    if current % 2 == 0:
      running_sum = running_sum + current
      return running_sum
    else:
      return running_sum
  else:
    if current % 2 == 0:
      running_sum = running_sum + current
      next = last + current
      last = current
      current = next
      
    else
    current = last + current
    last = current
    if 
    return
  
