>>> a_string = 'amanaplanacanalpanama' * 10
>>> min(timeit.repeat(lambda: reverse_string_readable_answer(a_string)))
10.38789987564087
>>> min(timeit.repeat(lambda: reversed_string(a_string)))
0.6622700691223145
>>> min(timeit.repeat(lambda: reverse_a_string_slowly(a_string)))
25.756799936294556
>>> min(timeit.repeat(lambda: reverse_a_string_more_slowly(a_string)))
38.73570013046265
