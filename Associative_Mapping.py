
def main():
    cache_size = pow(2,int(input("Enter the cache Size "))) #IN THE POWER OF 2^n
    cache_lines = pow(2,int(input("Enter the Cache lines "))) #IN THE POWER OF 2^n
    blocks = pow(2,int(input("Enter the Block Size ")))   #IN THE POWER OF 2^n

    # I HAVE USED QUEUE IMPLEMENTATION USING LIST FOR FULLY ASSOCIATIVE CACHE MAPPING
    cachequeue = []

    #print(cachequeue)
    var = True
    while var:
        user_input = int((input("choose operation 0.Exit 1.Loading 2.Searching \n")))
        if user_input == 1:
            inp=int(input("Input word address: "))
            t=inp//blocks
            block_name= "B" + str(t)
            if block_name in cachequeue:
                print(f'{block_name} already exist in cache')
            else:
                print("address not found")
                if len(cachequeue) < cache_lines:
                    cachequeue.append(block_name)
                else:
                    cachequeue.pop(0)
                    cachequeue.append((block_name))

                print(f'word {inp} in block {block_name} loaded successfully to cache')

        elif user_input == 2:
            inp = int(input("enter address to search: "))
            t = inp // blocks
            block_name = "B" + str(t)
            if block_name in cachequeue:
                print("cache hit")
            else:
                print("cache miss")
        elif user_input == 0:
            var = False
    #print(cachequeue)
    for i in range(len(cachequeue), cache_lines):
        cachequeue.append(None)
    print("CACHELINE|BLOCK_PRESENT")
    for i in range(len(cachequeue)):
        print(i, end=" ")
        print(cachequeue[i])


main()