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
        self.punctuation_pattern = self.create_punctuation_pattern()

    def create_punctuation_pattern(self):
        general_punctuations = ''.join(self.punctuations.get('general', []))
        arabic_punctuations = ''.join(self.punctuations.get('arabic', []))
        hyphens = ''.join(self.punctuations.get('hyphens', []))
        punctuation_pattern = f"[{general_punctuations}{arabic_punctuations}{hyphens}]"
        return re.compile(punctuation_pattern)
    
    def remove_punctuations(self, text):
        return self.punctuation_pattern.sub('', text)

    def in_unicode_range(self, text, lang):
        if lang not in self.regex_patterns:
            print(f"Language {lang} not supported.")
            return
        
        text = self.remove_punctuations(text)
        regex_pattern = self.regex_patterns[lang]
        matching_characters = re.findall(regex_pattern, text)
        non_matching_characters = re.findall(f"[^{regex_pattern[1:-2]}]", text)
        
        if matching_characters:
            matching_chars = ' '.join(matching_characters)
        else:
            matching_chars = "NAAN"
        
        if non_matching_characters:
            non_matching_chars = ' '.join(non_matching_characters)
        else:
            non_matching_chars = "NANA "
        
        return matching_chars, non_matching_chars

def main(yaml_file, input_file, output_file, language):
    # Load the YAML configuration file
    with open(yaml_file, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    # Extract Unicode ranges and punctuations
    unicode_ranges = config.get('unicode_ranges', {})
    punctuations = config.get('punctuations', {})

    # Create an instance of the UnicodeRangeChecker
    checker = UnicodeRangeChecker(unicode_ranges, punctuations)

    # Read text from the input file and write to the output file
    with open(input_file, 'r', encoding='utf-8') as text_file, open(output_file, 'w', encoding='utf-8') as output_file:
        for line in text_file:
            columns = line.strip().split('\t')
            if columns:
                text = columns[1]  # Assuming text is in the second column
                matching_chars, non_matching_chars = checker.in_unicode_range(text, language)
                output_file.write(f"{columns[0]}\t{matching_chars}\n")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <yaml_file> <input_file> <output_file> <language>")
        sys.exit(1)

    # Extract command-line arguments
    yaml_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    language = sys.argv[4]

    main(yaml_file, input_file, output_file, language)
