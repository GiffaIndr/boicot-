def test_system():
    # Test system
    system = open("testing.txt", "r")
    print(system.read())
    system.close()

test_system()