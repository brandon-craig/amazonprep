# Algorithms

## Divide-and-Conquer

### Steps

**Divide** the problem into a number of subproblems that are smaller instances of the same problem.

**Conquer** the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblem in a straightforward way.

**Combine** the solutions to the subproblems into the solutions for the original problem.

### Solving recurrences

* In the ***substitution method***, we guess a bound and then use mathematical induction to prove our guess correct
* The ***recursion-tree method*** converts the recurrence into a tree whose nodes represent the costs incurred at various levels of the recursion. We use techniques for bounding summations to solve the recurrence
* The ***master method*** provides bounds for recurrences of the form **T(n) = a * T(n/b) + f(n)**, where a >= 1, b > 1, and f(n) is a given function. A recurrence of this form characterizes a divide-and-conquer algorithm that creates ***a*** subproblems, each of which is ***1/b*** the size of the original problem, and in which the divide and combine steps together take **f(n)** time.


**Using the master method**

Merge sort is a sorting algorithm based on the divide-and-conquer paradigm. The sorting algorithm works by dividing the original array into 2 sub arrays of **n/2** lengths. The algorithm then recursively calls sort on the two sub-arrays and combines the sorted sub-arrays. 

Using the master method, we can easily determine the asymptotic bounds on the solution, **T(n)**.

Following the form, **T(n) = a * T(n/b) + f(n)** we can quickly determine that a = 2 because we create 2 subproblems, b = 2 as the subproblems are 1/2 the size of the original problems, and f(n) equals O(n) because the combine step takes n time. Thus we get the below recurrence


**T(n)** = {**O(1)**            if n = 1,</br>
            **2T(n/2) + O(n)**  if n > 1}


### Maximum-subarray problem




