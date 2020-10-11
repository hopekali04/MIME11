alphabet = "abcdefghijklmnopqrstuvwxyz"

# convert between letters and numbers up to 26
def number_to_letter(i):
	return alphabet[i%26] # %26 does the wrap-around

def letter_to_number(l):
	return alphabet.find(l) # index in the alphabet

# How to encode a single character (letter or not)
def caesar_shift_single_character(l, amount):
	i = letter_to_number(l)
	if i == -1: # character not found in alphabet
		return "" # remove it, it's space or punctuation
	else:
		return number_to_letter(i + amount) # Caesar shift

# How to encode a full text
def caesar_shift(text, amount):
	shifted_text = ""
	for char in text.lower(): # also convert uppercase letters to lowercase
		shifted_text += caesar_shift_single_character(char, amount)
	return shifted_text

### MAIN PROGRAM ###

message = """
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door—
"'Tis some visitor," I muttered, "tapping at my chamber door—
Only this and nothing more."
"""

code = caesar_shift(message, 2)
print(code)
print ("\n")
import matplotlib.pyplot as plt
alphabet = "abcdefghijklmnopqrstuvwxyz"

code = """
yfdpcpoplhhwdpssbjnsqvtlcpzpxqugtjphvgotuvwxufgoqigxwgkskduooyeuoue
fjlnmsqpgxrmcseeliswdheywseqgcbeothskxdzekgxmmkildjnaqbukprpfaaknsu
qpdwayqaqfxsoapvsgreqydqjnkpjghvrkygtidzibhrqkmocukhcunpjcazzvomtsc
fgycwfltmiegaejwcqrgsnxxcbtcrckufwsdxdhbxgppxcuzapbdhftzmugryfseavv
bssqlxanvmfwwzityziixasivzkmvtfczqmdgkabcnjbyhaoealengfptuedlmvryeb
titbwqkekzdpmbtiphdkwwiduassvbgalxgrfhrjrjplxpujrprqzcpcdqsjorigazt
kwwlnwbjryrzhgcttroyemuwwixwufymnknirzmexyowobvardlqktzajzoijwulomg
ztefdpftjealzapcgipgaaspuzxklvd
"""

letter_counts = [code.count(l) for l in alphabet]
letter_colors = plt.cm.hsv([0.8*i/max(letter_counts) for i in letter_counts])

plt.bar(range(26), letter_counts, color=letter_colors)
plt.xticks(range(26), alphabet) # letter labels on x-axis
plt.tick_params(axis="x", bottom=False) # no ticks, only labels on x-axis
plt.title("Frequency of each letter")
plt.savefig("output.png")
