def filter_columns(column):
    return column.strip()

# Read
f = open("weather.dat")
data = f.read()

# Split Lines
columns = data.split("\n")

# Filter valid rows
lines = filter(filter_columns, columns)

computationLines = []

for (index, line) in enumerate(lines):
    cutLine = line.strip()

    columnNumber = cutLine[0:2]
    maxTemp = cutLine[3:8]
    minTemp = cutLine[9:14]

    try:
        tempSpread = int(maxTemp) - int(minTemp)
        print("tempSpread", tempSpread)

        computationLines.append([columnNumber, tempSpread])
    except:
        print("Invalid input: cannot be converted")

print("computationLines,", computationLines)


