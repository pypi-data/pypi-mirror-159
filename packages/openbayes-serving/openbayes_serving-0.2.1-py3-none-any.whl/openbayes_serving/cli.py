import argparse

from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Init predict file')
    # add optional arguments
    parser.add_argument(
        'output', 
        type=str, 
        nargs='?',
        default='predictor.py', 
        help='Init file name, default is predictor.py')
    args = parser.parse_args()

    # if file exists, ask user whether to overwrite
    if Path(args.output).is_file():
        print('File exists, overwrite? (y/n)')
        if input() == 'y':
            with open("predictor-template.py", "r") as template:
                with open(args.output, 'w') as f:
                    f.write(template.read())
        else:
            print('Abort')
    else:
        with open("predictor-template.py", "r") as template:
            with open(args.output, 'w') as f:
                f.write(template.read())


if __name__ == '__main__':
    main()
