import utils

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

# TODO: Outsource
smallestRange = 999
smallestRangeTeam = ""

for teamStats in footballTeamsStats:
    try:
        goalsFor = int(teamStats[6])
        goalsAgainst = int(teamStats[8])

        currentRange = abs(goalsFor - goalsAgainst)

        if currentRange < smallestRange:
            smallestRange = currentRange
            smallestRangeTeam = teamStats[1]
    except Exception as X:
        print(X)

print("The team with the smallest difference is - ", smallestRangeTeam)
print("Range", smallestRange)
