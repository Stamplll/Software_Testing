def alternate(s):
    unique_chars = list(set(s))
    max_len = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1 = unique_chars[i]
            c2 = unique_chars[j]

            
            filtered = [c for c in s if c == c1 or c == c2]

            
            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    valid = False
                    break

            if valid and len(filtered) > 1:
                max_len = max(max_len, len(filtered))

    return max_len

# if __name__ == '__main__':
#     length_s = int(input())
#     s = input()
#     print(alternate(s))