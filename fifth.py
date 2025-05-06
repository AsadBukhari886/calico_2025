def solve_case(s):
    positions = []
    for idx, ch in enumerate(s):
        if ch == 'u':
            positions.append(idx)
    prefix_w = [0] * (len(s) + 1)
    for i in range(len(s)):
        prefix_w[i+1] = prefix_w[i] + (1 if s[i] == 'w' else 0)
    ans = 0
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            if prefix_w[positions[j]] - prefix_w[positions[i]] > 0:
                ans += 1
    return ans

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(solve_case(s))

if __name__ == "__main__":
    main()
