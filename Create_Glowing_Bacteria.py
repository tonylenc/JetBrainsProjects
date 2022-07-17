def get_complementary_strand(strand):
    translation = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complementary_strand = ''.join([translation[i] for i in strand])
    return complementary_strand


def cut_plasmid(strand, restriction_site, position):
    index = strand.find(restriction_site)
    if index > -1:
        return [strand[:index + position], strand[position + index:]]
    else:
        raise ValueError


def cut_gfp(gfp, left_restriction_site, right_restriction_site, cut):
    return gfp[gfp.index(left_restriction_site) + cut:gfp.rindex(right_restriction_site) + cut]


def glue(strands, gfp):
    return gfp.join(strands)


with open(input()) as dna:
    plasmid = dna.readline().rstrip('\n')
    plasmid_rest_site = dna.readline().rstrip('\n')
    GFP = dna.readline().rstrip('\n')
    gfp_rest_site_L, gfp_rest_site_R = dna.readline().split()

GFP_for_insertion = cut_gfp(GFP, gfp_rest_site_L, gfp_rest_site_R, 1)
strand_for_insertion = cut_plasmid(plasmid, plasmid_rest_site, 1)

print(glue(strand_for_insertion, GFP_for_insertion))
print(get_complementary_strand(glue(strand_for_insertion, GFP_for_insertion)))
