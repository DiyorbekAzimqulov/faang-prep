"""
stack has push, pop, top, getMin
we need to be able to get min value in constant time. 
we need to implement stack with getMin in constant time
how can we do this?
we can keep track of min value in a separate stack
when we push a value, we need to check whether stack is empty or not
if stack is empty, then we push the value to both stack and min stack
if stack is not empty, then we get the value of min stack and compare it with the value we are pushing
if value is less than min value, then we push the value to min stack
else then we simple push the value to stack

when we pop the value, we need to check whether the value we are popping is the min value or not
if it is min value, then we need to pop the value from min stack as well
else we simply pop the value from stack

when we get the min value, we simply return the top value of min stack
"""
