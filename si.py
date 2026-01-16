import sys
if len(sys.argv) == 4:
    print("Usage: python <principle> <rate> <time>")
    sys.exit(1)
    principle = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    simple_interest = (principle * rate * time)/100
    print("principle:", principle)
    print("Rate:",rate)
    print("Time:",time)
    print("Simple interest:", simple_interest)
else:
    print("Deafault values")
    principle = 100.0
    rate = 5.0
    time = 3.0
    simple_interest = (principle * rate * time)/100
    print("principle:", principle)
    print("Rate:",rate)
    print("Time:",time)
    print("Simple interest:", simple_interest)