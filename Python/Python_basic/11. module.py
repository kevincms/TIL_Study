# test_module 에 있는 함수들을 다양한 방법으로 사용할 수 있다.
import test_module
language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]
count=1

test_module.count_print(count)
test_module.language_print(language[count-1])
count+=1

import test_module as tm

tm.count_print(count)
tm.language_print(language[count-1])
count+=1

from test_module import count_print,language_print

count_print(count)
language_print(language[count-1])
count+=1

from test_module import count_print as cp,language_print as lp

cp(count)
lp(language[count-1])
count+=1

from test_module import * # * 는 전부 가져오는 것을 의미한다.

count_print(count)
language_print(language[count-1])
count+=1