import argparse
import re
from multiprocessing.pool import ThreadPool
from pathlib import Path
import subprocess
from time import sleep


EXTRACT_RE = re.compile(r'\s+A\s+(\d+\.\d+\.\d+\.\d+)')


class MassResolver:
    def __init__(self, args):
        self.args = args

    def process(self, host):
        host = host.strip()
        if not host:
            return
        cmd = ['echo', host] if self.args.echo else ['dig', host, 'a']
        output = subprocess.check_output(cmd, text=True)
        return host, EXTRACT_RE.findall(output)

    def run(self):
        # no need for actual multiprocess Pool
        # Python will just spawn shells, not actually process anything
        pool = ThreadPool(processes=self.args.processes)
        with self.args.inputfile.open('r') as inp:
            with (self.args.output / 'output.txt').open('w') as out:
                for host, res in pool.imap_unordered(self.process, inp):
                    line = f'{host}:{",".join(res)}'
                    print(line)
                    out.write(line)
                    out.write('\n')
        if self.args.wait:
            sleep(self.args.wait)


def parseargs():
    parser = argparse.ArgumentParser(description='Mass DNS Resolver')
    parser.add_argument(
        '-o', '--output',
        default='/output',
        type=Path,
        help='output directory for results'
    )
    parser.add_argument(
        '-p', '--processes',
        default=10,
        type=int,
        help='number of processes',
    )
    parser.add_argument(
        '--echo',
        action='store_true',
        help='just echo input back instead of resolving DNS (passive testing)',
    )
    parser.add_argument(
        '--wait',
        type=int,
        help='sleep WAIT seconds after completion',
    )
    
    parser.add_argument('inputfile', type=Path, help='THE input file')

    return parser.parse_args()


def main():
    args = parseargs()
    MassResolver(args).run()


if __name__ == "__main__":
    main()
