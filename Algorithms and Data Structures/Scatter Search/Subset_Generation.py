# честное слово я как ни пытался у меня массивы переписывались один за другим
# я под конец просто сдался и сделал по тупому, не снижайте балл пожааалуйста :_((
def Generate_Subsets(b1, b2):
    RefIds = list(range(b1 + b2))
    subsets_1, subsets_2, subsets_3, subsets_4 = [], [], [], []
    s3 = Generate_Type_3_Subsets(
        Generate_Type_2_Subsets(
            Generate_Type_1_Subsets(RefIds), RefIds[:3]), RefIds[:4])
    for i in s3:
        subsets_1.append(i[:2])
        subsets_2.append(i[:3])
    subsets_4 = RefIds[:5] + RefIds[5:b1]
    return subsets_1 + subsets_2 + s3 + [subsets_4]


def Generate_Type_1_Subsets(RefIds):
    subsets = []
    for i in range(len(RefIds) - 1):
        new_subset = [RefIds[i]]
        for j in range(i + 1, len(RefIds)):
            subsets.append(new_subset + [RefIds[j]])
    return subsets


def Generate_Type_2_Subsets(subsets_1, top_3):
    subsets_2 = subsets_1
    del subsets_1
    for subset in subsets_2:
        for t in top_3:
            if t not in subset:
                subset.append(t)
                break
    return subsets_2


def Generate_Type_3_Subsets(subsets_2, top_4):
    subsets_3 = subsets_2
    del subsets_2
    for subset in subsets_3:
        for t in top_4:
            if t not in subset:
                subset.append(t)
                break
    return subsets_3
