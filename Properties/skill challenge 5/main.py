class DNABase:

    base = { "adenine", "cytosine", "guanine", "thymine"}

    def __init__(self, nucleotide):
        self.base = nucleotide

    def get_base(self):
        return self.nucleotide

    def set_base(self, nucleotide):
        if nucleotide not in self.base:
            raise ValueError(f"Invalid base")

        self.nucleotide = nucleotide

    base_check = property(fget=get_base, fset=set_base)


