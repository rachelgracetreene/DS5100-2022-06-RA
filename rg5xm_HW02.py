# Title: DS5100 HW02
# Name: Rachel Grace
# UserID: rg5xm

# Task 1
gradebook = {'Jon':95, 'Mike':84, 'Jaime':99}
gradebook

# Task 2
gradebook['Mike']

# Task 3
gradebook['Jeff']

# Task 4
nameslist = ['Alex', 'Patrick', 'Tom', 'Joe', 'Alex']
nameslist

# Task 5
nameslist.sort()
nameslist

# Task 6
namesset = {'Alex', 'Patrick', 'Tom', 'Joe', 'Alex'}
namesset

# Task 7a
td = [2, 4, 1, 3, 1]
td

# Task 7b
index = 0 # start index
tdodd = []
for index in range(len(td)):
    if ((td[index]) % 2) == 1:
        tdodd.append(td[index])
    index += 1
tdodd

# Task 7c
index = 0
tdmore = []
for index in range(len(td)):
    if (td[index]) > 1:
        tdmore.append(td[index])
    index += 1
tdmore
