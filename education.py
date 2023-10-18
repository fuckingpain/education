print("jopa")

x = 0
# while (x <= 10):
#     print (x)
#     x += 1
    
# for x in range(1,10):
#     print (x)
    
# x = input("Input number")
# print (x)



# first_name, last_name, age = input(), input(), input()
# print(f'Имя: {first_name}, Фамилия: {last_name}, Возраст: {age}')#ЕЕЕЕЕЕЕБАТЬ КАК ВКУСНО .f-строки прекольна 1:28 :)ъ



# huh = dict(
#     bg = '#ffff',
#     hight = '30px',
#     weight = 'screen-full',
#     border = ('1','2','3'),
#     dict_in_dict = dict(
#         red = 'green',
#         blue = 'white'
#     )
    
# )
# print (huh['dict_in_dict'])#а как какать. хочу не весь внутренний dict вывести, а только часть









# #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def twoSum(nums: list[int], target: int) -> list[int]:
    for i in nums:
        for j in nums:
            if(int(i) + int(j) == target):
                nums = [nums.index(i),nums.index(j)]
                return nums
str = input()
nums = str.split()
target = int(input())

print(twoSum(nums, target))


