# DNA to RNA Transcription with Validation

def validate_dna(sequence):

    sequence = sequence.upper()
    for base in sequence:
        if base not in "ATGC":
            return False
    return True

def transcribe_dna(dna):

    dna = dna.upper()
    rna = dna.replace("T", "U")
    return rna

def main():
    dna_seq = input("Enter a DNA sequence: ")

    if validate_dna(dna_seq):
        rna_seq = transcribe_dna(dna_seq)
        print(f"\nOriginal DNA: {dna_seq.upper()}")
        print(f"Transcribed RNA: {rna_seq}")
    else:
        print("Error: Invalid DNA sequence. Only A, T, G, C are allowed.")

# Run the program
if __name__ == "__main__":
    main()
