def test_system():
    # Test system
    system = open("testing.txt", "r")
    print(system.readlines())
    system.close()

test_system()