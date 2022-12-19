lines = []
with open('./input.txt') as file:
    lines = [line.rstrip() for line in file]

# Find the pairs where one range is fully contained in the each other
# &


contained_pairs = 0
overlap_pairs = 0
for line in lines:
    pair = line.split(',')
    fopstr = pair[0].split('-')
    sopstr = pair[1].split('-')
    fop = [int(x) for x in pair[0].split('-')]
    sop = [int(x) for x in pair[1].split('-')]
    # Two cases: First fully contained in second, or second fully contained in first
    # Check whether the first and last element of the range are within the first and last element of the other
    if (fop[0] >= sop[0] and fop[1] <= sop[1]) or (sop[0] >= fop[0] and sop[1] <= fop[1]):
        contained_pairs = contained_pairs + 1
    # The first element of either range being inside the other range is enough to prove this when looking at both
    # Otherwise, the range is either completely bigger OR completely smaller OR partially smaller
    # When partially smaller (so last element(s) do overlap), it means the first element of the other range is inside the other range
    # Check whether the first element of a range is bigger than the first and smaller than the last of the other
    if (fop[0] >= sop[0] and fop[0] <= sop[1]) or (sop[0] >= fop[0] and sop[0] <= fop[1]):
        overlap_pairs = overlap_pairs + 1

print(contained_pairs)
print(overlap_pairs)


