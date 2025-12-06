from functions.run_python_file import run_python_file

def tests():
    print("Executing file 'main.py' with args '':")
    print(run_python_file("calculator", "main.py"))
    print()
    print("=================================================================")
    print()

    print("Executing file 'main.py' with args '[\"3 + 5\"]':")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()
    print("=================================================================")
    print()

    print("Executing file 'tests.py' with args '':")
    print(run_python_file("calculator", "tests.py"))
    print()
    print("=================================================================")
    print()

    print("Executing file '../main.py' with args '':")
    print(run_python_file("calculator", "../main.py"))
    print()
    print("=================================================================")
    print()

    print("Executing file 'nonexistent.py' with args '':")
    print(run_python_file("calculator", "nonexistent.py"))
    print()
    print("=================================================================")
    print()

    print("Executing file 'lorem.txt' with args '':")
    print(run_python_file("calculator", "lorem.txt"))
    print()
    print("=================================================================")
    print()


tests()