def square_root_generator(limit):
  n = 1
  while n <= limit:
     yield n ** 0.5
     n += 1

# Example usage:
limit = 5
generator = square_root_generator(limit)

sum = 0
for index, sqrt_value in enumerate(generator):
  sum += sqrt_value

print('sum', sum)

limit = 13
generator = square_root_generator(limit)

for index, sqrt_value in enumerate(generator):
  print(index, ':', sqrt_value )

