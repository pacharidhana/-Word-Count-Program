# Word Count Program

# Get input from user
text = input("Enter a paragraph of text:\n")

# Convert text to lowercase and split into words
words = text.lower().split()

# Create a dictionary to store word counts
word_count = {}

# Count occurrences
for word in words:
    word = word.strip('.,!?()"')  # remove punctuation
    word_count[word] = word_count.get(word, 0) + 1

# Display the word counts
print("\nWord Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
