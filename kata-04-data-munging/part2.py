# Read data
f = open("football.dat")
data = f.read()

# Split data into rows
rows = data.split("\n")

formattedRows = []
footballTeams = []
footballTeamsStats = []

for row in rows:
    formatRow = row.strip().split(" ")

    counter = 0
    currentRowFormatted = []

    # Structure the data
    for i, token in enumerate(formatRow):
        if token != "":
            # print(counter, repr(token))
            currentRowFormatted.append(token)
            counter += 1

    # TODO: Change the condition for real-world scenarios
    if counter == 8:
        print("The list of football teams: ", currentRowFormatted)
        footballTeams.append(currentRowFormatted)

    if counter == 10:
        # print("Add the team of", currentRowFormatted[1])
        footballTeamsStats.append(currentRowFormatted)

smallestRange = 999
smallestRangeTeam = ""

# Find the team with the smallest difference between F and A goals
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
