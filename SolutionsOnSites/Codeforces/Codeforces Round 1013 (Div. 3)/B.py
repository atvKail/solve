import sys

input = sys.stdin.readline


t = int(input().strip())
for _ in range(t):
    n, x = map(int, input().split())
    skls = list(map(int, input().split()))
    skls.sort(reverse=True)
    teams = 0
    team_size = 0

    for skill in skls:
        team_size += 1

        if team_size * skill >= x:
            teams += 1
            team_size = 0
    print(teams)
