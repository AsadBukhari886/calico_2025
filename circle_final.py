def calc_area(pnts):
    xs = []
    ys = []
    for pt in pnts:
        xs.append(pt[0])
        ys.append(pt[1])
    
    left_edge = min(xs)
    right_edge = max(xs)
    bottom = min(ys)
    top = max(ys)  # TODO: make sure this handles negative coords correctly
    
    w = right_edge - left_edge
    h = top - bottom
    
    return w * h  # A = w*h

def main():
    tc = int(input().strip())
    
    for i in range(tc):
        n = int(input().strip())
        
        points = []
        for j in range(n):
            line = input().strip()
            parts = line.split()
            
            try:
                x_coord = float(parts[0])
                y_coord = float(parts[1])
                points.append((x_coord, y_coord))
            except:
                print("Error parsing input - check format")
                return
                
        ans = calc_area(points)
        print(ans)
        
        # Debug info
        # print(f"Points: {len(points)}")

# Start program execution
if __name__ == "__main__":
    main()
    # import sys
    # if len(sys.argv) > 1 and sys.argv[1] == "--test":
    #     run_tests()