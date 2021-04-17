def summ(num):
  sum1 = num + rev(num)
  if sum1 == rev(sum1):
    return (int(sum1))
  else:
   return(summ(int (sum1)))

def rev(num):
  num_str = str(num)
  num_rev = num_str[::-1]
  return (int(num_rev))

n = int(input())
print (summ(n))
