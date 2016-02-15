def hanoi(num):
	solve(num, 0, 1, 2)

def solve(num, left, mid, right):
	if num == 1:
		move(left, right)
	else:
		solve(num - 1, left, right, mid)
		move(left, right)
		solve(num - 1, mid, left, right)
def move(left, right):
	print 'Move disk from ', left,'to ', right
	
num = raw_input('Enter number of disks: ')
hanoi(int(num))
