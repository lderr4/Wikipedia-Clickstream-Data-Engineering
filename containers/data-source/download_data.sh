#!/bin/bash

# Define the URL and output file name
URL="https://dumps.wikimedia.org/other/clickstream/2024-10/clickstream-nlwiki-2024-10.tsv.gz"
OUTPUT_FILE="/app/data/clickstream-nlwiki-2024-10.tsv.gz"

echo "Downloading $URL..."
curl -o $OUTPUT_FILE $URL

if [[ -f $OUTPUT_FILE ]]; then
    echo "Download complete: $OUTPUT_FILE"
    
    echo "Unzipping $OUTPUT_FILE..."
    gunzip -f $OUTPUT_FILE

    if [[ -f "${OUTPUT_FILE%.gz}" ]]; then
        echo "File unzipped successfully: ${OUTPUT_FILE%.gz}"
    else
        echo "Error: Failed to unzip $OUTPUT_FILE"
        exit 1
    fi
else
    echo "Error: Failed to download $URL"
    exit 1
fi
