a, b = input(), input()
for character in a:
	b = b.replace(character, '', 1)
print(b)