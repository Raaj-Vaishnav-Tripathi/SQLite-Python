import yaml
from app.sqlite_explorer import SQLiteDatabaseReader
import argparse


def main() -> None:
    arg_parser = argparse.ArgumentParser(description="A simple SQLite file reader")
    arg_parser.add_argument('filename')
    arg_parser.add_argument('command')
    arg_parser.add_argument('--config', default='project_config.yml', help='Path to the configuration file')

    args = arg_parser.parse_args()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    # Use configuration options if provided (e.g., logging level)
    logging_level = config.get('logging_level', 'info')
    # ... other configuration options

    with open(args.filename, 'rb') as f:
        print(SQLiteFile.exec(f, args.command))


if __name__ == '__main__':
    main()