# Project Explanation

## Problem 1
For Finding the Square Root of an Integer problem I decided to solve it implementing the binary search, due to the required time 
complexity.

### Time and Space complexity:
The  time complexity is O(log(n), based on the binary search approach as we transverse the  list.
The space complexity, it's independent of the input O(1).

----

## Problem 2
The solution for problem Search in a Rotated Sorted Array is based directly in the Binary Search Algorithms, where was necessary to search a number in a rotated array. 
For this excersice it was necessary to find a pivot point from where the array is rotated and then implement a Binary Search Algorithm to find where the requested number is located.

### Time and Space complexity
The time complexity for this excercie is O(log(n)), based on binary search. 
For the space complexity for this excercise is O(1) because it's independent of the input, in this case the pivots to the different array locations.

---

## Problem 3
For problem Rearrange Array Elements it was necessary list and get the frequency of numbers from the input array and store them into a new array. This excercise uses a variation of the merge Sort Algorithm  with a a variation in the way that based on the frequency of the array items defines how they will be stored through the different lists.

### Time and Space complexity 
The time complexity of this excercise uses a Merge sort algorithm wich is in order of the O(n log n).
The space complexity depends on the lenght of the input arrays so it can be defined as O(n)

---
## Problem 4
The Dutch National Flag Problem problem, consists in an algorith that sorts an array (consisting with 0, 1 and 2) from the lowest number (0) to the highest (2).

### Time and Space complexity
The time complexity for this excersice is 0(n)
The Space complexity the use of a few pointers, its in order of O(n)

---
## Problem 5
In this exercise Autocomplete with Tries, is focused on the use of the Trie data structure (tree store) which all the nodes contains some alphabet letters and the string or words can be retrived by trasversing down a branch path of the tree

### Time and Space complexity
The time complexity for this algorithm is dependent on how many and how long are the words that will be stored in the Trie. For this reasons the Time Complexity can be defined as O(m * n) where m is the longest word and n is the number of words.
The Space Complexity will be defined by the number of words for lookup O(n).

---
Problem 6
This problem Max and Min in a Unsorted Array is find the max and min values from an unsorted array and compare it with a tuple value.

### Time and Space complexity
The time complexity  for this excercise is O(n) becuase its not necesary to order the array just make a single traversal to get the values. 
In respect Space complexity is order of O(n) due the validations to get the values depends on the size of the array

---
Problem 7
For excercise HTTPRouter its similar with problem 5. For this Excercise was necesary to implement a Trie algorithm wich imitates the hierarchy of web page  instead of strings.

### Time and Space complexity
In this excercise the Time Complexity of of the trie depends on the length of the path that will be searched for, and the length of "depth" for next folder O(m * n). Similar to problem 5
The Space Complexity of the trie looking into the space depends in the number of path or paths O(n)


