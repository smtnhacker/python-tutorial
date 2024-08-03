def gen_mandala(num_rows, num_cols, pattern):
    new_pattern = []
    for row in range(num_rows):
        cur_row = pattern[row][:] + pattern[row][::-1]
        new_pattern.append(cur_row)
    for row in range(num_rows-1, -1, -1):
        cur_row = pattern[row][:] + pattern[row][::-1]
        new_pattern.append(cur_row)
    return new_pattern

testcases = [
   [
       "00",
       "01"
   ]
]