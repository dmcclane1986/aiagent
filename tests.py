from functions.run_python import run_python_file

def main():
    """Run tests for the run_python_file function."""
    
    print("Test 1: run_python_file('calculator', 'main.py')")
    print("=" * 50)
    result1 = run_python_file("calculator", "main.py")
    print(result1)
    print()
    
    print("Test 2: run_python_file('calculator', 'tests.py')")
    print("=" * 50)
    result2 = run_python_file("calculator", "tests.py")
    print(result2)
    print()
    
    print("Test 3: run_python_file('calculator', '../main.py') - Should return error")
    print("=" * 50)
    result3 = run_python_file("calculator", "../main.py")
    print(result3)
    print()
    
    print("Test 4: run_python_file('calculator', 'nonexistent.py') - Should return error")
    print("=" * 50)
    result4 = run_python_file("calculator", "nonexistent.py")
    print(result4)
    print()

if __name__ == "__main__":
    main()