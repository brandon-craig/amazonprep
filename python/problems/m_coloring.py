def mColoring(graph, m, k):
	while True:
		nextStep(graph, k, m, solution)

		if solution[k] == 0:
			return

		if k == n:
			return solution[1:]
		else:
			mColoring(graph, m, k+1)



def nextStep (graph, k, m):
	n = len(graph.keys())
	while True:
		solution[k] = (solution[k] + 1) % (m + 1)
		if solution[k] == 0:
			return

		i = 1
		while i < n:
			if i in graph[k] and solution[i] == solution[k]:
				break

			i += 1

		if i == (n+1):
			return


def main():
	pass

if __name__ == '__main__':
	main()