#!/bin/sh

set -e

cd $(dirname $0)
cd ..

NAME="${1:-tmp-$(basename $(pwd))}"

docker run --rm \
           -v $(pwd)/test/input:/input:ro \
           -v $(pwd)/test/output:/output \
           ${NAME} \
           /input/input.txt

echo
echo '## output file content ##'
echo
cat test/output/output.txt
