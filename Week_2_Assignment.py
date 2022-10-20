import re

handle = open("C:\my_projects\Courses\python-to-access-web-data\week_2_assignment_sample.txt")

numbers_list = []
for line in handle:
    line = line.rstrip()
    # print(line)
    extracted_numbers = re.findall("([0-9]+)",line)
    if len(extracted_numbers) < 1:
        continue
    
    for i in extracted_numbers:
        numbers_list.append(int(i))

print(sum(numbers_list))
    
