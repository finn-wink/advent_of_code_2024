
def text_to_num(letters):
    num_pattern = []
    for char in letters:
        if char == 'r':
            num_pattern.append(0)
        if char == 'w':
            num_pattern.append(1)
        if char == 'b':
            num_pattern.append(2)
        if char == 'g':
            num_pattern.append(3)
        if char == 'u':
            num_pattern.append(4)

    return num_pattern   

def find_pattern(desired, patterns, memorize=None):

    if memorize is None:
        memorize = {}

    if desired == '':
        return True

    if desired in memorize:
        return memorize[desired]
    
    for pat in patterns:
        if desired.startswith(pat):
            matched_bits.append(pat)
            if find_pattern(desired[len(pat):], patterns, memorize):
                memorize[desired] = True
                return True

    memorize[desired] = False
    return False

def deep_search(des, bits, patterns, unique_matches=0):

    bits = list(set(bits)) # Avoid duplicates

    for bit in bits:
        print(bit)
        if bit in patterns:
            patterns.remove(bit)
        else:
            continue
        if find_pattern(des, patterns):
            unique_matches += 1
            new_bits = [item for item in bits if item != bit]
            unique_matches = deep_search(des, new_bits, patterns, unique_matches)

    return unique_matches

f = open('input.txt', 'r')

PATTERNS = []
desired = []

for i, line in enumerate(f):    
    if i == 0:
        words = line.strip().split(',')
        for w in words:
            # print(num)
            PATTERNS.append(w.strip())

    elif line != '\n':
        desired.append(line.strip())

# PATTERNS = sorted(PATTERNS, key=len, reverse=True)

matched_total = 0

for d in desired:
    
    matched_bits = []

    matched = find_pattern(d, PATTERNS)
      
    if matched:
        matched_total += 1
        edit_pattern = PATTERNS
        u_match = deep_search(d, matched_bits, edit_pattern)
        matched_total += u_match

print(matched_total)