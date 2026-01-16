import sys

if len(sys.argv) == 4:
    print("User input given")

    script_name = sys.argv[0]
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])

    simple_interest = (principal * rate * time) / 100

    print("Principal:", principal)
    print("Rate:", rate)
    print("Time:", time)
    print("Simple Interest:", simple_interest)

else:
    print("User input not given")

    script_name = sys.argv[0]
    principal = 3.0
    rate = 2.0
    time = 40.0

    simple_interest = (principal * rate * time) / 100

    print("Principal:", principal)
    print("Rate:", rate)
    print("Time:", time)
    print("Simple Interest:", simple_interest)
