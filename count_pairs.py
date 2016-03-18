"""
File: <count_pairs.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Given a sequence of DNA and a base, count the number of bases contained in the sequence of DNA.>
"""
def count_v2(dna,base):
    i = 0
    for AT in dna:
        if AT == base:
            i += 1
        return dna.count(base)

dna = 'CACTTGATATCATCGG'
base= "AT"
n = count_v2(dna,base)

print 'There are %s pairs.' % (n)
