def fibonacci_evens(max_term):
  last = 1
  current = 2
  running_sum = long()
  while current <= max_term:
    nxt = last + current
    if current == max_term or nxt > max_term:
      if current % 2 == 0:
        running_sum = running_sum + current
        return running_sum
      else:
        return running_sum
    else:
      if current % 2 == 0:
        running_sum = running_sum + current
        last = current
        current = nxt
      
      else:
        nxt = last + current
        last = current
      
    current = nxt
  
print(fibonacci_evens(4000000))
