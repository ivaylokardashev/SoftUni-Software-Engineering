usernames = input().split(", ")
banned_chars = [":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "`"]
legal_usernames = []
flag = False
for user in usernames:
    if 3 <= len(user) <= 16:
        for char in user:
            if ((48 <= ord(char) or ord(char) > 122) and char not in banned_chars) or ord(char) == 45:
                flag = True
                continue
            flag = False
            break
        if flag:
            legal_usernames.append(user)

for username in legal_usernames:
    print(username)
