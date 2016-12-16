import sys

file = open(sys.argv[1], "r");

width = input("Number of flanking nucleotides: ")


prevLine = ""
inMiddle = False
header = ""


def parse_header(arr):
    """
        this functions receive an array with 
        and returns the proper header
    """
    for element in arr:
        element.replace(" ","")
        if (len(element) > 0 and element.startswith("rs")):
            return element.replace("=","")
            

for line in file:
    if(line[0] == '>'):
        prevLine = ""
        # got a header line
        fragments =  line.split("|")
        # print line
        bases =  [];
        for element in fragments:
            if element.startswith('alleles="'):
                bases = element[9:12].split("/")
                bases[0].strip()
                bases[1].strip()

        header  = parse_header(fragments[2].split(" "))
        # print "header", header
    elif(len(line.replace(" ","")) == 2):
        inMiddle = True
    else:
        if inMiddle:
            line = line.replace(" ","")
            line = line[0:width]
            
            
            prevLine = prevLine[-width:]
            print (">" + header.strip() + bases[0])
            print (prevLine  +  bases[0] + line)
            print "\n"  
            print (">" + header.strip() + bases[1])
            print (prevLine + bases[1] + line)
            print "\n"
            inMiddle = False
            
    if not inMiddle:
        prevLine = prevLine + line.replace(" ","")
        prevLine = prevLine.replace("\n","")
