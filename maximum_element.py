"""

You have an empty sequence, and you will be given N queries. Each query is one
of these three types:

    1 x  -Push the element x into the stack.
    2    -Delete the element present at the top of the stack.
    3    -Print the maximum element in the stack.

Input Format
The first line of input contains an integer, N. The next N lines each contain an
above mentioned query. (It is guaranteed that each query is valid.)

Output Format
For each type 3 query, print the maximum element in the stack on a new line.

"""

stack = []
max_element = 0

for i in range(int(raw_input())):
    query = raw_input().split()
    if query[0] == '1':
        value = int(query[1])
        stack.append(value)
        max_element = max(max_element, value)
    elif query[0] == '2':
        del_element = stack.pop()
        if del_element == max_element:
            max_element = max(stack + [0])
    else:
        print max_element
