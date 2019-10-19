def parse_ranges(arg):
    output = []
    arg = arg.replace(' ', '')
    ranges = [x.split('-') for x in arg.split(',')]
    for rang in ranges:
      try:
        if len(rang) == 1:
          tmp = int(rang[0])
          output.append(rang[0])
          #yield rang[0]
        else:
          tmp0 = int(rang[0])
          tmp1 = int(rang[1])
          for x in range(rang[0], rang[1]+1):
            #yield x
            output.append(x)
      except ValueError:
        
    return output

t1 = parse_ranges('1-2,4-4,8-10')
print(str(t1) + '\n' + '[1, 2, 4, 8, 9, 10]')
t2 = parse_ranges('0-0, 4-8, 20, 43-45')
print(str(t2) + '\n' + '[0, 4, 5, 6, 7, 8, 20, 43, 44, 45]')
t3 = parse_ranges('0, 4-8, 20->exit, 43-45')