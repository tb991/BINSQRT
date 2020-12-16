import bitSqrLong

## just in case :)

def check(pre_radix, post_radix):
    ## if it's two
    inputDeemed = "err"
    if pre_radix == "1":
        inputDeemed = "small"
    elif pre_radix == "10": 
        inputDeemed = "large"
    return inputDeemed
            
def allZeroes(post_radix):
    out = False
    if post_radix.count("0") == len(post_radix):
        out = True
    return out
    
x = "0.0"

# square of number is under two check
def u2c(raw_string):
    print("in: " + raw_string)
    dc = 0
    for p in raw_string:
        if p == "." and dc == 0:
            dc = dc + 1
            continue
        elif p != "0" and p != "1":
            print("input error")
            break
    # we're fine if here
    num = raw_string.split(".")
    x = bitSqrLong.sqr(num[0] + num[1])
    print(x)
    nextDigit = -1
    if len(x) == 2*(len(raw_string) - 1): # remove dot first
        # then it's over 2
        nextDigit = 0
    elif len(x) == 2*(len(raw_string) - 1) - 1:
        # then it's less than 2
        nextDigit = 1
    return nextDigit
# note that if you get zero then it means the rightmost digit of the input should have been zero, same for 1
## print("out: " + str(u2c("1.1")))
count = 0
x = "1.0"
y = "01"
while y != -1:
    y = u2c(x)
    if y==1:
        y = "1" # cand = 1.01 needs result = 1.01
        x = x + y
    elif y==-1:
        print("error")
        break
    else:
        y = "0" # cand = 1.1 needs result = 1.01 (may need 0 not sure)
        xpos = x.rfind("1")
        x = x[:xpos] + y
    a = input("press any button to continue...")
        
