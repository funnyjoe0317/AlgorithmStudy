
# 169. Majority Element
nums = [1,2,2,3,3,4,4,5,5,5]


# def majorityElement(nums):
#     if not nums:
#             return None
#     if len(nums) == 1:
#             return nums[0]

#     half = len(nums) // 2

#     a = majorityElement(nums[:half])
#     b = majorityElement(nums[half:])

#     return print([b, a][nums.count(a) > half ])

# majorityElement(nums)

# ** 리스트.sort()와 sorted(리스트)의 가장 큰 차이는
# 리스트.sort() 는 본체의 리스트를 정렬해서 변환하는 것이고,
# sorted(리스트) 는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것입니다.

a =  sorted(nums)[len(nums)//2]

print(a)