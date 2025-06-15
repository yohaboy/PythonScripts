import os

folder_path = './my_texts'
output_file = 'merged.txt'

with open(output_file, 'w') as outfile:
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')

print(f'All .txt files merged into {output_file}')

