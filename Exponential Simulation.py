import matplotlib.pyplot as plt

def linear_growth(k, x):
    blocks_stacked = [i * k for i in range(1, x + 1)]
    return blocks_stacked

def exponential_growth(x, base):
    blocks_stacked = [base ** i for i in range(x)]
    return blocks_stacked

def main():
    while True:
        print()
        
        # Linear Growth
        print("Linear Growth:")  # Add this line
        stages = [
            "stage 1: block 1",
            "stage 2: block 2",
            "stage 3: block 3",
            "stage 4: block 4",
            "stage 5: block 5",
            "stage 6: block 6",
            "stage 7: block 7",
            "stage 8: block 8",
            "stage 9: block 9",
            "stage 10: block 10"
        ]

        for stage in stages:
            print(stage)
        
        k = int(input("\nChoose a one-digit number 'k': "))
        if not (0 <= k <= 9):
            print("\nValue of k should be a single-digit number between 0 and 9 only.")
            continue  # Restart the loop if input is invalid
            
        # Exponential Growth
        print("\nExponential Growth:")
        for step in range(1, 11):
            print(f"Step {step}: {step * k} blocks")
        
        while True:  # Nested loop to handle invalid choice input
            print("\nChoosing Growth Type and Graphs (Grades 3-5):")
            print("Choose between three growth options: 2x, x2, or 3x.")
            choice = input("Enter '2x', 'x2', or '3x': ")
            if choice in ['2x', 'x2', '3x']:
                break  # Exit the nested loop if input is valid
            else:
                print("Invalid choice. Please enter '2x', 'x2', or '3x'.")
        
        if choice == '2x':
            base = 2
        elif choice == 'x2':
            base = 10
        elif choice == '3x':
            base = 3
    
        x_values = range(1, 11)
        blocks_stacked_exponential = exponential_growth(10, base)
        
        print(f"\nExponential Growth ({choice}):")
        for step, blocks in zip(x_values, blocks_stacked_exponential):
            print(f"Step {step}: {blocks} blocks")
    
        # Plot the data for both linear and exponential growth.
        blocks_stacked_linear = linear_growth(k, 10)
        
        plt.plot(x_values, blocks_stacked_linear, label=f"Linear Growth (k = {k})")
        plt.plot(x_values, blocks_stacked_exponential, label=f"Exponential Growth ({choice})")
        plt.xlabel('Step')
        plt.ylabel('Number of Blocks')
        plt.legend()
        plt.grid(True)
        plt.title('Linear vs Exponential Growth')
        plt.show()
        
        #if the user wants to run again code again
        repeat = input("Do you want to run again? (y/n): ")
        if repeat.lower() != 'y':
            break  # Exit the loop if the user doesn't want to repeat
        
if __name__ == "__main__":
    main()
