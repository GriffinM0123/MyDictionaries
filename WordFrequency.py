import string

def main():
    infile = open("AI.txt", "r")

    d = {}
    
    count = 0

    removetable = str.maketrans("","", string.punctuation)
    infile = [s.translate(removetable) for s in infile]

    for line in infile:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for w in words:
            if w in d:
                d[w] = d[w] + 1
            else:
                d[w] = 1
    print(d)

main()

