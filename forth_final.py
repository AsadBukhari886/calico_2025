def get_moves(from_pos, to_pos, rows, cols):
    row_dist = abs(from_pos[0] - to_pos[0])
    wrap_row = rows - row_dist  
    row_moves = min(row_dist, wrap_row)
    
    col_dist = abs(from_pos[1] - to_pos[1])
    wrap_col = cols - col_dist  
    col_moves = min(col_dist, wrap_col)
    
    
    return row_moves + col_moves

def solve():
   
    n, m = map(int, input().split())
    
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
   
    button_pos = {}  
    for r in range(n):
        for c in range(m):
            val = grid[r][c]
            button_pos[val] = (r, c)
    
    cursor = (0, 0)
    total_moves = 0  
    
    for num in range(1, n*m + 1):  
        target = button_pos[num]  
        
        moves = get_moves(cursor, target, n, m)
        total_moves += moves 
        
        cursor = target
    
    return total_moves

def main():
    try:
        t = int(input().strip())
        
        answers = []
        for case in range(1, t+1):
            answer = solve()
            answers.append(answer)
        
        for ans in answers:
            print(ans)
    except Exception as e:
        print(f"Error: {e}") 

if __name__ == "__main__":
    main()