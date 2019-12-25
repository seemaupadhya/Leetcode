#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

a=[7,6,4,3,1]

max_profit=0
min_price=2**32-1

for i in range(len(a)):
 if(a[i]<min_price):
   min_price=a[i]

 elif(a[i]-min_price>max_profit):
   max_profit=a[i]-min_price


print (max_profit)  
