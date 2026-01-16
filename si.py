import sys
if (sys.argv) == 4:
    print("User input given")
    script_name = sys.argv[0]
    principle= float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    simple_interest=(principle * rate * time)/100

 print("principle:",principle )
    print("rate:",rate )
    print("time:",time)
    print("simple interest:",simple_interest)

else:
    print("User input not given")
    script_name = sys.argv[0]
    principle = 3.0
    rate = 2.0
    time = 40.0
    simple_interest=(principle * rate * time)/100

    print("principle:",principle )
    print("rate:",rate )
    print("time:",time)
    print("simple interest:",simple_interest)
    
    
