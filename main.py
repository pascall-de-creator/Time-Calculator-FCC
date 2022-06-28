from time_calculator import add_time
from unittest import main

print(add_time("11:06 PM", "2:02"), "\n")

print(add_time("3:00 PM", "3:10"), "\n")

print(add_time("11:30 AM", "2:32", "Monday"), "\n")

print(add_time("11:43 AM", "00:20"), "\n")

print(add_time("10:10 PM", "3:30"), "\n")

print(add_time("11:43 PM", "24:20", "tueSday"), "\n")

print(add_time("6:30 PM", "205:12"), "\n")

main(module='test_module', exit=False)