def largeSum(arr):
  values = 0

  for i in arr:
    values+= int(i)
  return str(values)[:10]

#  only change code above this line

testNums = [
  '37107287533902102798797998220837590246510135740250',
  '46376937677490009712648124896970078050417018260538'
]

print(largeSum(testNums))
