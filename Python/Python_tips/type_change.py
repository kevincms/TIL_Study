# 1. list -> str
count=1
test_list=["%d"%i for i in range(4)]
print(f"{count}-1. {test_list}")
list_str="".join(test_list)
print(f"{count}-2. {list_str}")

# 2. tuple -> str
count+=1
test_tuple=tuple(test_list)
print(f"{count}-1. {test_tuple}")
tuple_str="".join(test_tuple)
print(f"{count}-2. {tuple_str}")