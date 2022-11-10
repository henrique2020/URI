from math import sqrt

while True:
  data = input()
  if data == '0': break

  l1, l2, p = map(int, data.split())
  area = (l1 * l2) / (p / 100)
  print(int(sqrt(area)))
