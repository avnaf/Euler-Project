def get_prime(lim = 10**6):
    yield 2
    flags = [True, True] + [False] * (lim - 2)
    for i in range(3,lim,2):
        if flags[i]:
            continue
        yield i
        if i <= lim // 2:
            for j in range(i*i, lim, i << 1):
                flags[j] = True
                
prime_ls = [p for p in get_prime()]              
                
def is_prime(x):
    global prime_ls
    return x in prime_ls

def truncatable(x):    
    def _truncatable(x, direction = 'right'):
        if not is_prime(x):
            return False
        
        if x < 10:
            return True
        
        if direction == 'right':
            return _truncatable(int(str(x)[:-1]), direction)
        else:
            return _truncatable(int(str(x)[1: ]), direction)
    
    return _truncatable(x) and _truncatable(x, 'left')

res = 0
counter = 1
for p in prime_ls[4:]:
    if truncatable(p):
        print '{} : {}'.format(counter,p)
        counter += 1
        res += p
        
        