#https://leetcode.com/problems/contains-duplicate/

a=[1,2,3,1]
if(len(a)==0):
  print(False)

else:
 arr=set(a)
 if(len(a)!=len(arr)):
   print(True)
 else:
   print(False)
