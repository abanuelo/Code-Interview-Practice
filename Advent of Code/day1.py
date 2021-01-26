import os

#Store numbers from input text into here
nums = []
with open('input-day1.txt') as f:
    for line in f:
        nums.append(int(line.strip()))

#Sort the array
nums.sort()

#Traverse sorted array using two pointers one at the end and one at the beginning
front_pointer = 0
end_pointer = len(nums)-1

found_2020 = False

#PART 1 while we haven't found the 2020 sum, continue to move pointers accordingly
# Time Complexity: O(n)
# Space Complexity: O(1)
while (not found_2020):
    res = nums[front_pointer] + nums[end_pointer]
    if (res > 2020):
        end_pointer -= 1
    elif (res < 2020):
        front_pointer += 1
    else:
        found_2020 = True

print("______________________PART 1______________________")
print("First number: ", nums[front_pointer])
print("Second number: ", nums[end_pointer])
print("Sum: ", nums[front_pointer] + nums[end_pointer])
print("Product: ", nums[front_pointer] * nums[end_pointer])

#PART 2 - Traversing through the input of numbers using three numbers to find sum of 2020
first_num = 0
second_num = 0
third_num = 0

found_2020 = False

# Time Complexity: O(n^2) 
# Space Complexity: O(1)
# The idea here is to continually traverse nums by two pointers near the start. We then find the sum of those pointers
# take the difference with respect to 2020 and verify its existence within the nums array
while (not found_2020): 
    for i,f_num in enumerate(nums):
        first_num = f_num
        for j,l_num in enumerate(nums):
            second_num = l_num
            if (i != j):
                res = first_num + second_num
                third_num = 2020 - res
                if (third_num > 0):
                    if (third_num in nums and nums[i] != third_num and nums[j] != third_num):
                        found_2020 = True
                    break
        if (found_2020 == True):
            break
    break

print("______________________PART 2______________________")
print("First number: ", first_num)
print("Second number: ", second_num)
print("Third number: ", third_num)
print("Sum: ", first_num + second_num + third_num)
print("Product: ", first_num * second_num * third_num)



