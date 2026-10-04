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

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("whats your name?")
value = float(input("whats the first number?"))
limit = float(input("whats the second number?"))
   


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

status = "" # replace with your if / else (or if / elif / else)

difference = limit  - value 
percent = (value / limit) * 100
secondDiff = 100 - percent

if value > limit:
    status = "over limit" 
else:
    if value < limit:
        status = "under limit" 

if status == "over limit" :
    print(f"over limit by {percent}%")
else:
    print("not over the limit")
    print(f"warning. {secondDiff}% will reach the limit ")


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 39)
print(f"  RECORD CHECK  -  {label}")
print("=" * 39)
print(f"Limit      : {limit}")
print(f"Value      : {value}")
print(f"Status     : {status}")

print(f"Difference : {difference:>10.2f}")
print(f"Percent    : {percent:>10.2f}%")
print(f"warning    : {secondDiff:>10.2f}% until limit")

print("=" * 39)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] the error is "ZeroDivisionError: division by zero" Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
