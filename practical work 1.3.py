d = dict()
d["a"] = ["1"]
for i in range(int(input())):
    str = input().split()
    if not (str[0] in d):
    	d[str[0]] = list()
    d[str[0]].append(str[2])
print(d)
max = "a"
for key in d.keys():
	if len(d[key])> len(d[max]):
		max = key
print("\n\nanswer -", max)
#admin 11.09.2024 193.168.0.1