# Copyright 2024 
    Name : A V N S Bhavana (PhD Scholar)
    Email Id : bhavana.akkiraju@research.iiit.ac.in
# 
# All rights reserved.
import argparse
import logging
import re
from langdetect import detect
import yaml

class TextPreprocessor:
    def __init__(self, yaml_file):
        self.load_yaml(yaml_file)

    def load_yaml(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as ip:
                data = yaml.safe_load(ip)
            
            self.unicode_ranges = data.get('unicode_ranges', {})
            self.punctuations = data.get('punctuations', {})
        except FileNotFoundError:
            logging.error(f"YAML file '{file_path}' not found.")
            raise
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML file: {e}")
            raise

    def detect_language(self, text):
        try:
            return detect(text)
        except Exception as e:
            logging.error(f"Error detecting language: {e}")
            raise

    def preprocess_text(self, text):
        try:
            language = self.detect_language(text)
            unicode_range = self.unicode_ranges.get(language)

            if not unicode_range:
                logging.warning(f"No Unicode range found for language '{language}'. Skipping preprocessing.")
                return text

            joined_range = ''.join(unicode_range)
            regex_pattern = f"[{joined_range}]+"
            unicode_regex = re.compile(regex_pattern)

            general_punctuations = ''.join(self.punctuations.get('general', []))
            arabic_punctuations = ''.join(self.punctuations.get('arabic', []))
            hyphens = ''.join(self.punctuations.get('hyphens', []))
            punctuation_pattern = f"[{general_punctuations}{arabic_punctuations}{hyphens}]"
            punctuation_regex = re.compile(punctuation_pattern)

            selected_text = unicode_regex.findall(text)
            selected_text = [word for word in selected_text if not punctuation_regex.match(word)]
            processed_text = ' '.join(selected_text)

            return processed_text
        except Exception as e:
            logging.error(f"Error preprocessing text: {e}")
            raise

def clean_and_overwrite(input_file, output_file, yaml_file):
    try:
        preprocessor = TextPreprocessor(yaml_file)

        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if len(line.split('\t')) == 1:
                    processed_text = preprocessor.preprocess_text(line.strip())
                    outfile.write(f'{processed_text}\n')
                else:
                    file_id, text = line.strip().split('\t')
                    processed_text = preprocessor.preprocess_text(text)
                    outfile.write(f'{file_id}\t{processed_text}\n')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text Preprocessor')
    parser.add_argument('input_file', metavar='input_file', type=str,
                        help='Input file path')
    parser.add_argument('output_file', metavar='output_file', type=str,
                        help='Output file path')
    parser.add_argument('yaml_file', metavar='yaml_file', type=str,
                        help='YAML file path')
    parser.add_argument('--log', metavar='log_file', type=str, default=None,
                        help='Log file path (optional)')

    args = parser.parse_args()

    if args.log:
        logging.basicConfig(filename=args.log, level=logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO)

    try:
        clean_and_overwrite(args.input_file, args.output_file, args.yaml_file)
        logging.info("Text preprocessing completed successfully.")
    except Exception:
        logging.exception("An error occurred during text preprocessing.")
