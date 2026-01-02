import utils
from utils import rangeTop as smallestRange
from utils import resultValue as smallestRangeTeam

# Read and split data
rows = utils.read_file("football.dat")

# Define data lists
footballTeams = []
footballTeamsStats = []

for row in rows:
    formattedRow = utils.format_rows(row)

    if not formattedRow:
        continue

    counter = 0
    currentRow = []

    if "team" in formattedRow[0].lower():
        footballTeams.append(formattedRow)
    else:
        footballTeamsStats.append(formattedRow)

# Optimise this part of the code
for teamStats in footballTeamsStats:
    if len(teamStats) < 10:
        continue

    try:
        goalsFor = int(teamStats[6])
        goalsAgainst = int(teamStats[8])

        currentRange = abs(goalsFor - goalsAgainst)

        if currentRange < smallestRange:
            smallestRange = currentRange
            smallestRangeTeam = teamStats[1]
    except Exception as X:
        print(X)

# Result
if smallestRangeTeam:
    print(f"{smallestRangeTeam} has the smallest range of {smallestRange}")
else:
    print("There was an error trying to find the Team with the smallest range")
