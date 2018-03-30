def subsetSumProblem(n, s):
	if not checkBounds(n, s):
		return False

	return q(len(n)-1, s, n)


def q (i, s, n):
	if i < 0:
		return False

	else:
		return (n[i] == s) or q(i-1, s, n) or q(i-1, s-n[i], n)

def checkBounds(n, s):
	sumNegative = None
	sumPositive = None

	for i in n:
		if i == 0:
			continue
		if i > 0:
			if sumPositive:
				sumPositive += i
			else:
				sumPositive = i
		else:
			if sumNegative:
				sumNegative += i
			else:
				sumNegative = i


	if sumNegative and s < sumNegative:
		return False

	if sumPositive and s > sumPositive:
		return False

	return True


def main():
	check = [5, 10, 12, 13, 15, 18]
	if subsetSumProblem(check, 30):
		print "Found"

	else:
		print "Not Found"

if __name__ == '__main__':
	main()