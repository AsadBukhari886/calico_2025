def min_distance(pos1, pos2, n, m):
    """Calculate minimum distance between two positions considering wrap-around."""
    row_dist = min(
        abs(pos1[0] - pos2[0]),  
        (n - abs(pos1[0] - pos2[0])) % n  
    )
    
    col_dist = min(
        abs(pos1[1] - pos2[1]),  
        (m - abs(pos1[1] - pos2[1])) % m  
    )
    
    return row_dist + col_dist

def solve_test_case():
    n, m = map(int, input().split())
    
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    positions = {}
    for i in range(n):
        for j in range(m):
            positions[grid[i][j]] = (i, j)
    
    total_actions = 0
    current_pos = (0, 0)  
    
    for num in range(1, n*m + 1):
        target_pos = positions[num]
        
        moves = min_distance(current_pos, target_pos, n, m)
        total_actions += moves
        
        current_pos = target_pos
    
    return total_actions

def main():
    t = int(input().strip())
    
    results = []
    for _ in range(t):
        result = solve_test_case()
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()