def suffixarray(s):
	suffix=[(s[i:],i) for i in range(len(s))]
	suffix.sort(key=lambda x:x[0])
	return suffix
print(suffixarray("banana"))
