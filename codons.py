def create_codon_dict(file_path):
    
    final = {}
    with open(file_path, "r") as y:
      rows = y.readlines()
    for r in rows:
        x = r.strip().split("\t")
        final[x[0]] = x[2]

    return final
