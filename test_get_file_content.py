from functions.get_file_content import get_file_content

def tests():
    print("Result for 'lorem.txt' file:")
    result = get_file_content("calculator", "lorem.txt")
    result_split = result.split("[...File")
    print(f"Mesage length: {len(result_split[0])}")
    print(result_split[1])
    print()
    print("=================================================================")
    print()

    print("Result for 'main.py' file:")
    print(get_file_content("calculator", "main.py"))
    print()
    print("=================================================================")
    print()

    print("Result for 'pkg/calculator.py' file:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()
    print("=================================================================")
    print()

    print("Result for '/bin/cat' file:")
    print(get_file_content("calculator", "/bin/cat"))
    print()
    print("=================================================================")
    print()

    print("Result for 'pkg/does_not_exist.py' file:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()

tests()

