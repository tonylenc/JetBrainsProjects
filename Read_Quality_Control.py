import gzip


def get_info(path):
    with gzip.open(path, "r") as archive:
        dna_strands = archive.readlines()[1::4]

    dna_lengths, gc_content, undefined = [], [], []
    amount = len(dna_strands)
    for dna in dna_strands:
        dna = dna.decode().strip()
        dna_lengths.append(len(dna))
        gc_content.append(
            round((dna.count("G") + dna.count("C")) / len(dna) * 100, 2))
        if "N" in dna:
            undefined.append(round(dna.count("N") / len(dna) * 100, 2))

    return {"reads_amount": amount,
            "average_length": round(sum(dna_lengths) / amount),
            "repeats": amount - len(set(dna_strands)),
            "undefined_amount": len(undefined),
            "GC_average": round(sum(gc_content) / amount, 2),
            "Ns_per_read": round(sum(undefined) / amount, 2)}


def display(selected):
    print("Reads in the file = ", selected["reads_amount"],
          "\nReads sequence average length = ", selected["average_length"],
          "\n\nRepeats = ", selected["repeats"],
          "\nReads with Ns = ", selected["undefined_amount"],
          "\n\nGC content average = ", selected["GC_average"], "%",
          "\nNs per read sequence = ", selected["Ns_per_read"], "%", sep="")


def main():
    file_1, file_2, file_3 = get_info(
        input()), get_info(input()), get_info(input())
    if file_1["GC_average"] >= file_2["GC_average"] and file_1["GC_average"] >= file_3["GC_average"]:
        display(file_1)
    elif file_2["GC_average"] >= file_1["GC_average"] and file_2["GC_average"] >= file_3["GC_average"]:
        display(file_2)
    else:
        display(file_3)


if __name__ == "__main__":
    main()
