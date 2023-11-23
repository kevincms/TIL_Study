import itertools

count=1

# 1. product
test=itertools.product("test",repeat=2)
for i in itertools.product("1234",repeat=2):
    i="".join(i)
    print(f"{count}. {i}",type(i)) 