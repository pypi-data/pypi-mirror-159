import click
import base64
import binascii
import re
import sys
from importlib import metadata


pkgname = __name__.split('.')[0]

@click.command()
@click.argument('input', type=click.File('rb'))
@click.option('--encode/--decode', default=True, help='Run the appropriate process.')
@click.version_option(metadata.version(pkgname))
def main(input, encode):
    """
    Encode input stream by converting each chunk and storing it
    on a dedicated line with a checkusm control.

    Decode the stream by reverting the encoding process.
    """
    if encode:
        count = 0
        while True:
            count += 1
            chunk = input.read(24) # split input stream (%3 to avoid padding)
            if not chunk:
                break
            line = base64.b64encode(chunk).decode('ascii') # convert chunk
            crc = binascii.crc32(chunk) # caculate checksum
            click.echo(f'{count}: {line} {crc:08x}') # format line output

    else:
        line_num = 0
        chunks = b''
        for line in iter(input.read().decode('ascii').splitlines()):
            try:
                line_num, b64, crc = re.match(
                    r'^\s*(\d+):\s+([a-zA-Z0-9\+\/=]+)\s+(\w{8})\s*$',
                    line).groups()              # parse line
                chunk = base64.b64decode(b64)  # convert data
                # verify checksum
                if binascii.crc32(chunk) != int(crc, 16):
                    raise ValueError()
                chunks += chunk # store chunk

            except AttributeError:
                click.echo(f'Error parsing line {int(line_num)+1}')
                sys.exit(1)

            except ValueError:
                click.echo(f'Error verifying checksum for line {line_num}')
                sys.exit(1)

        click.echo(chunks, nl=False) # write file
