# alice in wonderland is a relatively short text, but it's good enough for most statistical tests.
# Note: it has \r\n style line endings

# curl http://www.gutenberg.org/files/11/11.txt > alice_in_wonderland.txt
corpus = open("alice_in_wonderland.txt", "rb").read()

freqs = [0]*0x100

for char in corpus:
	freqs[char] += 1

# convert values to a fraction of all characters
total = sum(freqs)
freqs = [f/total for f in freqs]

# print nicely
print("byte_freqs = [")
for row_start in range(0, 0x100, 8):
	print("\t" + ", ".join("{:.6f}".format(f) for f in freqs[row_start:row_start+8]) + ",")
print("]")
print()

# construct a character freqency dictionary
freq_dict = {}
for c, f in enumerate(freqs):
	if f:
		freq_dict[chr(c)] = f

# print nicely
print("char_freqs = {")
for c, f in sorted(freq_dict.items()):
	print("\t{}:\t{:.6f},".format(repr(c), f))
print("}")
