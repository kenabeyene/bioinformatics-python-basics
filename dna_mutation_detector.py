# DNA Mutation Detector

def validate_dna(sequence):

    sequence = sequence.upper()
    for base in sequence:
        if base not in "ATGC":
            return False
    return True


def find_mutations(dna1, dna2):

    mutations = []
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            mutations.append(i + 1)  # +1 for human-friendly numbering
    return len(mutations), mutations


def main():

    dna1 = input("Enter the first DNA sequence: ").upper()
    dna2 = input("Enter the second DNA sequence: ").upper()


    if not (validate_dna(dna1) and validate_dna(dna2)):
        print("Error: Invalid DNA sequence. Only A, T, G, C are allowed.")
        return

    if len(dna1) != len(dna2):
        print("Error: DNA sequences must be the same length.")
        return
    count, positions = find_mutations(dna1, dna2)

    print("\nDNA Mutation Analysis")
    print("---------------------")
    print(f"First DNA Sequence:  {dna1}")
    print(f"Second DNA Sequence: {dna2}")
    print(f"Number of mutations: {count}")
    if count > 0:
        print(f"Mutation positions: {positions}")
    else:
        print("No mutations found! ✅")


if __name__ == "__main__":
    main()
