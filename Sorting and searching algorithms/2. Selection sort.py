
lst = [95, 48, 48, 99, 89, 100, 57, 1, 89]


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_val_inx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_val_inx]:
                lowest_val_inx = j
        nums[i], nums[lowest_val_inx] = nums[lowest_val_inx], nums[i]

