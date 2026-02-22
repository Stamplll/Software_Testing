def funnystring(s):
    r = s[::-1]

    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(r[i]) - ord(r[i+1])):
            return "Not Funny"
    return "Funny"


# if __name__ == '__main__':
#     q = int(input())
#     if 1 <= q <= 10:
#         for _ in range(q):
#             s = input().strip()
#             if 2 <= len(s) <= 10000: 
#                 print(funnystring(s))