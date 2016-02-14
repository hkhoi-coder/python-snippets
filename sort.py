def is_increasing(arr):
	for i in range(0, len(arr) - 1):
		if arr[i] > arr[i + 1]: return False
	return True

def selection_sort(arg):
	for i in range(len(arg)):
		min = arg[i]
		index = i

		for j in range(i,len(arg)):
			if arg[j] < min:
				min = arg[j]
				index = j

		temp = arg[i]
		arg[i] = arg[index]
		arg[index] = temp

def insertion_sort(arg):
	for i in range(1, len(arg)):
		cur = arg[i]
		j = i - 1
		while j >= 0 and arg[j] > cur:
			arg[j + 1] = arg[j]
			j -= 1
		arg[j + 1] = cur

def bubble_sort(arg):
	for i in range(len(arg) - 1, -1, -1):
		for j in range(i):
			if arg[j] > arg[j + 1]:
				temp = arg[j]
				arg[j] = arg[j + 1]
				arg[j + 1] = temp
def merge_sort(arg):
	if len(arg) <= 1: return

	mid = len(arg) / 2
	sub0 = arg[:mid]
	sub1 = arg[mid:]

	merge_sort(sub0)
	merge_sort(sub1)

	merge(arg, sub0, sub1)

def merge(master, sub0, sub1):
	i0 = 0
	i1 = 0
	for i in range(len(master)):
		if i0 >= len(sub0):
			master[i] = sub1[i1]
			i1 += 1
		elif i1 >= len(sub1):
			master[i] = sub0[i0]
			i0 += 1
		else:
			if sub0[i0] < sub1[i1]:
				master[i] = sub0[i0]
				i0 += 1
			else:
				master[i] = sub1[i1]
				i1 += 1

def quick_sort_impl(arr, left, right):
	if left >= right: return

	pivot = arr[(left + right) / 2]
	iLeft = left
	iRight = right

	while iLeft < iRight and arr[iLeft] != arr[iRight]:
		while arr[iLeft] < pivot: iLeft += 1
		while arr[iRight] > pivot: iRight -= 1
		if iLeft < iRight:
			temp = arr[iLeft]
			arr[iLeft] = arr[iRight]
			arr[iRight] = temp
	
	quick_sort_impl(arr, left, iLeft)
	quick_sort_impl(arr, iLeft + 1, right)

def quick_sort(arr):
	quick_sort_impl(arr, 0, len(arr)- 1)

arr = [62,58,576,428,7568,74,6,857,842,67,5,8263,45,46,24,378,5824,368]
selection_sort(arr)
print is_increasing(arr)
