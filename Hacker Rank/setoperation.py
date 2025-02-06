n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(*sorted(a ^ b), sep='\n') 
# how to print each element in new line
# print(*sorted(a ^ b), sep='\n')  # this is the answer
  
 