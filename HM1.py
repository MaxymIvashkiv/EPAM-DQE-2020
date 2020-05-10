import re, collections
path = input('Enter path: ')
filename = input('Enter file name: ')
while True:
    try:
        myfile = open(f"{path}\{filename}", "r")
    except Exception:
        print('Please enter correct path/file name')
        path = input('Enter path: ')
        filename = input('Enter file name: ')
    else:
        break
    #безкінечний цикл поки не буде введено правильний шлях і назву файла
cnt = collections.Counter()
n = re.findall('(\w+)\s', myfile.read().lower())
for word in n:
    cnt[word] += 1
final = dict(collections.OrderedDict(sorted(dict(cnt).items(), key=lambda t: t[0])))
myfile.close()
for keys, values in final.items():
    print(keys, ':', values)


