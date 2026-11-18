
# ==========================================
#       ACT MAJOR
# FUNDAMENTALS OF PROGRAMMING
# ==========================================

while True:

    print("\n====================================")
    print("             ACT MAJOR")
    print("    FUNDAMENTALS OF PROGRAMMING")
    print("====================================")
    print("[1] CONDITIONAL STATEMENTS IN PYTHON")
    print("[2] LOGICAL OPERATORS")
    print("[3] INTRODUCTION TO ITERATION AND LOOPS")
    print("[4] INTRODUCTION TO PROGRAMMING")
    print("[5] BASIC SYNTAX")
    print("[6] ARITHMETIC OPERATORS")
    print("[0] EXIT")
    print("====================================")

    try:
        topics = int(input("Choose your lesson: "))
    except ValueError:
        print("INVALID INPUT! ENTER A NUMBER.")
        continue

    # ==========================================
    # TOPIC 1: CONDITIONAL STATEMENTS
    # ==========================================

    if topics == 1:

        while True:
            print("\n===== CONDITIONAL STATEMENTS =====")
            print("[1] Introduction to Conditional Statements")
            print("[2] Relational Operators")
            print("[3] The IF Statement")
            print("[4] The IF-ELSE Statement")
            print("[5] The IF-ELIF-ELSE Statement")
            print("[0] Back to Main Menu")

            try:
                answer = int(input("Choose Topic: "))
            except ValueError:
                print("INVALID INPUT!")
                continue

            if answer == 0:
                break

            elif answer == 1:
                print("\n===== INTRODUCTION TO CONDITIONAL STATEMENTS =====")
                print("Conditional statements allow programs to make decisions.")
                print("EXAMPLE: Checking Age")

                age = int(input("Enter your age: "))

                if age >= 18:
                    print("You are an adult.")
                elif age >= 0:
                    print("BATA KAPA BOI!")
                else:
                    print("INVALID AGE!")

            elif answer == 2:
                print("\n===== RELATIONAL OPERATORS =====")
                print("Used to compare two values.")
                print("== Equal")
                print("!= Not Equal")
                print("> Greater Than")
                print("< Less Than")
                print(">= Greater Than or Equal")
                print("<= Less Than or Equal")

                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))

                print("Equal:", a == b)
                print("Not Equal:", a != b)
                print("Greater Than:", a > b)
                print("Less Than:", a < b)
                print("Greater Than or Equal:", a >= b)
                print("Less Than or Equal:", a <= b)

            elif answer == 3:
                print("\n===== THE IF STATEMENT =====")
                print("Executes code only when the condition is TRUE.")

                grade = int(input("Enter your grade: "))

                if grade >= 75:
                    print("PASADO KA!")

                print("Program finished.")

            elif answer == 4:
                print("\n===== THE IF-ELSE STATEMENT =====")
                print("Provides an alternative when the condition is FALSE.")

                grade = int(input("Enter your grade: "))

                if grade >= 75:
                    print("PASSED!")
                else:
                    print("BAWI NEXT YEAR!")

            elif answer == 5:
                print("\n===== THE IF-ELIF-ELSE STATEMENT =====")
                print("Used to check multiple conditions.")

                age = int(input("Enter your age: "))

                if age < 0:
                    print("INVALID AGE!")
                elif age <= 12:
                    print("CHILD")
                elif age <= 19:
                    print("TEENAGER")
                elif age <= 59:
                    print("ADULT")
                else:
                    print("SENIOR CITIZEN")

            else:
                print("INVALID LESSON!")

    # ==========================================
    # TOPIC 2: LOGICAL OPERATORS
    # ==========================================

    elif topics == 2:

        while True:
            print("\n===== LOGICAL OPERATORS =====")
            print("[1] AND Operator")
            print("[2] OR Operator")
            print("[3] NOT Operator")
            print("[0] Back to Main Menu")

            try:
                answer = int(input("Choose Topic: "))
            except ValueError:
                print("INVALID INPUT!")
                continue

            if answer == 0:
                break

            elif answer == 1:
                print("\n===== AND OPERATOR =====")
                print("ALL conditions must be TRUE.")

                age = int(input("Enter your age: "))

                if age >= 18 and age <= 60:
                    print("ALLOWED")
                else:
                    print("NOT ALLOWED")

            elif answer == 2:
                print("\n===== OR OPERATOR =====")
                print("At least ONE condition must be TRUE.")

                day = input("Enter the day: ").strip().lower()

                if day == "saturday" or day == "sunday":
                    print("IT'S SHOTERDAY!")
                else:
                    print("IT'S A REGULAR SCHOOL DAY!")

            elif answer == 3:
                print("\n===== NOT OPERATOR =====")
                print("NOT reverses a Boolean result.")

                raining = input("Is it raining? (yes/no): ").strip().lower()

                if not (raining == "yes"):
                    print("YOU CAN GO OUTSIDE!")
                else:
                    print("BRING AN UMBRELLA!")

            else:
                print("INVALID LESSON!")

    # ==========================================
    # TOPIC 3: ITERATION AND LOOPS
    # ==========================================

    elif topics == 3:

        while True:
            print("\n===== ITERATION AND LOOPS =====")
            print("[1] Types of Loops")
            print("[2] Python FOR Loop")
            print("[3] Print Numbers 1 to 5")
            print("[4] Counting Downward 5 to 1")
            print("[5] Repeating a Program with WHILE TRUE")
            print("[0] Back to Main Menu")

            try:
                answer = int(input("Choose Topic: "))
            except ValueError:
                print("INVALID INPUT!")
                continue

            if answer == 0:
                break

            elif answer == 1:
                print("\n===== TYPES OF LOOPS =====")
                print("[1] FOR LOOP")
                print("[2] WHILE LOOP")

                types = int(input("Choose type of loop: "))

                if types == 1:
                    print("\n===== FOR LOOP =====")

                    for number in range(3):
                        print("I LOVE CCST!")

                elif types == 2:
                    print("\n===== WHILE LOOP =====")

                    count = 1

                    while count <= 3:
                        print("HELLO WORLD!")
                        count += 1

                else:
                    print("UNAVAILABLE LOOP!")

            elif answer == 2:
                print("\n===== PYTHON FOR LOOP =====")
                print("Repeats a block of code.")

                for number in range(4):
                    print("STUDY HARD!")

            elif answer == 3:
                print("\n===== PRINT NUMBERS 1 TO 5 =====")

                for number in range(1, 6):
                    print(number)

            elif answer == 4:
                print("\n===== COUNTING DOWNWARD =====")

                for number in range(5, 0, -1):
                    print(number)

            elif answer == 5:
                print("\n===== WHILE TRUE =====")

                while True:
                    name = input("Enter your name (X to exit): ")

                    if name.upper() == "X":
                        print("PROGRAM STOPPED!")
                        break

                    print("HELLO", name)

            else:
                print("INVALID LESSON!")

    # ==========================================
    # TOPIC 4: INTRODUCTION TO PROGRAMMING
    # ==========================================

    elif topics == 4:

        while True:
            print("\n===== INTRODUCTION TO PROGRAMMING =====")
            print("[1] Programming Language")
            print("[2] Python Programming")
            print("[3] About Python")
            print("[0] Back to Main Menu")

            try:
                answer = int(input("Choose Lesson: "))
            except ValueError:
                print("INVALID INPUT!")
                continue

            if answer == 0:
                break

            elif answer == 1:
                print("\n===== PROGRAMMING LANGUAGE =====")
                print("A programming language is used to give")
                print("instructions to a computer.")

                print("\nEXAMPLE:")
                print("HELLO WORLD!")
                print("WELCOME TO PROGRAMMING!")

            elif answer == 2:
                print("\n===== PYTHON PROGRAMMING =====")
                print("Python was created by Guido van Rossum in 1991.")
                print("It is a high-level, interpreted programming language.")

                print("\nEXAMPLE:")

                name = input("Enter your name: ")
                course = input("Enter your course: ")

                print("Hello", name)
                print("Your course is", course)
                print("WELCOME TO PYTHON!")

            elif answer == 3:
                print("\n===== ABOUT PYTHON =====")
                print("[1] Simple and Easy to Learn")
                print("[2] Readable Syntax")
                print("[3] Versatile")
                print("[4] Huge Community")

                definition = int(input("Why learn Python?: "))

                if definition == 1:
                    print("Great for beginners!")
                    print("Python is easy to understand.")

                elif definition == 2:
                    print("Code looks almost like English.")

                elif definition == 3:
                    print("Used in AI, web development,")
                    print("automation, games, and many more.")

                elif definition == 4:
                    print("Python has a huge community")
                    print("that helps programmers.")

                else:
                    print("INVALID CHOICE!")

            else:
                print("INVALID LESSON!")

    # ==========================================
    # TOPIC 5: BASIC SYNTAX
    # ==========================================

    elif topics == 5:

        while True:
            print("\n===== BASIC SYNTAX =====")
            print("[1] Print Statement")
            print("[2] Variables")
            print("[3] Comments")
            print("[4] User Input")
            print("[5] Data Types")
            print("[0] Back to Main Menu")

            try:
                answer = int(input("Choose Lesson: "))
            except ValueError:
                print("INVALID INPUT!")
                continue

            if answer == 0:
                break

            elif answer == 1:
                print("\n===== PRINT STATEMENT =====")
                print("Used to display output.")

                print("HELLO WORLD!")
                print("WELCOME TO PYTHON!")

            elif answer == 2:
                print("\n===== VARIABLES =====")
                print("Variables store information.")

                name = "Juan"
                age = 18

                print("Name:", name)
                print("Age:", age)

            elif answer == 3:
                print("\n===== COMMENTS =====")
                print("Comments are notes in a program.")
                print("They are ignored by Python.")

                # This is a comment
                print("THIS IS A PYTHON PROGRAM!")

            elif answer == 4:
                print("\n===== USER INPUT =====")
                print("Used to get information from the user.")

                name = input("Enter your name: ")
                print("HELLO", name)

            elif answer == 5:
                print("\n===== DATA TYPES =====")

                name = "Juan"
                age = 18
                grade = 90.5
                is_student = True

                print("Name:", name, type(name))
                print("Age:", age, type(age))
                print("Grade:", grade, type(grade))
                print("Student:", is_student, type(is_student))

            else:
                print("INVALID LESSON!")

    # ==========================================
    # TOPIC 6: ARITHMETIC OPERATORS
    # ==========================================

    elif topics == 6:

        while True:
            print("\n===== ARITHMETIC OPERATORS =====")
            print("[1] Addition")
            print("[2] Subtraction")
            print("[3] Multiplication")
            print("[4] Division")
            print("[5] Floor Division")
            print("[6] Modulus")
            print("[7] Exponentiation")
            print("[8] Complete Calculator")
            print("[0] Back to Main Menu")

            try:
                answer = int(input("Choose Lesson: "))
            except ValueError:
                print("INVALID INPUT!")
                continue

            if answer == 0:
                break

            elif answer in range(1, 9):
                print("\n===== ARITHMETIC OPERATORS =====")

                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if answer == 1:
                    print("Addition:", num1 + num2)

                elif answer == 2:
                    print("Subtraction:", num1 - num2)

                elif answer == 3:
                    print("Multiplication:", num1 * num2)

                elif answer == 4:
                    if num2 != 0:
                        print("Division:", num1 / num2)
                    else:
                        print("CANNOT DIVIDE BY ZERO!")

                elif answer == 5:
                    if num2 != 0:
                        print("Floor Division:", num1 // num2)
                    else:
                        print("CANNOT DIVIDE BY ZERO!")

                elif answer == 6:
                    if num2 != 0:
                        print("Modulus:", num1 % num2)
                    else:
                        print("CANNOT DIVIDE BY ZERO!")

                elif answer == 7:
                    print("Exponentiation:", num1 ** num2)

                elif answer == 8:
                    print("Addition:", num1 + num2)
                    print("Subtraction:", num1 - num2)
                    print("Multiplication:", num1 * num2)

                    if num2 != 0:
                        print("Division:", num1 / num2)
                        print("Floor Division:", num1 // num2)
                        print("Modulus:", num1 % num2)
                    else:
                        print("Division: CANNOT DIVIDE BY ZERO!")
                        print("Floor Division: CANNOT DIVIDE BY ZERO!")
                        print("Modulus: CANNOT DIVIDE BY ZERO!")

                    print("Exponentiation:", num1 ** num2)

            else:
                print("INVALID LESSON!")

    # ==========================================
    # INVALID MAIN MENU CHOICE
    # ==========================================

    elif topics == 0:
        print("THANK YOU FOR USING ACT MAJOR!")
        break

    else:
        print("INVALID LESSON! PLEASE CHOOSE 0 TO 6.")

    print("\nTHANK YOU FOR USING ACT MAJOR!")
    input("Press ENTER to return to Main Menu...")
