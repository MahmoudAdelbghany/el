list = ['こんにちは', 'さようなら', 'おはよう', 'こんばんは', 'おやすみ']
file = open('file.txt', 'w')
file.write('\n'.join(list))
file.close()
file = open('file.txt', 'r')
print(file.read().split())
file.close()
