# DNA Sequence Analyzer

def validate_dna(sequence):
    valid_bases = {"A", "T", "G", "C"}
    sequence = sequence.upper()
    for base in sequence:
        if base not in valid_bases:
            return False
    return True

def analyze_dna(sequence):
    sequence = sequence.upper()

    count_A = sequence.count("A")
    count_T = sequence.count("T")
    count_G = sequence.count("G")
    count_C = sequence.count("C")

    total_length = len(sequence)

    gc_content = ((count_G + count_C) / total_length * 100) if total_length > 0 else 0
    at_content = ((count_A + count_T) / total_length * 100) if total_length > 0 else 0

    if gc_content > 50:
        richness = "GC-rich"
    elif at_content > 50:
        richness = "AT-rich"
    else:
        richness = "Balanced"

    results = {
        "Total Length": total_length,
        "A": count_A,
        "T": count_T,
        "G": count_G,
        "C": count_C,
        "GC Content (%)": round(gc_content, 2),
        "AT Content (%)": round(at_content, 2),
        "Richness": richness
    }

    return results

def print_dna_report(results):
    print("\n==== DNA Sequence Analysis ====")
    for key, value in results.items():
        print(f"{key}: {value}")
    print("================================")

def main():
    dna_sequence = input("Enter a DNA sequence: ").upper()

    if validate_dna(dna_sequence):
        results = analyze_dna(dna_sequence)
        print_dna_report(results)
    else:
        print("❌ Error: Invalid DNA sequence. Please enter only A, T, G, or C.")

if __name__ == "__main__":
    main()
