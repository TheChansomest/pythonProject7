

def main():
    num_disks = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    move_disks(num_disks,from_peg,to_peg,temp_peg)
    print("All the pegs are moved!")



def move_disks(num_disks,from_peg,to_peg,temp_peg):
    if num_disks > 0:
        move_disks(num_disks,from_peg,to_peg,temp_peg)
        print(f"movea disc from peg {from_peg} to peg {to_peg} .")
        move_disks(num_disks-1,temp_peg, to_peg, from_peg)

main()