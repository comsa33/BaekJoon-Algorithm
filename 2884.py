h, m = input().split(' ')

total_m = int(h)*60 + int(m) - 45
print(total_m//60, total_m%60)