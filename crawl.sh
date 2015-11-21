#!/bin/bash
set -e
spiders=(fox reuters)
for spider in ${spiders[@]}; do
  # Scrapy appends results.
  echo Running spider $spider
  rm -f ${spider}.csv || true
  scrapy crawl $spider -o ${spider}.csv -t csv 2>> log.txt
done
