def alternatingCharacters(s):
    count = 0
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count

# if __name__ == '__main__':
#     q = int(input())
#     if 1 <= q <= 10:
#         for num in range(q):
#             s = input()
#             if 1 <= len(s) <= 10**5:
#                 print(alternatingCharacters(s))