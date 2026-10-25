"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

def status_of(percent):
    """Checks the status using the percent."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check_record(value, limit):
    """Calculates the difference, percent and status."""
    difference = limit - value
    percent = value / limit * 100
    status = status_of(percent)
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Prints the report for a record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Limit      : {limit}")
    print(f"Value      : {value}")
    print(f"Status     : {status}")
    print(f"Difference : {difference:>10.2f}")
    print(f"Percent    : {percent:>10.2f}%")
    print("=" * 34)

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    """Loads records from a file."""
    records = []

    with open(path) as f:
        for line in f:
            parts = line.strip().split(",")

            record = {
                "label": parts[0],
                "value": float(parts[1]),
                "limit": float(parts[2])
            }

            records.append(record)

    return records


records = load_records("records.txt")




# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
count = 0

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])

    print_report(record["label"], record["value"], record["limit"], difference, percent, status)

    if status == "OVER LIMIT":
        count += 1

print("Over limit:", count)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
