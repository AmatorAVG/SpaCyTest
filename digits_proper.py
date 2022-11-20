import spacy
from collections import Counter
import argparse


def html_table(lol):
    result = '<table>'
    for sublist in lol:
        result += '<tr align="right"><td>'
        result += '</td><td>'.join(sublist)
        result += '</td></tr>'
    result += '</table>'
    return result


def main():

    parser = argparse.ArgumentParser(description='Program for seeking digits and proper nouns')
    parser.add_argument('path', nargs='?', help='Path for output file', default='output.html')
    args = parser.parse_args()

    nlp = spacy.load("en_core_web_sm")

    text = input().replace("/", " ")
    doc = nlp(text)

    entries = [token.text for token in doc if token.pos_ == "PROPN" or token.is_digit]
    entries_freq = Counter(entries)
    entries_for_html = [[key, str(value)] for key, value in entries_freq.items()]

    file = open(args.path, "w")
    file.write(html_table(entries_for_html))
    file.close()


if __name__ == '__main__':
    main()
