#! /bin/bash

for file in `grep -rl 'docs.djangoproject.com/en/4.2' * | grep -v pyc | grep -v swp`
do
    rm /tmp/bob
    sed 's"docs.djangoproject.com/en/4.2"docs.djangoproject.com/en/4.2"g' < $file > /tmp/bob
    echo $file
    cp /tmp/bob $file
done
