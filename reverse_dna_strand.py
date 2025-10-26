# Reverse DNA Strand Generator

def validate_dna(sequence):
    sequence = sequence.upper()
    for base in sequence:
        if base not in "ATGC":
            return False
    return True


def reverse_dna(dna):
    return dna[::-1]


def main():
    dna = input("Enter a DNA sequence: ").upper()

    if validate_dna(dna):
        reversed_sequence = reverse_dna(dna)
        print("\nReverse DNA Strand Generator")
        print("----------------------------")
        print(f"Original DNA Sequence:   {dna}")
        print(f"Reversed DNA Sequence:   {reversed_sequence}")
    else:
        print("Error: Invalid DNA sequence. Only A, T, G, C are allowed.")


if __name__ == "__main__":
    main()
