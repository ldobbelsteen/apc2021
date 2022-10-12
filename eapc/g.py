# MF6, 404NAMENOTFOUND

source = input().split("/")
dest = input().split("/")
i = 0
k = len(source)
j = len(dest)
n = min(k, j)
while i < n:
    if not source[i] == dest[i]:
        break
    i += 1
start = source[0:i]
end = []

if len(start) != k:
    j = 0
    while j <= (n - i):
        if not source[len(source)-j-1] == dest[len(dest)-j-1]:
            break
        j += 1
    end = source[len(source)-j:len(source)]
middleS = source[i: -len(end) if len(end) > 0 else len(source)]
middleD = dest[i:-len(end) if len(end) > 0 else len(dest)]
output = "/".join(start)
if len(start) > 0:
    output += "/"
output2 = "/".join(end)
if len(end) > 0:
    output2 = "/" + output2
print(output + "{" + "/".join(middleS) +
      " => " + "/".join(middleD) + "}" + output2)
