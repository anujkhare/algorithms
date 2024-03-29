"""
The directory is structured as follows:

    topic1/
        q1.py
        q2.py
        ...
    topic2/
        ...

For each question, there is some meta-data in the comments of the `.py` file itself.
Supported tags are listed in the code below.
"""

from tabulate import tabulate
from tqdm import tqdm
from typing import Dict
import pathlib
import pandas as pd


SUPPORTED_FIELDS = [
    'Name',
    'Topic',
    'Sub-topic',
    'Difficulty',
    'Bookmarked',
    'Link',
    'Approach',
    'Time complexity',
    'Space complexity',
    'Notes',
    'Website',
]


def parse_file(path_to_file: pathlib.Path) -> Dict[str, str]:
    metadata = {}
    with open(str(path_to_file), 'r') as infile:
        lines = infile.read().split('\n')
    for line in lines:
        if not line.startswith('##') or '::' not in line:
            continue

        line = line.lstrip('##').strip()
        field, value = line.split('::')
        field, value = field.strip(), value.strip()
        if field not in SUPPORTED_FIELDS:
            print('Unknown field: "{}"'.format(field))
            continue

        metadata[field] = value

    metadata['Name'] = path_to_file.stem
    metadata['Topic'] = path_to_file.parent.name

    return metadata


def get_df_from_folders(folder_path: str) -> pd.DataFrame:
    all_data = []
    for path_to_file in tqdm(list(pathlib.Path(folder_path).glob('**/*.py'))):
        all_data.append(parse_file(path_to_file))

    return pd.DataFrame(all_data)


def main():
    df = get_df_from_folders('solutions')
    df.fillna('', inplace=True)
    df = df[SUPPORTED_FIELDS]
    df.sort_values(by=['Topic', 'Sub-topic', 'Difficulty'], ascending=True, inplace=True)
    df.reset_index(inplace=True, drop=True)
    md_table = tabulate(df, tablefmt='pipe', headers='keys')
    with open('table.md', 'w') as f:
        f.write(md_table)


if __name__ == '__main__':
    main()
