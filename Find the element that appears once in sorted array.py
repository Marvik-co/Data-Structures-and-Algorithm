def findOnce(arr : list, n : int):
  # z=0
  # for i in range(n):
  #     z^=arr[i]
  # return z

  l,h=0,n-1
  if l==h:
     return arr[l]

  while l<=h:
     mid=(l+h)//2
     if mid==len(arr)-1 and arr[mid]!=arr[mid-1]:
         return arr[mid]
     elif mid==0 and arr[mid]!=arr[mid+1]:
         return arr[mid]
     elif arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
         return arr[mid]
     elif mid%2==0 and arr[mid]==arr[mid+1]:
         l=mid+1
     elif mid%2==0 and arr[mid]==arr[mid-1]:
         h=mid-1
     elif mid%2!=0 and arr[mid]==arr[mid-1]:
         l=mid+1
     elif mid%2!=0 and arr[mid]==arr[mid+1]:
         h=mid-1

  return -1
# def findOnce(arr : list, n : int)
