
n = int(input())
my_list = list(map(int, input().split(" ")))
target = int(input())

left = 0
right = len(my_list) - 1
success = False

while left < right:
    sum = my_list[left] + my_list[right]
    if sum == target:
        success = True
        break
    elif sum < target:
        left += 1
    else:
        right -= 1
        
if success == True:
    print("Yes")
else:
    print("No")
