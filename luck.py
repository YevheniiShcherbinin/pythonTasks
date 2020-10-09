def lucky(num):
  array = [1] * 10 + [0] * (num // 2 * 9 - 9)
  for i in range(num // 2 - 1):
    array = [sum(array[x::-1]) if x < 10 else sum(array[x:x-10:-1]) for x in range(len(array))]
  return sum([x**2 for x in array])
print(lucky(6))

# print(Lucky(6))
# TEST Luck
# a = 0
# z = 999999
# cnt = 0
# for i in range(a, z+1):
# i_str = str(i)
# while len(i_str) < 6:
# i_str = "0" + i_str
# i = list(i_str)
# f = i[0:3]
# s = i[3:]
# if sum(map(int, f)) == sum(map(int, s)):
# cnt += 1
# print(cnt)

# def lucky(minimum, maximum):
# for each in range(minimum, maximum+1):
# number = ("{0:0%d}" % len(str(maximum))).format(each)
# a = number[:len(number)//2]
# b = number[len(number)//2:]
# if a == b:
# yield number
# elif sum([int(x) for x in a]) == sum([int(x) for x in b]):
# yield number
# print(len(list(lucky(0, 10**6-1))))
