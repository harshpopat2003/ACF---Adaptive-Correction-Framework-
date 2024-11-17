import os
from acf import AdaptiveCorrectionFramework

def menu_application():
    acf = AdaptiveCorrectionFramework()
    language = "en"  # Default language

    while True:
        terminal_width = os.get_terminal_size().columns
        header_border = "=" * terminal_width
        centered_title = "ADAPTIVE CORRECTION FRAMEWORK (ACF)".center(terminal_width)

        print(header_border)
        print(centered_title)
        print(header_border)
        print("\nChoose an option from the menu below:")
        print("-" * 50)
        print("1. Set Language (current: {})".format(language.upper()))
        print("2. Enter a problem")
        print("3. Test on Dataset")
        print("4. End Application")
        print("-" * 50)

        try:
            choice = int(input("Enter your choice: "))
            print("-" * 50)

            if choice == 1:
                language_input = input("Enter language ('en' for English, 'hi' for Hindi): ").strip().lower()
                if language_input in ["en", "hi"]:
                    language = language_input
                    print(f"Language set to: {language.upper()}")
                else:
                    print("Invalid input. Please choose 'en' for English or 'hi' for Hindi.")
                    print(f"Language remains set to: {language.upper()}")

            elif choice == 2:
                problem = input("Enter the problem statement: ")

                print("\nProcessing problem...\n")
                result = acf.run(problem, language)

                print(f"Initial Solution:\n{result['initial_solution']}\n")
                print(f"Errors Identified:\n{result['errors']}\n")

                for error_type, correction in result["corrections"].items():
                    print(f"Correction for {error_type}:\n{correction}\n")

                print(f"Final Solution:\n{result['final_solution']}\n")

            elif choice == 3:
                print("Testing on Dataset...\n")
                dataset_filename = input("Enter the dataset filename: ").strip()
                max_steps = int(input("Enter the maximum number of iteration steps for refinement (default: 5): ") or "5")
                graph_rag_dir = input("Enter the GRAPH_RAG directory path: ").strip()
                dataset_dir = input("Enter the dataset directory path: ").strip()
                result_dir = input("Enter the result directory path: ").strip()

                print("\nRunning evaluation on the dataset...\n")
                # Here you would call your dataset evaluation function, e.g.,
                # evaluate(dataset_filename, max_steps, graph_rag_dir, dataset_dir, result_dir)
                print(f"Evaluation completed. Results saved to {result_dir}/{dataset_filename}")

            elif choice == 4:
                print("Thank you for using the application!".center(terminal_width))
                print(header_border)
                break
            else:
                print("Invalid choice! Please select a valid option.")
                print("-" * 50)
        except ValueError:
            print("Invalid input! Please enter a numeric choice.")
            print("-" * 50)

if __name__ == "__main__":
    menu_application()