target=9  
nums=[11,2,5,6,7]
dict={}
for i in range(len(nums)):
  if(target-nums[i] in dict):
    print(dict[target-nums[i]],i)
  else:
    dict[nums[i]]=i       



