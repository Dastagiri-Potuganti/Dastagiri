#nums=[0,0,1,1,1,2,2,3,3,4]
#nums=[1,1,2]
'''x=[]
for i in nums:
    if i not in x:
        x.append(i)
count=len(x)
while len(nums)!=len(x):
    x.append('_')
print(count,',',x)'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x=[]
        for i in nums:
            if i not in x:
                x.append(i)
        count=len(x)
        while len(nums)!=len(x):
            x.append('_')
        return count,x
nums=[0,0,1,1,1,2,2,3,3,4]
obj=Solution(nums)
print(obj.removeElement())
    


'''nums=[1,2,3,4,5,6]
output={'even':[],'odd':[]}
for i in nums:
    if i%2==0:
        output['even'].append(i)
    else:
        output['odd'].append(i)
print(output)'''
