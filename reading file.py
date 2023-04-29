

def main():
    infile = open("philosophers.txt", 'r')

    file_contents = infile.read()
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    #infile.close()
    print(file_contents)

main()