def sqr(x): # rightmost is LSB
    x = str(x)

    num_digits = len(x)

    jumpCount = "0"*len(x)
    stackCount = x
    together = ""
    total_digimons = len(x) # helps for hyphens to arrange mult table

    # this will hold the multiplication table
    mult_table = []
    # end of multiplication table
    print("progpos1")
    for i in range(num_digits-1, -1,-1): # silly range function (start, AFTER LAST, step)
        if x[i]=="0":
            #print("-"*total_digimons + jumpCount)
            mult_table.append("-"*total_digimons + jumpCount)
        elif x[i]=="1":
            #print("-"*total_digimons + stackCount)
            mult_table.append("-"*total_digimons + stackCount)
        stackCount = stackCount + "0"
        jumpCount = jumpCount + "0"
        total_digimons = total_digimons - 1
        print("progpos2")
    binary_chart = "1"
    binary_to_unary_variable = ""
    unary_accumulator = ""
    checkCount = 0
    binCounts = (len(x) + len(x))*[0]
    binCountsUnary = (len(x) + len(x))*[""]
    pureBinaryResult = (len(x) + len(x))*[0] # this is the main output everything else is auxiliary to the programming/debugging
    
    print("progpos3")
    
    for i in range(len(mult_table[0])-1,0,-1):
        binary_to_unary_variable = binary_chart
        for j in range(0,len(mult_table)):
            if mult_table[j][i]=="1":
                unary_accumulator = unary_accumulator + binary_to_unary_variable
                binCounts[len(mult_table[0])-1 - i] = binCounts[len(mult_table[0])-1 - i] + 1; # need the index of the element found widthways in the mult table
                binCountsUnary[len(mult_table[0])-1 - i] = binCountsUnary[len(mult_table[0])-1 - i] + "1"
                checkCount = checkCount + len(binary_to_unary_variable)
        binary_chart = binary_chart + binary_chart # simulates an array of the values of each bit in a binary number
        print("progpos4") # stalls here for large numbers

    for x in range(0,len(binCountsUnary)):
        print("progpos5")
        for y in range(0,len(binCountsUnary[x]), 1):
            print("progpos6")
            if not(binCountsUnary[x]=="1" or binCountsUnary[x]==""):
                while len(binCountsUnary[x])>1:
                    binCountsUnary[x] = binCountsUnary[x].replace("11", "", 1)
                    binCountsUnary[x+1] = binCountsUnary[x+1] + "1"
    out = ""
    numberStarted = False;
    for x in reversed(binCountsUnary):
        print("progpos7")
        if x=="" and numberStarted:
            out = out + "0"
        elif x=="1":
            out = out + "1"
            numberStarted = True
            
    print("progpos8")
    return out
