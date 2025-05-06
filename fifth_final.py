def count_ways_to_form_uwu(my_string):
    u_positions = []
    for index, character in enumerate(my_string):
        if character == 'u':
            u_positions.append(index)

    w_prefix_sum = [0] * (len(my_string) + 1)
    for i in range(len(my_string)):
        w_prefix_sum[i+1] = w_prefix_sum[i]
        if my_string[i] == 'w':
            w_prefix_sum[i+1] += 1

    #print(f"String: {my_string}")
    #print(f"u positions: {u_positions}")
    #print(f"prefix sum for w's: {w_prefix_sum}")

    total_pairs = 0

    for first_u in range(len(u_positions)):
        for second_u in range(first_u+1, len(u_positions)):
            w_in_between = w_prefix_sum[u_positions[second_u]] - w_prefix_sum[u_positions[first_u]]
            if w_in_between > 0:
                total_pairs += 1
                #print(f"Pair found: u at {u_positions[first_u]} and u at {u_positions[second_u]} with {w_in_between} w's between")

    #print(f"Total pairs for this string: {total_pairs}")
    return total_pairs


def main():
    #num_test_cases = int(input("Enter number of test cases: "))
    num_test_cases = int(input())
    all_answers = []

    for case in range(num_test_cases):
        #test_string = input(f"Enter string for case {case+1}: ").strip()
        test_string = input().strip()
        answer = count_ways_to_form_uwu(test_string)
        all_answers.append(answer)

    #print("\nFinal Answers:")
    for ans in all_answers:
        print(ans)


if __name__ == "__main__":
    #print("Starting program...")
    main()
