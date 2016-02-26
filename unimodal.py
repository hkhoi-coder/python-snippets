def unimodal(ar):
	return __unimodal(ar, 0, len(ar) - 1)

def __unimodal(ar, left, right):
	if left >= right:
		return ar[left]
	mid = (left + right) / 2
	mid_value = ar[mid]

	is_increasing = False

	if mid < len(ar) - 1:
		next_value = ar[mid + 1]
		is_increasing = next_value > mid_value
	elif mid > 0:
		pre_value = ar[mid - 1]
		is_increasing = pre_value < mid_value

	if is_increasing:
		return __unimodal(ar, mid + 1, right)
	else:
		return __unimodal(ar, left, mid)

a = [1,2,3,4,5,6,7,8,9,8,7]
print unimodal(a)