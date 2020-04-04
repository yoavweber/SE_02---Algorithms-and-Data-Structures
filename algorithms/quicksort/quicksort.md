Quicksort step by step:

for the sake of simplicity, we would divide the algorithm into two section:
#### Partitioning
1.  Find a “pivot” element in an array. The pivot item is the basis for comparison for a single round.
2.  While the value at the left pointer in the array is less than the pivot value, move the left pointer to the right Continue until the value at the left pointer is greater than or equal to the pivot value.
3.  While the value at the right pointer in the array is greater than the pivot value, move the right pointer to the left. Continue until the value at the right pointer is less than or equal to the pivot value.
4. We swap the values that the left and right pointers are pointing to.
5. We continue this process until the pointers are pointing to the very same
value or the left pointer has moved to the right of the right pointer.
6. swap the pivot with the value that the left pointer is currently pointing to.

#### quicksort
1. partition the array.
2. treat all the elements that are left to the pivot as one array
3. treat all the elements that are right to the pivot as one array
4. repeat those steps until we have subarray that has zero or one elements.


## analysis
Partitioning consist two steps:
* Comparison: We compare each value to the pivot
* Swaps: when needed, we swap the value being pointed to by the left and right pointer.

#### partition:
looping over all the array: n
swapping(max number): n/2
O(n+n/2) => O(n)
time complexity: O(n)


in quicksort, we are creating from the arrays sub arrays until each sub array has 1 or 0 elements.
## quicksort best case running time
The best case would occur when the partition would be evenly balanced. this would happend if the array has odd number of elements and the pivot would be right in the middle after partitioning.
time analysis:
n+(n/2)*2 + (n/4)*4.... = nlog2n

time complexity: O(nlogn)



## quicksort average case
In average cases, the pivot would be around half of the array, assuming 3-to-1 split,which there is a chance of 50% it would happen. which mean we would get 1/4 sub array and 3/4 sub array.

time analysis:
n+((n/4)+(3n/4)) + ((n/16+3n/16)*2).... = nlog4/3n

time complexity: O(nlogn)

## quicksort worst case
The worst case would happen when the pivot that was choose by the partition function would always be the lowest, which would lead to a situation where on sub array would have n-1 elements, and the other would be one. This could happen if the array is sorted.

time analysis:
as before, the partitioning would take O(n). since the partitioning would be done on every sub array, and there would be N sub array we would get:

n+(n-1)+(n-2)...... which equal to O(N**2).

## Time complexity proof
array: [3,10,14,1,2,5,9,6,7]
element numbers: 9

##### partition number 1
number of swaps:  3
number of comparisons:  8
steps in partition:  11
array after partition:  [3, 6, 5, 1, 2, 7, 9, 10, 14]
total steps:  11

##### partition number 2
number of swaps:  2
number of comparisons:  4
steps in partition:  6
array after partition:  [1, 2, 5, 3, 6, 7, 9, 10, 14]
total steps:  17
##### partition number 3
number of swaps:  1
number of comparisons:  2
steps in partition:  3
array after partition:  [1, 2, 5, 3, 6, 7, 9, 10, 14]
total steps:  20
##### partition number 4
number of swaps:  1
number of comparisons:  1
steps in partition:  2
array after partition:  [1, 2, 3, 5, 6, 7, 9, 10, 14]
total steps:  22
##### partition number 5
number of swaps:  1
number of comparisons:  2
steps in partition:  3
array after partition:  [1, 2, 3, 5, 6, 7, 9, 10, 14]
total steps:  25
##### partition number 6
number of swaps:  1
number of comparisons:  1
steps in partition:  2
array after partition:  [1, 2, 3, 5, 6, 7, 9, 10, 14]
total steps:  27


#### number of steps at the end 27

if n = 9
n*logn = 9*log9 = 28.529325013 ~ 27

## use cases
In many of these languages, the sorting algorithm that is employed under the hood is Quicksort.