from functions.write_file import write_file

def tests():
    print("Result writing to 'lorem.txt' file with content 'wait, this isn't lorem ipsum':")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print()
    print("=================================================================")
    print()

    print("Result writing to 'pkg/morelorem.txt' file with content 'wait, this isn'wait, this isn'lorem ipsum dolor sit amet':")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print()
    print("=================================================================")
    print()

    print("Result writing to '/tmp/temp.txt' file with content 'wait, this isn'wait, this isn'this should not be allowed':")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print()

tests()