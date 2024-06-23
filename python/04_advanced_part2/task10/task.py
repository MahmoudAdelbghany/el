file = open('file.txt', 'r')
print(len(file.read().split()))
file.close()