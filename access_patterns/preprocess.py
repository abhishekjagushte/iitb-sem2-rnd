import re
import os

def list_and_process_files(directory, config):
    try:
        # List all entries in the directory
        entries = os.listdir(directory)

        for dir in config.keys():
            output_dir = os.path.join(directory, dir)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            for entry in entries:
                entry_path = os.path.join(directory, entry)
                output_path = os.path.join(output_dir, entry)    
                
                # Check if it is a file
                if os.path.isfile(entry_path):
                    # print(entry_path, output_path, config[dir])
                    remove_lines_with_pattern(entry_path, output_path, config[dir])
                else:
                    print(entry_path)
    except Exception as e:
        print("Error: ", e)


def remove_lines_with_pattern(input_file, output_file, pattern):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        file.write("eip,vpn,ps,e,ts\n")
        for line in lines:
            if re.match(pattern, line):
                file.write(line)

pattern = r"([0-9]+,){4}[0-9]*"
# pattern = r"([0-9]+,){3}7"


configs ={
    # "only_l2_hits": r"([0-9]+,){3}7",
    # "all": r"([0-9]+,){3}[0-9]*",
    # "L2_hits_and_miss": r"([0-9]+,){3}[789]",
    "NUCA_hit": r"([0-9]+,){3}8,[0-9]*",
    # "L2_miss": r"([0-9]+,){3}[89]"
}


directory_path = '/home/abhishekjagushte/IITB/rnd/iitb-sem2-rnd/access_patterns/500M'
list_and_process_files(directory_path, configs)

