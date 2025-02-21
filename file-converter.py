import sys
from pathlib import Path
import markdown as md

def main():
    if len(sys.argv) < 2:
        raise ValueError('Command is required')
    command = sys.argv[1]
    print(sys.argv)
    if (command == "markdown"):
        markdown()
    else:
        raise ValueError('Invalid command.\nPlease input the command within [markdown]')

def markdown():
    print("Convert markdown to html")
    inputPath = sys.argv[2]
    if not is_md_file(inputPath):
        raise ValueError('Inputfile is not a markdown file.\nPlease input a file with ending .md.')
    outputPath = sys.argv[3]
    if not is_html_file(outputPath):
        raise ValueError('Outputpath is not a HTML file.\nPlease input a file with ending .html.')
    with open(inputPath) as f:
        md_content = f.read()
        html_content = md.markdown(md_content)
    with open(outputPath, 'w') as f:
        f.write(html_content)
    print(f'Convert from {inputPath} to {outputPath} succeeded!')

def is_md_file(file_path):
    return Path(file_path).suffix == '.md'

def is_html_file(file_path):
    return Path(file_path).suffix == '.html'

if __name__ == "__main__":
    main()