def removeElement(nums, val) :
    if len(nums) == 0:
        return 0
    else:
        j = 0
        for i in range(0, len(nums)):
            if not nums[i] == val:
                nums[j] = nums[i]
                j += 1
    return len(nums[:j])

