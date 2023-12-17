import re

def load_values(filename):
    values = {}
    with open(filename, 'r') as file:
        for line in file:
            letter, score = line.split()
            values[letter] = int(score)
    return values

def calculate_score(letter, position):
    if position == 0:
        return 0
    elif position == 1:
        return values[letter]
    elif position == 2:
        return values[letter] + 3
    else:
        return values[letter] + 6
    
def process_name(name):
    words = re.findall(r'\b\w+\b', name.upper())
    abbreviations = set()

    for word in words:
        first_letter = word[0]
        for i in range(len(word) - 1):
            position = i + 1
            if i + 1 < len(word):  # Check if the next index is within the bounds of the word
                score = calculate_score(word[i], position)
                abbrev = f'{first_letter}{word[i]}{word[i+1]}'
                abbreviations.add((abbrev, score))

    return abbreviations

def main():
    input_filename = input("Enter the input filename (with .txt extension): ")
    output_filename = input("Enter your surname: ").lower() + "_" + input_filename[:-4] + "_abbrevs.txt"

    try:
        with open(input_filename, 'r') as file:
            names = file.readlines()

        global values
        values = load_values("values.txt")

        results = {}
        for name in names:
            abbreviations = process_name(name)
            for abbrev, score in abbreviations:
                if abbrev not in results or results[abbrev] > score:
                    results[abbrev] = score

        with open(output_filename, 'w') as file:
            for abbrev, score in sorted(results.items(), key=lambda x: x[1]):
                file.write(f'{abbrev}: {score}\n')

        print(f"Results written to {output_filename}")

    except FileNotFoundError:
        print("File not found. Please make sure the input file exists.")

if __name__ == "__main__":
    main()
