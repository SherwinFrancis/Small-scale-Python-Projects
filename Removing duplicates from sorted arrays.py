def remove_duplicates(nums) :
    if len(nums) == 0:
        return 0

    j = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # check if current element is different
            nums[j] = nums[i]
            j += 1

    # remove extra elements after the last unique one
    del nums[j:]

    return len(nums)

    


        