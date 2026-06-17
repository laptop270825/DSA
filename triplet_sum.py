def pair_sum_sorted(nums, start, target):
    """
    Given a sorted array of integers and a target integer, return the indices of the two numbers that add up to the target.

    Args:
    nums (List[int]): A sorted list of integers.
    start (int): The starting index for the search.
    target (int): The target sum.

    Returns:
    List[List[int]]: A list containing lists of the two numbers that add up to the target.
    """
    left, right = start, len(nums) - 1
    pairs=[]
    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            pairs.append([nums[left], nums[right]])
            left+=1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs  # Return the list of pairs if found
triplets=[]
nums=input("Enter the list of numbers separated by space: ").split()
nums=[int(num) for num in nums]
nums.sort()
for i in range(len(nums)):
    if nums[i]>0:
        break
    elif i>0 and nums[i]==nums[i-1]:
        continue
    pairs=pair_sum_sorted(nums,i+1,-nums[i])
    for pair in pairs:
        if pair != []:
            triplet = [nums[i]] + pair
            triplets.append(triplet)
        else:
            continue
print(triplets)