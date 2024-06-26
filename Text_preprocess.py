# Copyright 2024 
    Name : A V N S Bhavana (PhD Scholar)
    Email Id : bhavana.akkiraju@research.iiit.ac.in
# 
# All rights reserved.
import sys
import yaml
import re

class UnicodeRangeChecker:
    def __init__(self, unicode_ranges, punctuations):
        self.unicode_ranges = unicode_ranges
        self.punctuations = punctuations
        self.regex_patterns = {
            lang: f"[{''.join(ranges)}]+" for lang, ranges in unicode_ranges.items()
        }

    def create_punctuation_pattern(self, lang):
        general_punctuations = ''.join(self.punctuations.get('general', []))
        hyphens = ''.join(self.punctuations.get('hyphens', []))
        punctuation_pattern = general_punctuations + hyphens
        if lang in ['ar', 'ur', 'fa']:
            arabic_punctuations = ''.join(self.punctuations.get('arabic', []))
            punctuation_pattern += arabic_punctuations
        return re.compile(f"[{punctuation_pattern}]")
    
    def remove_punctuations(self, text, lang):
        punctuation_pattern = self.create_punctuation_pattern(lang)
        return punctuation_pattern.sub('', text)

    def in_unicode_range(self, text, lang):
        if lang not in self.regex_patterns:
            print(f"Language {lang} not supported.")
            return
        
        text = self.remove_punctuations(text, lang)
        regex_pattern = self.regex_patterns[lang]
        matching_characters = re.findall(regex_pattern, text)
        non_matching_characters = re.findall(f"[^{regex_pattern[1:-2]}]", text)
        
        matching_chars = ' '.join(matching_characters)
        non_matching_chars = ' '.join(non_matching_characters)
        
        return matching_chars, non_matching_chars

def contains_english(text):
    return bool(re.search(r'[A-Za-z0-9]', text))

def main(yaml_file, input_file, output_file, separate_file, language):
    # Load the YAML configuration file
    with open(yaml_file, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    # Extract Unicode ranges and punctuations
    unicode_ranges = config.get('unicode_ranges', {})
    punctuations = config.get('punctuations', {})

    # Create an instance of the UnicodeRangeChecker
    checker = UnicodeRangeChecker(unicode_ranges, punctuations)

    # Read text from the input file and write to the respective output files
    with open(input_file, 'r', encoding='utf-8') as text_file, \
         open(output_file, 'w', encoding='utf-8') as output_file, \
         open(separate_file, 'w', encoding='utf-8') as sep_file:
        
        for line in text_file:
            columns = line.strip().split(' ',1)
            if columns:
                text = columns[1]  # Assuming text is in the second column
                matching_chars, non_matching_chars = checker.in_unicode_range(text, language)
                # print(len(non_matching_chars))
                if contains_english(text):
                    sep_file.write(f"{columns[0]}\t{text}\n")
                else:
                    output_file.write(f"{columns[0]}\t{matching_chars}\n")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 6:
        print("Usage: python script.py <yaml_file> <input_file> <output_file> <separate_file> <language>")
        sys.exit(1)

    # Extract command-line arguments
    yaml_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    separate_file = sys.argv[4]
    language = sys.argv[5]

    main(yaml_file, input_file, output_file, separate_file, language)

