from collections import Counter, defaultdict, deque


########### Counter: zählt  #######
files = ["a.pdf", "b.pdf", "c.csv", "names.csv", "numbers.pdf", "x.png"]
extensions = [file.split(".")[-1] for file in files]
c = Counter(extensions)
print(c.most_common(2))  # [('pdf', 3), ('csv', 2)]

########### Default Dict  ############
groups = defaultdict(list)
users = [("Max", "Admin"), ("Peter", "Admin"), ("Alice", "Devs")]

for username, group in users:
    groups[group].append(username)

print(groups)

########## Deque #######
jobs = deque(["Doc1.txt", "Doc2.txt", "Doc3.txt"])
jobs.rotate(1)
print(jobs)

last_logs = deque(maxlen=5)
for i in range(1, 11):
    last_logs.append(f"Logeintrag {i}")

print(last_logs)
