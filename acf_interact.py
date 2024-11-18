import os

def menu_application():
    language = "en"  # Default language

    while True:
        terminal_width = os.get_terminal_size().columns
        header_border = "=" * terminal_width
        title_en = "ADAPTIVE CORRECTION FRAMEWORK (ACF)"
        title_hi = "एडाप्टिव करेक्शन फ्रेमवर्क (ACF)"
        centered_title = title_en.center(terminal_width) if language == "en" else title_hi.center(terminal_width)

        print(header_border)
        print(centered_title)
        print(header_border)
        if language == "en":
            print("\nChoose an option from the menu below:")
            print("-" * 50)
            print("1. Set Language (current: {})".format(language.upper()))
            print("2. Enter a problem")
            print("3. End Application")
            print("-" * 50)
        else:  # Hindi
            print("\nनीचे दिए गए मेनू से एक विकल्प चुनें:")
            print("-" * 50)
            print("1. भाषा बदलें (वर्तमान: {})".format(language.upper()))
            print("2. एक समस्या दर्ज करें")
            print("3. एप्लिकेशन बंद करें")
            print("-" * 50)

        try:
            choice = int(input("Enter your choice: " if language == "en" else "अपना विकल्प दर्ज करें: "))
            print("-" * 50)

            if choice == 1:
                if language == "en":
                    language_input = input("Enter language ('en' for English, 'hi' for Hindi): ").strip().lower()
                else:
                    language_input = input("भाषा दर्ज करें ('en' अंग्रेज़ी के लिए, 'hi' हिंदी के लिए): ").strip().lower()

                if language_input in ["en", "hi"]:
                    language = language_input
                    print(f"Language set to: {language.upper()}" if language == "en" else f"भाषा बदल दी गई है: {language.upper()}")
                else:
                    if language == "en":
                        print("Invalid input. Please choose 'en' for English or 'hi' for Hindi.")
                        print(f"Language remains set to: {language.upper()}")
                    else:
                        print("अमान्य इनपुट। कृपया 'en' अंग्रेज़ी के लिए या 'hi' हिंदी के लिए चुनें।")
                        print(f"भाषा यथावत बनी रहेगी: {language.upper()}")

            elif choice == 2:
                problem = input("Enter the problem statement: " if language == "en" else "समस्या कथन दर्ज करें: ")

                print("\nProcessing problem...\n" if language == "en" else "\nसमस्या संसाधित की जा रही है...\n")
                print("Feature not available in this version. Please try again later." if language == "en" else "यह सुविधा इस संस्करण में उपलब्ध नहीं है। कृपया बाद में प्रयास करें।")
                result = ""

            elif choice == 3:
                print("Thank you for using the application!".center(terminal_width) if language == "en" else "एप्लिकेशन का उपयोग करने के लिए धन्यवाद!".center(terminal_width))
                print(header_border)
                break
            else:
                if language == "en":
                    print("Invalid choice! Please select a valid option.")
                else:
                    print("अमान्य विकल्प! कृपया एक मान्य विकल्प चुनें।")
                print("-" * 50)
        except ValueError:
            if language == "en":
                print("Invalid input! Please enter a numeric choice.")
            else:
                print("अमान्य इनपुट! कृपया एक संख्यात्मक विकल्प दर्ज करें।")
            print("-" * 50)

menu_application()