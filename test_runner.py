from caesar_cipher import caesar_encrypt, caesar_decrypt

def run_test(name, func, expected):
    result = func()
    if result == expected:
        print(f"[PASS] {name}")
    else:
        print(f"[FAIL] {name} — expected: {expected}, got: {result}")

def test_cases():
    run_test("Encrypt ABC +3", lambda: caesar_encrypt("ABC", 3), "DEF")
    run_test("Decrypt DEF -3", lambda: caesar_decrypt("DEF", 3), "ABC")
    run_test("Encrypt XYZ +3 (wrap)", lambda: caesar_encrypt("XYZ", 3), "ABC")
    run_test("Decrypt ABC -3 (wrap)", lambda: caesar_decrypt("ABC", 3), "XYZ")
    run_test("Encrypt Hello, World! +5", lambda: caesar_encrypt("Hello, World!", 5), "Mjqqt, Btwqi!")
    run_test("Decrypt Mjqqt, Btwqi! -5", lambda: caesar_decrypt("Mjqqt, Btwqi!", 5), "Hello, World!")

if __name__ == '__main__':
    test_cases()