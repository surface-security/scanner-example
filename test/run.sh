#!/bin/sh

set -e

cd $(dirname $0)
cd ..

./build.sh nopush

if [ -e '.git' ]; then
    NAME=$(basename $(cat .git/config| grep '/scanners/' | tr -d ' ') | sed -e 's/\.git$//g')
else
    # fingers crossed name is the same as repo
    NAME=$(basename $(pwd))
fi

docker run --rm \
           -v $(pwd)/test/input:/input:ro \
           -v $(pwd)/test/output:/output \
           test/${NAME}:dev \
           /input/input.txt

echo
echo '## output file content ##'
echo
cat test/output/output.txt
