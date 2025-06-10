from functions.get_files_info import get_files_info

def main():
    """Run tests for the get_files_info function."""
    
    print("Test 1: get_files_info('calculator', '.')")
    print("=" * 50)
    result1 = get_files_info("calculator", ".")
    print(result1)
    print()
    
    print("Test 2: get_files_info('calculator', 'pkg')")
    print("=" * 50)
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    print()
    
    print("Test 3: get_files_info('calculator', '/bin') - Should return error")
    print("=" * 50)
    result3 = get_files_info("calculator", "/bin")
    print(result3)
    print()
    
    print("Test 4: get_files_info('calculator', '../') - Should return error")
    print("=" * 50)
    result4 = get_files_info("calculator", "../")
    print(result4)
    print()

if __name__ == "__main__":
    main()