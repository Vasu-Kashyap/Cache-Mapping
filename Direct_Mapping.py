
def main():
    cache_size = pow(2, int(input("Enter the cache Size "))) #IN THE POWER OF 2^n
    cache_lines = pow(2, int(input("Enter the Cache lines "))) #IN THE POWER OF 2^n
    blocks = pow(2, int(input("Enter the Block Size "))) #IN THE POWER OF 2^n

    #I HAVE USED DICTIONARY FOR REPRESENTING CACHE IN DIRECT MAPPING
    cache={}
    for i in range(cache_lines):
        cache[i]=None

    var = True
    while var:
        user_input = int((input("choose operation 0.Exit 1.Loading 2.Searching \n")))
        if user_input == 1:
            inp=int(input("Input word address: "))
            t=inp//blocks
            block_name= "B" + str(t)
            if block_name in cache.values():
                print(f'{block_name} already exist in cache')
            else:
                print("address not found")
                k_mod_n=t%cache_lines
                cache[k_mod_n]=block_name
                print(f'word {inp} in block {block_name} loaded successfully to cache line {k_mod_n}')
        elif user_input == 2:
            inp = int(input("enter address to search: "))
            t = inp // blocks
            block_name = "B" + str(t)
            if block_name in cache.values():
                print("cache hit")
            else:
                print("cache miss")
        elif user_input == 0:
            var = False
    print("CACHELINE|BLOCK_PRESENT")
    for i in cache:
        print (i, cache[i])
    #print(cache)


main()