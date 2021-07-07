integer = int(input())

sum_ = integer % 10
integer //= 10

sum_ += integer % 10
integer //= 10

sum_ += integer % 10

print(sum_)
