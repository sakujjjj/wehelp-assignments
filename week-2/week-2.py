# 要求一 #
def caculate(min,max):
    sum=0
    for n in range(min,max+1):
        sum = sum+n
    print(sum)
    
caculate(1, 3)
caculate(4, 8)

# 要求二 #
def avg(data):
    sum=0
    for i in data["employees"]:
        # print(i)
        sa = i["salary"]
        #印出薪水
        # print(sa)
        sum=sum+sa
    #薪水總和
    # print(sum)
    mean = sum/data["count"]
    print(mean)

avg(
    {
        "count":3,
        "employees":[
            {
                "name":"John",
                "salary":30000
            },
            {
                "name":"Bob",
                "salary":60000
            },
            {
                "name":"Jenny",
                "salary":50000
            }
        ]
    }
)
# 要求三 #
def maxProduct(nums):
    ####判斷負數
    negative =[i for i in nums if i<0]
    # print(len(negative))

####判斷負數數量<2 執行取最大值
    if len(negative) < 2:
        #### nums取max (a)
        max_value = max(nums)
        # print(max_value)
        a = max_value
        # print(a)

        #### nums刪除a 產生nums2
        nums.remove(a)
        # print(nums)
        nums2 = nums
        # print(nums2)

        #### nums2取max (b)
        max_value2 = max(nums2)
        b = max_value2
        # print(b)

        print(a*b)

####其他 執行取最小值
    else:
                #### nums取min (a)
        min_value = min(nums)
        # print(max_value)
        a = min_value
        # print(a)

        #### nums刪除a 產生nums2
        nums.remove(a)
        # print(nums)
        nums2 = nums
        # print(nums2)

        #### nums2取max (b)
        min_value2 = min(nums2)
        b = min_value2
        # print(b)

        print(a*b)


maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])

# 要求四 #
def twoSum(nums, target):
    for i in range(len(nums)):
        left = nums[i+1:]
        for j in range(len(left)):
            if (nums[i] + left[j]) == target:
                return i, j+i+1
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
