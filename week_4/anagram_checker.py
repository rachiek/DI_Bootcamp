class AnagramChecker:
    def __init__(self, file_path):
        """Load the word list from the given file path."""
        self.words = set()
        with open(file_path, "r", encoding="utf-8") as f:
            self.words = {word.strip().lower() for word in f if word.strip()}

    def is_valid_word(self, word):
        """Return True if the word exists in the loaded word list."""
        if not word or not isinstance(word, str):
            return False
        return word.strip().lower() in self.words

    def is_anagram(self, word1, word2):
        """Return True if word1 and word2 are anagrams and not identical."""
        if not word1 or not word2:
            return False
        word1_normalized = word1.strip().lower()
        word2_normalized = word2.strip().lower()
        if word1_normalized == word2_normalized:
            return False
        return sorted(word1_normalized) == sorted(word2_normalized)

    def get_anagrams(self, word):
        """Return a list of valid anagrams for the given word."""
        if not word or not isinstance(word, str):
            return []
        word_normalized = word.strip().lower()
        return [candidate for candidate in self.words if self.is_anagram(word_normalized, candidate)]
  