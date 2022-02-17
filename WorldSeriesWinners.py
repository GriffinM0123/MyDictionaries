infile = open("WorldSeriesWinners.txt", "r")
infile2 = open("WorldSeriesWinners.txt", "r")

count = 0

teamN = {}

yearWon = {}


for team in infile:
    team = team.strip()
    if team in teamN:
        teamN[team] = teamN[team] + 1
    else:
        teamN[team] = 1

print(teamN)



yr = 1902

for team in infile2:
    team = team.rstrip("\n")
    if yr == 1903:
        yr += 2
        yearWon[yr] = team
    elif yr == 1993:
        yr += 2
        yearWon[yr] = team
    else:
        yr += 1
        yearWon[yr] = team 
yearWon[yr] = team

print(yearWon)


prompted_yr = input("What year do you want me to find the World Series Winner for?")
print(yearWon[team][prompted_yr])