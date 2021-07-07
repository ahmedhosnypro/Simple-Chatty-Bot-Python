height = int(input())
width = int(input())
length = int(input())

allowed = (height <= 10 < width <= 35 < length <= 40) or (height + width + length <= 80)

print(allowed)
