# nstructions:
# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.
# Part I: Analyzing a Simple String

# Step 1: Create the Text Class
# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.content).

# Step 2: Implement word_frequency Method
# Create a method called word_frequency(word).
# Split the text content into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

# Step 3: Implement most_common_word Method
# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.

# Step 4: Implement unique_words Method
# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.
# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method
# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.

class Text:
    def __init__(self, content):
        self.content = content

    def word_frequency(self, word):
        words = self.content.split()
        count = words.count(word)
        if count == 0:
            return f"{word} was not found in text!"
        return count

    def most_common_word(self):
        words = self.content.split()
        if not words:
            return None
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        return max(frequency, key=frequency.get)

    def unique_words(self):
        words = self.content.split()
        unique_words = set(words)
        return list(unique_words)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        return cls(content)

if __name__ == "__main__":
    document = Text.from_file("text.txt")
    print("Text content:")
    print(document.content)
    print()
    print("Frequency of 'text':", document.word_frequency("text"))
    print("Most common word:", document.most_common_word())
    print("Unique words:", document.unique_words())
