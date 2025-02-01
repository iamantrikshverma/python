count = 0
for i in range(11):
    # if i%3 == 0:
    #     continue  
    # if (i**0.5).isdigit():
    #     continue 
    # print(i**0.5)
    # if '.' not in str(i**0.5):
    #     continue
    
    # k = str(i**0.5)    #only possible for int
    # if k[-1]=='0' and k[-2]== '.':
    #     continue
    # print(i)
    # count = 0
    for j in range(9):
        if i*j<=64:
            count+=1
print(count)    
    