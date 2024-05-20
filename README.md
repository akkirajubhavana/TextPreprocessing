Text Preprocessing
This script preprocesses text data by removing punctuation and special characters based on language-specific Unicode ranges. It supports multiple languages and can be customized using a YAML configuration file.

Usage
To use the script, follow these steps:

Install Dependencies: Make sure you have Python installed on your system. You also need to install the required Python packages listed in requirements.txt. You can install them using pip:

bash
Copy code
pip install -r requirements.txt
Prepare Input Data: Prepare your input text data in a text file. Each line in the file represents a piece of text to be processed. If you have tab-separated files with text data and IDs, ensure that the text is in the second column.

Prepare YAML Configuration: Create a YAML configuration file (config.yaml) to specify Unicode ranges and punctuation rules for each supported language. See the provided config.yaml for an example.

Run the Script: Execute the script from the command line, providing the input file, output file, and YAML configuration file paths as arguments. Optionally, you can specify a log file path to save log messages.

bash
Copy code
python preprocess.py input_file.txt output_file.txt config.yaml --log log_file.txt
input_file.txt: Path to the input text file.
output_file.txt: Path to the output file where preprocessed text will be saved.
config.yaml: Path to the YAML configuration file.
--log log_file.txt (optional): Path to the log file.
Configuration
The YAML configuration file (config.yaml) contains Unicode ranges and punctuation rules for each supported language. You can customize these ranges and rules according to your requirements.

Logging
The script logs information, warnings, and errors during execution. If a log file path is provided, log messages will be saved to that file. Otherwise, logs will be printed to the console.

Dependencies
Python 3.x
langdetect
PyYAML
Install the dependencies using pip:

bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License. See the LICENSE file for details.
