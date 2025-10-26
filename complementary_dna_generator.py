# Complementary DNA Strand Generator

def validate_sequence(sequence):
    sequence = sequence.upper()
    for base in sequence:
        if base not in "ATGC":
            return False
    return True


def get_complement(dna):
    dna = dna.upper()
    complement = ""
    for base in dna:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "C":
            complement += "G"
        elif base == "G":
            complement += "C"
    return complement


def main():
    dna = input("Please enter a DNA sequence: ").upper()

    if validate_sequence(dna):
        complement = get_complement(dna)
        print("\nDNA Complement Generator")
        print("--------------------------")
        print(f"Original DNA Sequence: {dna}")
        print(f"Complementary DNA Sequence: {complement}")
    else:
        print("Error: Invalid DNA sequence. Only A, T, G, C are allowed.")


if __name__ == "__main__":
    main()
