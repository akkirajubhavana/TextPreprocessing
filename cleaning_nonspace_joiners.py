import re
import sys

# List of non-space joiners to check
non_space_joiners = [
    '\u200B',  # Zero Width Space
    '\u200C',  # Zero Width Non-Joiner
    '\u200D',  # Zero Width Joiner
    '\u200E',  # Left-to-Right Mark
    '\u200F',  # Right-to-Left Mark
    '\u202A',  # Left-to-Right Embedding
    '\u202B',  # Right-to-Left Embedding
    '\u202C',  # Pop Directional Formatting
    '\u202D',  # Left-to-Right Override
    '\u2066',  # Left-to-Right Isolate
    '\u2067',  # Right-to-Left Isolate
    '\u2028'   # Line Separator
]

# Create a regex pattern to match any of the non-space joiners
pattern = re.compile(f"[{''.join(non_space_joiners)}]")

def clean_file(input_path, output_path):
    # Open the original file and create a new file for the cleaned content
    with open(input_path, 'r', encoding='utf-8') as ip, open(output_path, 'w', encoding='utf-8') as op:
        for line in ip:
            if pattern.search(line):
                # Print the lines that contain non-space joiners
                print(f"Line with non-space joiner: {line.strip()}")
            # Remove non-space joiners using the regex pattern
            cleaned_line = pattern.sub('', line)
            # Write the cleaned line to the new file
            op.write(cleaned_line)

    print(f"Cleaned file saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        clean_file(input_file_path, output_file_path)
