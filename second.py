def solve(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    
    width = max_x - min_x
    height = max_y - min_y
    
    area = width * height
    
    return area

def main():
    T = int(input().strip())  
    
    for _ in range(T):
        N = int(input().strip())  
        points = []
        
        for i in range(N):
            line = input().strip()
            x, y = map(float, line.split())
            points.append((x, y))
        
        area = solve(points)
        print(area)  
if __name__ == "__main__":
    main()