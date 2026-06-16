class Solution(object):
    def twoSum(self,arr,target):
        rlar=list(arr)
        arr.sort()
        l,el=0,len(arr)-1
        while l<len(arr)-1:
            if arr[l] + arr[el] == target:
                if rlar.index(arr[l]) != rlar.index(arr[el]):
                    return rlar.index(arr[l]),rlar.index(arr[el])
                elif rlar.index(arr[l]) == rlar.index(arr[el]):
                    a=l
                    rlar[rlar.index(arr[l])]='y'
                    return a,rlar.index(arr[a])
            elif arr[l] + arr[el] < target:
                l+=1
            elif arr[l] + arr[el] > target:
                el-= 1
        else:
            False