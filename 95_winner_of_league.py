# 

'''

You are given the scores of a football league among a set of teams. You need to find the winner of the league and print the name of winner and points earned by the team. Each team gets 3 points for a win, 1 point for a draw and 0 for a loss. The name of the teams is represented as upper case character viz. A B...Z.

Constraints
There will only be one team which gets the highest points

Input
There are many lines in the input.
The first line contains an integer, N, representing number of teams in the league. The next (N*(N-1))/2
lines contain three space separated strings <Team1, Team2, Score>
Here,
Team1 is the name of the home team.
Team2 is the name of the away team.

Score represents the score of the match, (M-N), where M represents the score of the home team and N represents the score of the away team.

Output
The output should have two lines.
The first line should contain a character representing the name of the leader team.
The second line containing an integer representing the points won by the leader team.

Input
3
A B 2-1
B C 5-6
C A 2-1
Output
C
6
Explaination
A has won 1 match : 3 points
B has won 0 match : 0 points
C has won 2 match : 6 points

'''

n = int(input())
matches = (n*(n-1))//2

teams= {}

for i in range(matches):
    match = input().split(' ')
    team1 = match[0]
    team2 = match[1]
    score1, score2 = tuple(map(int, match[2].split('-')))
    if score1 == score2:
        score1, score2 = 1,1
    else:
        score1 = 3 if score1>score2 else 0
        score2 = 3 if score1<score2 else 0
    if teams.get(team1):
        teams[team1] += score1
    else:
        teams[team1] = score1
    if teams.get(team2):
        teams[team2] += score2
    else:
        teams[team2] = score2

sortedscore = sorted(teams.items(), key=lambda x: x[1])
print(sortedscore[n-1][0])
print(sortedscore[n-1][1])

