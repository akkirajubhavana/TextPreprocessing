# TextPreprocessing

This script preprocesses text data by removing punctuation and special characters based on language-specific Unicode ranges. It supports multiple languages and can be customized using a YAML configuration file.

## Usage

### 1. Install Dependencies

Ensure you have Python installed on your system. Install the required Python packages listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```
### 2. Prepare Input Data
  Prepare your input text data in a text file. Each line in the file represents a piece of text to be processed. If you have tab-separated files with text data and IDs, ensure that the text is in the second column.
### 3. Update YAML Configuration
   Update the YAML configuration file (config.yaml) to specify Unicode ranges and punctuation rules for each supported language. See the provided config.yaml for an example.
   ```bash
        unicode_ranges:
          ar: 
            - '\u0621-\u0629\u062A-\u062D\u062E\u062F\u0630-\u0638\u063A\u0641-\u064A\u064B-\u0652\u0660-\u0669'
          ur: 
            - '\u0621-\u0642\u0644-\u0648\u066B\u066C\u0679\u067E\u0686\u0688\u0691\u0698\u06A9\u06AF\u06BE\u06C1\u06CC\u06D2'
          fa: 
            - '\u0621-\u0629\u062A-\u062D\u062E-\u062F\u0630-\u0652\u0654\u067E\u0686\u0698\u06A9\u06AF\u06CC'
        punctuations:
          general: 
            - '\u0021-\u0029\u002B-\u002F\u003A-\u003E\u005B-\u005F\u007C\u00A9\u00AB-\u00BB'
          hyphens: 
            - '\u2010-\u2014\u2026\u2030\u20AC'
          arabic: 
            - '\u0609\u060C-\u061F\u066D\u06D4\u066A-\u066C'
   ```
### 4. Run the Script
  Execute the script from the command line, providing the input file, output file, and YAML configuration file paths as arguments. Optionally, you can specify a log file path to save log messages.
   ```bash 
          python preprocess.py input_file.txt output_file.txt config.yaml --log log_file.txt 
  ```
    input_file.txt: Path to the input text file.
    output_file.txt: Path to the output file where preprocessed text will be saved.
    config.yaml: Path to the YAML configuration file.
    --log log_file.txt (optional): Path to the log file.
   
## Configuration
  The YAML configuration file (config.yaml) contains Unicode ranges and punctuation rules for each supported language. You can customize these ranges and rules according to your requirements.

## Logging**
The script logs information, warnings, and errors during execution. If a log file path is provided, log messages will be saved to that file. Otherwise, logs will be printed to the console.

## Dependencies 
  1) Python 3.x
  2) langdetect
  3) PyYAML
  
  Install the dependencies using pip:
   ```bash 
           pip install -r requirements.txt
  ```
    
## License
This project is licensed under the MIT License. See the LICENSE file for details.
