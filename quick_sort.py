#quick_sort
def quick_sort(lis):
    if len(lis)<2:
        return lis
    else:
        pivot=lis[0]
        gt_lis=[i for i in lis[1:] if i>=pivot]
        lt_lis=[i for i in lis[1:] if i<pivot]
        return quick_sort(lt_lis)+[pivot]+quick_sort(gt_lis)
print(quick_sort([85,76,24,81,33,95,12,23,23,57453,2,65,24,53,568,4788,3423424,8989]))

### [2, 12, 23, 23, 24, 24, 33, 53, 65, 76, 81, 85, 95, 568, 4788, 8989, 57453, 3423424]
