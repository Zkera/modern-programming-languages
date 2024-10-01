d = dict()
d["a"] = ["1"]
for i in range(int(input())):
    str_line = input().split()
    if not (str_line[0] in d):
        d[str_line[0]] = list()
    d[str_line[0]].append(str_line[2])
print(d)
max_login = "a"
for key in d.keys():
    if len(d[key])> len(d[max_login]):
        max_login = key
print("\n\nanswer -", max_login)
#admin 11.09.2024 193.168.0.1
