from io import SEEK_CUR, SEEK_SET
from typing import BinaryIO, Any
import struct


class SQLiteDatabaseReader:
    """A simple reader for exploring basic information and structure of SQLite files."""

    def __init__(self, f: BinaryIO):
        self.file = f

        if self.read_bytes(16) != b'SQLite format 3\x00':
            raise ValueError('Not a valid SQLite file')

        self.page_size = self.read_uint16()

    def read_bytes(self, size: int) -> bytes:
        """Reads a specified number of bytes from the file."""
        return self.file.read(size)

    def read_uint16(self) -> int:
        """Reads and unpacks an unsigned 16-bit integer."""
        return struct.unpack('>H', self.read_bytes(2))[0]

    def execute_command(self, command: str) -> str:
        """Executes a basic dot command (currently only supports .dbinfo)."""
        if command[0] == '.':
            if command == '.dbinfo':
                return self.get_database_info()
            else:
                raise NotImplementedError(f'Unknown dot command: {command}')
        else:
            raise NotImplementedError('Only basic dot commands supported')

    def get_database_info(self) -> str:
        """Provides basic information about the database."""
        return '\n'.join((
            f'Database page size: {self.page_size}',
            f'Number of tables: TODO (implementation required)'
        ))

# Example usage (optional)
if __name__ == '__main__':
    with open('sample.db', 'rb') as f:
        reader = SQLiteDatabaseReader(f)
        info = reader.execute_command('.dbinfo')
        print(info)