rangeTop = 999
resultValue = ""

def read_file(path):
    f = open(path)
    return f.read().split("\n")

def format_rows(row):
    return row.strip().split()

