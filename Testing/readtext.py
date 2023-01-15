with open("token.txt", 'r') as file:
    token = file.read().replace('\n', '')

print(token)
