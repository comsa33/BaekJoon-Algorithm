import sys

arr = sys.stdin.readline().rstrip()
arr = list(map(int, list(arr)))
print(arr)
# arr.sort(reverse=True)

for i in range(len(arr)):
    temp = arr[i]
    k = i
    while k > 0 and temp > arr[k-1]:
            arr[k] = arr[k-1]
            k -= 1
    arr[k] = temp

print(arr)
print(''.join(map(str, arr)))
