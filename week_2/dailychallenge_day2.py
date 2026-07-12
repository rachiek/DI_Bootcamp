MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Convert matrix_string to a 2D list (matrix)
lines = [line for line in MATRIX_STR.strip().splitlines()]
# normalize rows to the same length by padding with spaces
max_len = max(len(line) for line in lines)
matrix = [list(line.ljust(max_len)) for line in lines]

# Step 2: Iterate through columns
# ... code to iterate through columns ...

# Step 3: Filter alpha characters
# ... code to filter alpha characters ...

# Step 4: Replace symbols with spaces
decoded_message = ""
# ... code to replace symbols with spaces ...

# Step 5: Print the decoded message
print(decoded_message)
# Step 3 & 4: Read column-wise, keep letters, replace non-letters with spaces
chars = []
for col in range(max_len):
	for row in range(len(matrix)):
		ch = matrix[row][col]
		if ch.isalpha():
			chars.append(ch)
		else:
			chars.append(' ')

# Step 5: collapse multiple spaces and print decoded message
decoded = ''.join(chars)
decoded_message = ' '.join(decoded.split())
print(decoded_message)