from functions.get_files_info import get_files_info

def tests():

    print("Result for '.' directory:")
    results =  get_files_info("calculator")
    print(results)
    print()

    print("Result for 'pkg' directory:")
    results = get_files_info("calculator", "pkg")
    print(results)
    print()

    print("Result for '/bin' directory:")
    results = get_files_info("calculator", "/bin")
    print(results)
    print()


tests()