import numpy
import numpy as np

def main():
    cache_size = pow(2,int(input("Enter the cache Size: ")))     #IN THE POWER OF 2^n
    cache_lines = pow(2,int(input("Enter the Cache lines: ")))   #IN THE POWER OF 2^n
    blocks = pow(2,int(input("Enter the Block Size: ")))         #IN THE POWER OF 2^n
    k = pow(2,int(input("enter no. of sets(n):")))               #IN THE POWER OF 2^n
    sets = int(cache_lines/k)

    # I HAVE USED  IMPLEMENTATION USING LIST FOR k-WAY SET ASSOCIATIVE CACHE MAPPING

    cache = [[None for i in range(sets)] for j in range(k)]

    #print(cache)
    var = True
    while var:
        user_input = int((input("choose operation 0.Exit 1.Loading 2.Searching \n")))
        if user_input == 1:
            inp=int(input("Input word address: "))
            t=inp//blocks
            block_name= "B" + str(t)
            k_mod_n = t % k
            if block_name in cache[k_mod_n]:
                print(f'{block_name} already exist in cache')
            else:
                print("Address not found")
                if len(cache[k_mod_n]) < sets:
                    cache[k_mod_n].append(block_name)
                else:
                    cache[k_mod_n].pop(0)
                    cache[k_mod_n].append((block_name))

                print(f'{inp} in {block_name} loaded successfully to set {k_mod_n}  ')

        elif user_input == 2:
            inp = int(input("enter address to search: "))
            t = inp // blocks
            block_name = "B" + str(t)
            k_mod_n = t % k
            if block_name in cache[k_mod_n]:
                print("cache hit")
            else:
                print("cache miss")
        elif user_input == 0:
            var = False

    arr = numpy.array(cache)
    result = arr.flatten()
    #print(result)
    finalcache = result.tolist()

    print("CACHELINE|BLOCK_PRESENT")
    for i in range(len(finalcache)):
        print(i, end=" ")
        print(finalcache[i])


main()