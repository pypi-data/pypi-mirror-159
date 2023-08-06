import argparse
import json
from pathlib import Path

from regener.classes.pdf import PDF  # type: ignore


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i', '--input', action='store', required=True, type=Path,
        help='Path to folder with files (json, images, fonts)',
    )

    parser.add_argument(
        '-o', '--output', action='store', required=False, type=Path,
        help='Path to the pdf file or to directory where that pdf file will be generated',
    )

    return parser.parse_args()


def generate_pdf(content: dict, path: Path):
    pdf = PDF(
        orientation=content['metadata'].get('orientation') or 'portrait',
        unit=content['metadata'].get('units') or 'mm',
        format=content['metadata'].get('format') or 'A4',
    )
    pdf.add_page()
    pdf.load_from_json(content)
    pdf.install_font(content, path)
    pdf.load_layouts(content, path)
    pdf.load_items(content)
    return pdf


def select_output_path(argument_output: Path, argument_path: Path, content_path) -> str:
    if not argument_output:
        if not content_path:
            return 'cv.pdf'
        else:
            return str(argument_path / content_path)
    else:
        output_path = argument_output

        if argument_output.is_dir():
            output_path = argument_output / 'cv.pdf'

        return str(output_path)


def main():
    arguments = parse_arguments()
    json_file_path = Path(arguments.input) / 'cv.json'

    with open(json_file_path, 'r') as json_file:
        content = json.load(json_file)

    pdf_content = generate_pdf(content, arguments.input)
    pdf_content.output(select_output_path(arguments.output, arguments.input, content.get('output')))


if __name__ == '__main__':
    main()
