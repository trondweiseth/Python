import itertools
import argparse

def capitalize_first_letter(word):
    """Capitalize the first letter of a word."""
    if word:
        return word[0].upper() + word[1:]  # Capitalize first letter and leave the rest unchanged
    return word

def generate_combinations(words, numbers, capitalize_first=False):
    """Generate combinations by adding numbers to words in a controlled manner."""
    combinations = set()  # Use a set to store unique combinations

    # Generate all possible word combinations (both lowercase and capitalized)
    for r in range(1, len(words) + 1):
        for word_combination in itertools.permutations(words, r):
            # Combine word combinations into a string (lowercase version)
            word_combination_str = ''.join(word_combination)
            combinations.add(word_combination_str)  # Add lowercase combination

            # If capitalize_first is True, also yield the capitalized versions
            if capitalize_first:
                # Generate all possible capitalizations of the word combination
                for capitalized_combination in itertools.product(*[(w, capitalize_first_letter(w)) for w in word_combination]):
                    capitalized_combination_str = ''.join(capitalized_combination)
                    combinations.add(capitalized_combination_str)  # Add capitalized combination

            # If numbers are included, generate combinations with numbers as well
            if numbers:
                # Add numbers to the word combinations
                for number in numbers:
                    combinations.add(word_combination_str + number)  # Word followed by number
                    combinations.add(number + word_combination_str)  # Number followed by word
                    
                    # Handle combinations with special characters like "!"
                    if '!' in words:  # Check if special character '!' is in the words list
                        combinations.add(word_combination_str + number + "!")
                        combinations.add(number + word_combination_str + "!")
                    
                    # If capitalize_first is True, also generate combinations with the capitalized versions
                    if capitalize_first:
                        for capitalized_combination in itertools.product(*[(w, capitalize_first_letter(w)) for w in word_combination]):
                            capitalized_combination_str = ''.join(capitalized_combination)
                            combinations.add(capitalized_combination_str + number)
                            combinations.add(number + capitalized_combination_str)
                            if '!' in words:
                                combinations.add(capitalized_combination_str + number + "!")
                                combinations.add(number + capitalized_combination_str + "!")
            else:
                # Just yield combinations of words if no numbers are provided
                combinations.add(word_combination_str)

    # Yield all unique combinations from the set
    for combo in combinations:
        yield combo

def generate_numbers(min_digits=1, max_digits=4):
    """Generate sequential numbers with customizable digits, from min_digits to max_digits."""
    numbers = []
    # Loop through each digit length from min_digits to max_digits
    for length in range(min_digits, max_digits + 1):
        # Generate numbers with leading zeros for each length
        for i in range(0, 10**length):  # Start from 0, ensuring leading zeros
            # Use f-string formatting to ensure numbers are padded with leading zeros
            numbers.append(f"{i:0{length}d}")  # Example: 000, 001, 002, ..., 9999
    return numbers

if __name__ == "__main__":
    # Argument parser to handle command-line arguments
    parser = argparse.ArgumentParser(description="Generate all possible combinations of given words or characters.")
    parser.add_argument("input", type=str, help="Words or characters separated by ';'")
    parser.add_argument("--add-numbers", action="store_true", help="Include numbers in the combinations.")
    parser.add_argument("--min-digits", type=int, default=1, help="Minimum number of digits for numbers to be included.")
    parser.add_argument("--max-digits", type=int, default=4, help="Maximum number of digits for numbers to be included.")
    parser.add_argument("--capitalize-first-letter", action="store_true", help="Capitalize the first letter of each word in combinations.")
    
    args = parser.parse_args()
    
    # Parse the input into a list of words or symbols
    words = [item.strip() for item in args.input.split(';') if item.strip()]
    
    # Add numbers if the parameter is set
    if args.add_numbers:
        numbers = generate_numbers(args.min_digits, args.max_digits)
    else:
        numbers = []
    
    # Generate combinations and print them one by one
    for combo in generate_combinations(words, numbers, capitalize_first=args.capitalize_first_letter):
        print(combo)
