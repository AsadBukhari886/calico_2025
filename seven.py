def main():
    import sys
    print("Paste your input (press Ctrl+Z then Enter when done):")
    
    # Read all input, ignoring empty lines and cleaning whitespace
    data = []
    while True:
        try:
            line = input().strip()
            if line:
                data.extend(line.split())
        except EOFError:
            break
    
    ptr = 0
    try:
        num_test_cases = int(data[ptr])
        ptr += 1
        
        results = []
        
        for _ in range(num_test_cases):
            if ptr >= len(data):
                raise ValueError("Unexpected end of input")
                
            num_blocks = int(data[ptr])
            ptr += 1
            
            blocks = []
            for _ in range(num_blocks):
                if ptr + 3 >= len(data):
                    raise ValueError("Incomplete block coordinates")
                
                x0 = int(data[ptr])
                y0 = int(data[ptr+1])
                x1 = int(data[ptr+2])
                y1 = int(data[ptr+3])
                ptr += 4
                blocks.append((x0, y0, x1, y1))
            
            # Build support map (block index -> supporting block index)
            support_map = [-1] * num_blocks
            for i in range(num_blocks):
                x0_i, y0_i, x1_i, y1_i = blocks[i]
                if y0_i == 0:
                    continue  # On floor
                
                supported = False
                for j in range(num_blocks):
                    x0_j, y0_j, x1_j, y1_j = blocks[j]
                    if (y0_i == y1_j) and (x0_i >= x0_j) and (x1_i <= x1_j):
                        support_map[i] = j
                        supported = True
                        break
                
                if not supported and y0_i != 0:
                    results.append("Unstable")
                    break
            else:
                # Check stability from top to bottom
                is_stable = True
                substructure_mass = [0.0] * num_blocks
                substructure_com_x = [0.0] * num_blocks
                
                for i in reversed(range(num_blocks)):
                    x0, y0, x1, y1 = blocks[i]
                    mass = (x1 - x0) * (y1 - y0)
                    com_x = (x0 + x1) / 2
                    
                    total_mass = mass
                    total_com_x = com_x * mass
                    
                    # Add all blocks resting on this one
                    for k in range(num_blocks):
                        if support_map[k] == i:
                            total_mass += substructure_mass[k]
                            total_com_x += substructure_com_x[k] * substructure_mass[k]
                    
                    substructure_mass[i] = total_mass
                    if total_mass > 0:
                        substructure_com_x[i] = total_com_x / total_mass
                    
                    # Stability check for non-floor blocks
                    if support_map[i] != -1:
                        s_block = support_map[i]
                        s_x0, _, s_x1, _ = blocks[s_block]
                        current_com = substructure_com_x[i]
                        
                        # COM must be strictly within supporting block's edges
                        if not (s_x0 < current_com < s_x1):
                            is_stable = False
                            break
                
                results.append("Stable" if is_stable else "Unstable")
        
        # Print all results
        for result in results:
            print(result)
    
    except (ValueError, IndexError) as e:
        print(f"Error: {str(e)} - check your input format")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()