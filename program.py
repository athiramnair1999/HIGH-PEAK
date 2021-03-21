def minD(arr,n,k):
  result=1000000000
  arr.sort()
  for i in range(n-k):
    if result>arr[i+k-1]-arr[i]:
      result=arr[i+k-1]-arr[i]
  return result
def fidl(res,arr,n,k):
  result=10000000000
  for i in range(n):
    if result>arr[i+k-1]-arr[i]:
      result=arr[i+k-1]-arr[i]
      if res==result:
        return i
  return 0
arr=[]
f1=open("input.txt","r")
f2=open("output.txt","a")
r=""
k=int(f1.readline()[-2])
r=f1.readline()
items=f1.readlines()
f1.seek(0)
r=f1.readline()
r=f1.readline()
r=f1.readline()
while r!='':
    i=-2
    while r[i].isalpha()==False:
        i=i-1
    arr.append(int(r[i+3:-1]))
    r=f1.readline()
n=len(arr)
result=minD(arr,n,k)
f2.write("Number of employees:"+str(k)+"\n")
si=fidl(result,arr,n,k)
f2.write("Here the goodies that are selected for distribution are:")
for i in range(si,si+k):
  f2.write(items[i])
f2.write("And the difference between the chosen goodie with highest price and the lowest price is:"+str(result)+"\n")  
f2.write("\n")
f1.close()
f2.close()
