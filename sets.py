name = {10,10,20,30,40,40,50}
print(name)

nums = {}
print(type(nums))

nums=set()
print(type(nums))

nums = {10,20,30}
nums.add(40)
print(nums)

#union
A={10,20,30}
B={30,40,50}
print(A |B)
#union using method()
print(A.union(B))

#intersection
A={10,20,30}
B={30,40,50}
print(A & B)
print(A.intersection(B))

#difference
A={10,20,30}
B={30,40,50}
print(A - B)
print(B - A)

A={10,20,30}
B={30,40,50}
print(A ^ B)


#set main methods
nums={10,20,30,40}
print(max(nums))
print(min(nums))
print(len(nums))
print(sum(nums))
nums.add(50)
print(nums)
result=sorted(nums)
print(result)
nums.update([60,70,80])
print(nums)
nums.remove(70)
print(nums)
nums.pop()
print(nums)
nums.discard(60)
print(nums)
nums.clear()
print(nums)