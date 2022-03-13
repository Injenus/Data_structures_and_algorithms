# Data Structures
import random

# Arrays
# ищём второе наименьшее
lst = [] # ищём второе наименьшее
for i in range(20):
    lst.append(random.randint(-10, 20))
print(lst)
if lst[0] <= lst[1]:
    m1, m2 = lst[0], lst[1]
else:
    m1,m2=lst[1], lst[0]
for el in lst:
    if el <= m1 and el <= m2:
        m2 = m1
        m1 = el
    elif el >= m1 and el <=m2:
        m2=el
lst.sort()
print(lst,m1,m2)


# Stacks
# Queues
# Linked lists
# Graphs


# Counts
# Bors (in essence, these are also trees, but they should be considered separately in value).
# Hash tables
