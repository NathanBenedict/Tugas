import sys

x = "Hello"
alphabets = digits = special = 0

for line in sys.stdin:
    x = line
    for i in range(len(x)):
        if((x[i] >= 'a' and x[i] <= 'z') or (x[i] >= 'A' and x[i] <= 'Z')): 
            alphabets = alphabets + 1 
        elif(x[i] >= '0' and x[i] <= '9'):
            digits = digits + 1
        else:
            special = special + 1

sys.stdout.write("Total huruf: " + str(alphabets))
sys.stdout.write('\n')
sys.stdout.write("Total angka: " + str(digits))
sys.stdout.write('\n')
sys.stdout.write("Total symbol: " + str(special))
sys.stdout.write('\n')
