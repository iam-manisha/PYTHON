s = input()
new = ''

for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
        new += str(ip)
    else:
        new += s[ip]

print(new)