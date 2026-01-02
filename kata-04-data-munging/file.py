import utils
from utils import rangeTop as lowestTempSpread
from utils import resultValue as lowestSpreadDay

def filter_columns(column):
    return column.strip()

# Read and split data
rows = utils.read_file("weather.dat")

# Filter valid rows
lines = filter(filter_columns, rows)

print("lines", lines)

computationLines = []

for (index, line) in enumerate(lines):
    cutLine = line.strip()

    columnNumber = cutLine[0:2].strip()
    maxTemp = cutLine[3:8]
    minTemp = cutLine[9:14]

    try:
        tempSpread = int(maxTemp) - int(minTemp)
        computationLines.append([columnNumber, tempSpread])
    except Exception as X:
        print("Invalid input: cannot be converted - ", X)

for day in computationLines:
    if day[1] < lowestTempSpread:
        lowestSpreadDay = day[0]
        lowestTempSpread = day[1]

print("lowestSpreadDay", lowestSpreadDay, "lowestTempSpread", lowestTempSpread)

# Learning Results:
# Refreshed knowledge around data types, map, filter, sort, slicing and more methods
