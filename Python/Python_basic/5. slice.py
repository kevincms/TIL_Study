test_list=[i for i in range(10)]
test_str="0123456789"
count=1

print("%d."%count,test_list[3],test_str[5]) # 1. 
count+=1

print("%d."%count,test_list[2:5],test_str[4:9]) # 2.
count+=1

print("%d."%count,test_list[:3],test_str[:-3]) # 3.
count+=1

print("%d."%count,test_list[3:],test_str[-3:]) # 4.
count+=1

print("%d."%count,test_list[::2],test_str[::3]) # 5.
count+=1