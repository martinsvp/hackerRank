n = int(input())

if n % 2 != 0:
    res = "Weird"
elif 2 <= n <= 5:
    res = "Not Weird"
elif 6 <= n <= 20:
    res = "Weird"
else:
    res = "Not Weird"

print(res)