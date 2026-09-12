#append 
lst = [1,2,3,5]
lst.append(8)
print(lst)


#insert
lst = [1,9,2,3]
lst.insert(4,7)
print(lst)

#extend
lst = [1,2,3]
lst.extend([4,5])
print(lst)

#remove
lst=[1,2,3,4,5]
lst.remove(2)
print(lst)

#pop(only last elemnet will be removed)
lst=[2,3,4]
lst.pop()
print(lst)

#clear
lst=[10,23,44,56]
lst.clear()
print(lst)


#index
a=[4,5,6,7]
x=a.index(6)
print(x)

#count
lst=[2,2,2,2]
x=lst.count(2)
print(x)

#sort(ascending or descending order)
lst=[1,2,3,4,5]
x=lst.sort(reverse=True)
print(lst)

#reverse
lst=[12,33,44,5]
x=lst.reverse()
print(lst)


#copy
lst=[3,4,5,9]
new_lst = lst.copy()
print(lst)