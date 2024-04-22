# 

'''

A coding competition was conducted in company with e employees. Data of employees who participated and who did not participate in the competition is available. There were three problems in the coding competition. Data as mentioned below is available The number of employees who have solved only the first, only the second and only the third problem are equal.

pl employees who solved the first ,second problem.
p2 employees who solved the second , third problem.
p3 employees who solved the third first problem.
q employees who solved all the 3 problems.
r employees who did not participate in competition.

Answer the following questions based on data.

How many employees have solved the first problem?
How many employees have solved exactly one of the 3 problems?

Refer this Image - https://i.imgur.com/tEKYtqN.png


Input
30
26
28
14
43
345

Output
126
246

'''


p1 = 30
p2 = 26
p3 = 28
q = 14
r = 43
total = 345

participated = total - r
s1 = p1-q
s2 = p2-q
s3 = p3-q
x = (participated-(s1+s2+s3+q))//3

print(x+q+s1+s3)
print(x*3)