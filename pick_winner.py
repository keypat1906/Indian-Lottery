import time
import argparse
import os
import mmap
from collections import defaultdict


def pick_winner(file):  
    '''
    Function which calculate the winners
    Return the number of winners in each group
    '''  
    # Loop will keep running until Control C is pressed
    # Enter as many as numbers you like
    while True:
        input_data = input().split()
        
        # validate the input data 
        # Check if it is numbers, otherwise return the error
        for data in input_data:
            if not data.isdigit():
                print("Enter numbers only")
                return 
        # Check if total number does not exceed 5
        if len(input_data) > 5:
            print( "Only 5 numbers are allowed")
            return
        
        print("Winner Numbers:", input_data)
        start_time = time.time()
    
        input_data.sort()
        set_input_data = set(input_data)
        count_dic = defaultdict(int)

        with open(file, 'r') as f:
            with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:                
                while mmap_obj.readline():
                    line = str(mmap_obj.readline().decode("utf-8") )
                    common_data = set_input_data.intersection(set(line.replace('\\','').split()))
                    count_dic[len(common_data)] += 1

        print("--------------------------------------")
        print("| Numbers matching   |      Winners   ") 
        print("--------------------------------------")
        print("| 5                  |      ",count_dic[5] )
        print("| 4                  |      ",count_dic[4] )
        print("| 3                  |      ",count_dic[3] )
        print("| 2                  |      ",count_dic[2] )
        print("--------------------------------------")
        print("Total time taken to pull winners",time.time()-start_time)
        print("")
        print("")
        print("READY")
        print("")

def process_line(line):
    return "FOO: %s" % line

def check_file_exists(file):
    """
    'Type' for argparse - checks that file exists
    """
    if not os.path.exists(file):
        raise argparse.ArgumentTypeError("File {0} does not exist".format(file))
    return file


def main():
    """
    Main function to process the winners
    Enter the file name as argument to run 
    e.g  'pick_winner.py  FILENAME'
    """
    print("READY")
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=check_file_exists)
    args = parser.parse_args()
    file = os.getcwd() +  "/" + str(args.file)
    pick_winner(file)


if __name__ == "__main__":
    main()


