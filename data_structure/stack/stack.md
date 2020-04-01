Stacks allow you to handle data in order, and then get rid of it once you don’t need it anymore.
Stacks are ideal for processing any data that should be handled in reverse order to how it was received.

in a stack:
* data can only be inserted at the end of the stack
* data can only be read from the end of the stack
* data can only be removed from the end of the stuck - the first to come, the last to go

The stack can be implemented using an array or linked list(get back to it after link list).



Analysis of Stack Operations(Array based stack): 
1. Insert: O(1)
2. Delete: O(1)
3. Search: O(n)
4. Read: O(n)

Practical Example:
In the stack.py, I created simple linter which check if for every open bracket there is a close one. The linter works as followed:

1. the linter would go on every line in the code until its find a brace
2. if we find opening brace, we add it to the stack.
3. if we find another brace we check:
  * if its an opening brace we would add it to the stack
  * if its a closing brace we would check if it has the same type to the element in the stack, if not we rise an error.
  * if it has, we pop element from the stack
4. if we finish the file and there are elements in the stack, its mean that we are missing a brace.

since you are only allowed to insert or remove data from the top of the stack.