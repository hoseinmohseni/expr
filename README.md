# expr
Calculate mathematical expressions in Python

algorithm : 
Step 1: Create two stacks - the operand stack and the character stack.
Step 2: Push the character to the operand stack if it is an operand.
Step 3: If it is an operator, check if the operator stack is empty. 
Step 4: If the operator stack is empty, push it to the operator stack.
Step 5: If the operator stack is not empty, compare the precedence of the operator and the top character in the stack. 
If the character’s precedence is greater than or equal to the precedence of the stack top of the operator stack, then push the character to the operator stack.
Otherwise, pop the elements from the stack until the character’s precedence is less or the stack is empty.
Step 6: If the character is “(“, push it into the operator stack.
Step 7: If the character is “)”, then pop until “(” is encountered in the operator stack.



