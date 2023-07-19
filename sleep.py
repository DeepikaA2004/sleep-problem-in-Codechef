def is_sleep_deprived(hours_slept):
    return hours_slept < 7

# Main function to read inputs and call the helper function for each test case
def main():
    # Read the number of test cases
    T = int(input().strip())

    # Process each test case
    for _ in range(T):
        hours_slept = int(input().strip())
        if is_sleep_deprived(hours_slept):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
