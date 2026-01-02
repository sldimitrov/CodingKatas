def filterTokens(row):
    if row == "":
        return

    return row

# Read data
f = open("football.dat")
data = f.read()

# Structure the data
rows = data.split("\n")

formattedRows = []
footballTeams = []
footballTeamsStats = []

for row in rows:
    formatRow = row.strip().split(" ")

    counter = 0
    currentRowFormatted = []

    for i, token in enumerate(formatRow):
        if token != "":
            print(counter, repr(token))
            currentRowFormatted.append(token)
            counter += 1

    print("counter", counter)

    if counter == 8:
        print("These are footbal teams")
        footballTeams.append(currentRowFormatted)

    if counter == 10:
        print("This is a football team stats")
        footballTeamsStats.append(currentRowFormatted)

print("footballTeams", footballTeams)
print("footballTeamsStats", footballTeamsStats)
