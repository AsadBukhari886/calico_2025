def solve():
    n = int(input().strip())

    if n == 1:
        return "uwu"
    elif n == 2:
        return "uwuu"  
    
    import math
    k = int(math.sqrt(n))

    while k > 0 and n % k != 0:
        k -= 1
    
    if k == 0:
        k = 1
    
    m = n // k
    
    assert k * m == n, f"error: {k}*{m}!={n}"
    
    return "u" * k + "w" + "u" * m

def main():
    try:
        t = int(input().strip())
        
        for _ in range(t):
            result = solve()
            print(result)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()