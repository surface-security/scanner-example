# Boilerplate

Template scanner to speed up creating new ones

The only thing scanners need to follow is:
* process a single input file that will be specified as first positional argument
* produce as many output files as wanted in `/output` path (inside the container)

Input file format will match whatever is chosen as `Input Generator` and the output produced should match whatever is expected by `Output Parser` <-- settings defined in the scanner configuration in Surface)


This repository is actually built as a scanner (named `example`) that can be used to test scanners framework or a new rootbox.

## NOTE

This is a dumb scanner as it only resolves A records and it shells out to `host` utility. This has a performance impact (spawning shells) over simply using a DNS lib/package but the purpose is to exemplify the common scenario of building entrypoints to *wrap* external/3rd-party scanners


Rest of README.md is also part of the example, feel free to re-use

# Example Scanner in Docker

This scanner performs DNS resolution.

Input expected: one hostname per line
Output provided: single file, with `hostname:IP`

## Usage

```
Mass DNS Resolver

positional arguments:
  inputfile             THE input file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output directory for results
  -p PROCESSES, --processes PROCESSES
                        number of processes
  --echo                just echo input back instead of resolving DNS (passive
                        testing)
  --wait WAIT           sleep WAIT seconds after completion
```

`echo` will just echo back so it can be executed without hammering nameservers (if not required).

`wait` will introduce sleep at the end which can be useful to easily simulate a long scan.

## Run locally
- Build: `./build.sh nopush`
- Create `/tmp/input/input.txt` and `/tmp/output`.
- Run: `docker run --rm -v /tmp/input:/input -v /tmp/output:/output ${PWD##*/}:latest`
