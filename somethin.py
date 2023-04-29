

def main():
    file_contents = into_file()
    scalar_mult(file_contents)
    swap_first_last(file_contents)
    swap_first_last_using_negative_indexing(file_contents)
    make_a_file_with_math(file_contents)

def into_file():
    infile = open("integers.txt", 'r')
    file_contents = infile.read()
    infile.close()
    return file_contents.split(",")

def scalar_mult(file_contents):
    num = get_scalar()
    scaled_line = ""
    print("The list\n", file_contents, "\nwill be scaled by",num, "to get")
    for i in file_contents:
        scaled_int = str(int(i)*num)
        scaled_line += scaled_int + "  "
    print(scaled_line)

def get_scalar():
    valid = False
    while not valid:
        num = input("Give me an integer to be multiplied: ")
        try:
            num = int(num)
            print("that is a valid number")
            valid = True
        except:
            print("that is not a valid number")
    return num

def swap_first_last(swap):
    swap[0], swap[len(swap) - 1] = swap[len(swap) - 1], swap[0]
    print("The swapped list of the original is\n",swap)

def swap_first_last_using_negative_indexing(swap2):
    swap2[0], swap2[-1] = swap2[-1], swap2[0]
    print("The swapped list of the original, by using negative indexing\n", swap2)

def make_a_file_with_math(file_contents):
    outfile = open('output_part2_3.txt', 'w')
    outfile.write("Your Name: " + input("Write your name here: ") + "\n")
    outfile.write("LAB: LAB7" + "\n")
    outfile.write("Original list of numbers:" + "\n")
    outfile.write(str(file_contents)+ "\n")
    outfile.write("The sum of all the numbers is " + str(get_sum(file_contents)) + "\n")
    outfile.write("The average of all the numbers is " +str(get_avg(file_contents)) + "\n")
    outfile.write("The max of all the numbers is " +str(get_list_max(file_contents)) + "\n")
    outfile.write("The count of all the numbers is " +str(get_count(file_contents)) + "\n")
    outfile.close()

def get_sum(sum):
    total = 0
    for num in sum:
        total += int(num)
    return total

def get_avg(avg):
    return get_sum(avg) / len(avg)

def get_list_max(greatist):
    myMax = greatist[0]
    for i in greatist:
       if i >  myMax:
           myMax = i
    return myMax

def get_count(count):
    return len(count)


main()