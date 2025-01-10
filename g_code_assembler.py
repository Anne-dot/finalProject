import re

 ###

# from tkinter import filedialog
# import os

# # Open folder dialog
# folder_selected = filedialog.askdirectory()

# # # Check if a folder was selected
# # if folder_selected:
# #     print("Selected folder:", folder_selected)
# # else:
# #     print("No folder selected.")

# files = os.listdir(folder_selected)

# # Print each file name
# for file_name in files:
#     print(file_name)


## eventually this will be the selection of the file
## this is example file relative path
file_path = '01288 uued uksed 2.nc'

## give a name for the output file based on the input file name
output_file_name = file_path[0:-3] + '.txt'

insert_lines = [
    ['( Algseaded masinale )', 'G00G21G17G90G40G49G80', 'G71G91.1'],
    ['()', '( T66riista vahetamine )', '()'],
    ['()', '( Spindli kiirus )'],
    ['()', '( Spindli peatamine )'],
    '(  )',

    ]

with open(file_path, 'r') as input_file, open(output_file_name, 'w', encoding='utf-8') as output_file:
    
    ## Add initial setup for the machine

    for i in insert_lines[0]:
        output_file.write(i + '\n')

    for line in input_file:

        # Tool change needs 'M06' added to the line
        # Additional comment for the operator added

        if line[0] == 'T':
            for i in insert_lines[1]:
                output_file.write(i + '\n')
            output_file.write(line.strip() + 'M06\n')

        # Add comment before spindle speed line
        elif line[0] == 'S':
            for i in insert_lines[2]:
                output_file.write(i + '\n')
            output_file.write(line)
            output_file.write('G94\n( T66tluse algus )\n')

        # Stop spindle before tool change
        elif line.strip == 'M5':
            for i in insert_lines[3]:
                output_file.write(i)
            output_file.write(line)

        elif line.strip():
            output_file.write(line)


