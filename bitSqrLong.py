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
    binary_chart = "1"
    ##binary_to_unary_variable = ""
    ##unary_accumulator = ""
    ##checkCount = 0
    binCounts = (len(x) + len(x))*[0]
    binCountsUnary = (len(x) + len(x))*[""]
    pureBinaryResult = (len(x) + len(x))*[0] # this is the main output everything else is auxiliary to the programming/debugging
    ## debug section
    for x in mult_table:
        print(x)
    ## end debug section
    input("progpaused")
    for i in range(len(mult_table[0])-1,0,-1): # stuck in this loop for large inputs () tick if fixed
        ##binary_to_unary_variable = binary_chart
        ##print(binary_to_unary_variable)
        print("end of currnum unit")
        for j in range(0,len(mult_table)):
            if mult_table[j][i]=="1":
                ##unary_accumulator = unary_accumulator + binary_to_unary_variable
                binCounts[len(mult_table[0])-1 - i] = binCounts[len(mult_table[0])-1 - i] + 1; # need the index of the element found widthways in the mult table
                binCountsUnary[len(mult_table[0])-1 - i] = binCountsUnary[len(mult_table[0])-1 - i] + "1"
                ##checkCount = checkCount + len(binary_to_unary_variable)
        ##binary_chart = binary_chart + binary_chart # simulates an array of the values of each bit in a binary number

    for x in range(0,len(binCountsUnary)):
        for y in range(0,len(binCountsUnary[x]), 1):
            if not(binCountsUnary[x]=="1" or binCountsUnary[x]==""):
                while len(binCountsUnary[x])>1:
                    binCountsUnary[x] = binCountsUnary[x].replace("11", "", 1)
                    binCountsUnary[x+1] = binCountsUnary[x+1] + "1"
    out = ""
    numberStarted = False;
    for x in reversed(binCountsUnary):
        if x=="" and numberStarted:
            out = out + "0"
        elif x=="1":
            out = out + "1"
            numberStarted = True
    return out
