#! /bin/bash

PREVIOUS=4.2
NEXT=5.2

echo "Moving documentation links from $PREVIOUS to $NEXT"

for file in `grep -rl "docs.djangoproject.com/en/$PREVIOUS" * | grep -v pyc | grep -v swp`
do
    if [[ "$file" == *"fixver"* ]]
    then
        echo "Skipping fixver.sh"
        continue
    fi
    rm /tmp/bob
    sed 's"docs.djangoproject.com/en/$PREVIOUS"docs.djangoproject.com/en/$NEXT"g' < $file > /tmp/bob
    echo $file
    cp /tmp/bob $file
done

echo "Checking for even earlier versions of Django document urls..."
grep -r 'docs.djangoproject.com/en/[0-9].[0-9]/' * | grep -v pyc | grep -v swp | grep -v $NEXT


