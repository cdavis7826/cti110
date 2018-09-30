# Write a program that will keep a running total of bugs collected for five days.
# 9/27/18
# CTI-110 P4T2 - Bug Collector
# Chad Davis
# (Enter the value of "Total",
#  write the "for" loop and "range" for days collected,
#  Show total number of bugs collected.)



# Initialize the accumulator.
total = 0

# Get the bugs collected for each day from collector.
for day in range(1, 6):
    print ('Enter the number of bugs collected on day', day)
    bugs = int(input())
    total += bugs

# Show how many bugs have been collected.
print ('You have collected a total of', total, 'bugs.')
