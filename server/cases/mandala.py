import random

def gen_mandala(num_rows, num_cols, pattern):
    new_pattern = []
    for row in range(num_rows):
        cur_row = pattern[row][:] + pattern[row][::-1]
        new_pattern.append(cur_row)
    for row in range(num_rows-1, -1, -1):
        cur_row = pattern[row][:] + pattern[row][::-1]
        new_pattern.append(cur_row)
    return new_pattern

def gen_testcase():
    num_rows = random.randint(2,5)
    num_cols = random.randint(1,10)
    pattern = []
    for _ in range(num_rows):
        pattern.append("".join(random.choices("01", k=num_cols)))
    return pattern

testcases = [
   [
       "00",
       "01"
   ],
   [
       "0001",
       "0011",
       "0111",
       "1111"
   ],
   [
       "01",
       "10"
   ],
   [
       
   ]
]
testcases += [gen_testcase() for _ in range(20)]