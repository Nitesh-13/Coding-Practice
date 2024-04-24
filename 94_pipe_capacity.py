#

'''

A plumber wants to check whether a pipe junction where N incoming pipes and M outgoing pipes are balanced, and, if not, needs to balance the junction by adding an input pipe or an output pipe of a suitable capacity. At the junction, there are a set of input pipes and a set of output pipes. Each pipe has a rated capacity and an actual capacity. The actual capacity for each pipe is lower than the rated capacity by a constant R, the "rust factor", which depends on the material of the pipe, and is the same for all the pipes
at the junction. 
For example, if the rated capacity is 65, and Ris 2, the actual capacity is 63.

A junction is balanced if the sum of the actual capacities of the input pipes is the same as the sum of the actual capacities of the output pipes. If it is not balanced, the plumber needs to add one input pipe or one output pipe to balance the junction, and determine the rated capacity of that added pipe.
Hel Here we have N incoming pipes and M outgoing pipes. The incoming pipes may be of different rated capacities. Similarly, the outgoing pipes may also be of different rated capacities.

Find the rated capacity of the pipe required to make the junction balanced. If the combined actual capacity of the incoming pipes is more than the combined actual capacity of the outgoing pipes then the plumber will need to add an outgoing pipe. Conversely, if the combined actual capacity of the incoming pipes is less than the combined actual capacity of the outgoing pipes then the plumber will need to add an incoming pipe.

If an outgoing pipe is added then denote its rated capacity as a negative number. If an incoming pipe is added then denote its rated capacity as a positive number.

Example 1:
Input:
3 3 2
85 75 95
70 80 45

Output:
-62

Explanation:
There are 3 input pipes, 3 output pipes, and the rust factor is 2.

Example 2:
Input:
5 6 1
10 26 33 40 50
20 7 53 25 45 10

Output
BALANCED

'''

inp = int(input())
out = int(input())
rf = int(input())

inpCapacity = 0
outCapacity = 0

for i in range(inp):
    inpCapacity+= int(input())
for i in range(out):
    outCapacity += int(input())

oc = ((outCapacity - out*rf) - (inpCapacity - inp*rf))
if oc < 0:
    oc = abs(oc) + rf
    oc = -oc
elif oc == 0:
    oc = 'BALANCED'
else:
    oc += rf
print(oc)
