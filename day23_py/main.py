
f = open('input.txt', 'r')

lan_array = []

for line in f:
    computers = line.strip().split('-')
    lan_array.append(computers)

parties_with_t = 0
search_lan_parties = True

while search_lan_parties:

    if len(lan_array) == 1:
        break

    lan1, lan2 = lan_array[0]

    for i, search in enumerate(lan_array[1:]):
        if lan1 in search and lan2 not in search:
            new_search = search.copy()
            new_search.remove(lan1)
            new_search = new_search + [lan2]  
            print(new_search)      
            
            for k, pp in lan_array:
                if pp == new_search or pp == new_search[::-1]:
                    indx = k
                    for comp in new_search + [lan1]:
                        if comp[0] == 't':
                            parties_with_t += 1
                    lan_array.pop(indx)
                    lan_array.remove([lan1] + [lan2])
                    lan_array.remove(search)
                    break

        elif lan2 in search and lan1 not in search:
            new_search = search.copy()
            new_search.remove(lan2)
            new_search = new_search + [lan1]

            for k, pp in lan_array:
                if pp == new_search or pp == new_search[::-1]:
                    indx = k
                    for comp in new_search + [lan2]:
                        if comp[0] == 't':
                            parties_with_t += 1
                    lan_array.pop(indx)
                    lan_array.remove([lan1] + [lan2])
                    lan_array.remove(search)
                    break

        if i == len(lan_array[1:]) - 1:
            lan_array.remove([lan1] + [lan2])

    print(parties_with_t)

# For the first record, check if another record is found in the rest,
# if it is, check if there is a third matching, if not check the second one,
# Else remove