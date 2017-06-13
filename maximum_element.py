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

N = int(raw_input())
stack = []

for i in range(N):
    query = raw_input().split(' ')
    if query[0] == '1':
        stack.append(int(query[1]))
    elif query[0] == '2':
        del stack[-1]
    else:
        print max(stack)