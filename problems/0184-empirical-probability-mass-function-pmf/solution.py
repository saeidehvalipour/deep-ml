from collections import Counter
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """

    if not samples:
        return []
    
    counts = Counter(samples)
    total = len(samples)
    # prob = {k: v / total for k,v in counts.items()}

    return [(value, counts[value] / total) for value in sorted(counts)]
    # n = len(pmf_dict)
    # total = sum(pmf_dict.values())
    # for n in samples:
    #     pmf_dict[n] = pmf_dict.get(n ,0) +1
    # print( dict(sorted(prob.items(), key=lambda x:x[1])) )
    # dict(sorted(d.items(), key=lambda x: x[1]))   

#     total = sum(d.values())
# normalized_d = {k: v / total for k, v in d.items()}
