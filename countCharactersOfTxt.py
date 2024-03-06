# Define the Spanish alphabet
spanish_alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Create a dictionary to store the letter counts
letter_counts = {letter: 0 for letter in spanish_alphabet}

# Open the input file
with open("input.txt", "r", encoding="utf-8") as file:
    # Read the contents of the file
    text = file.read().lower()

    # Count the occurrences of each letter
    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1

# Calculate the total number of letters
total_letters = sum(letter_counts.values())

# Sort the letter counts in descending order
sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

# Open the output file
with open("output.txt", "w", encoding="utf-8") as file:
    # Write the letter counts and percentages to the file in descending order
    for letter, count in sorted_counts:
        percentage = (count / total_letters) * 100
        file.write(f"{letter}: {count} ({percentage:.2f}%)\n")