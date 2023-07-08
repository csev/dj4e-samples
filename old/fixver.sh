#! /bin/bash

for file in `grep -rl 'docs.djangoproject.com/en/3.0' * | grep -v pyc | grep -v swp`
do
    if [[ "$file" == *"fixver"* ]]
    then
        echo "Skipping fixver.sh"
        continue
    fi
    rm /tmp/bob
    sed 's"docs.djangoproject.com/en/3.0"docs.djangoproject.com/en/4.2"g' < $file > /tmp/bob
    echo $file
    cp /tmp/bob $file
done
