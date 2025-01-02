#!/bin/bash

# Define the URL and output file name
URL="https://dumps.wikimedia.org/other/clickstream/2024-10/clickstream-enwiki-2024-10.tsv.gz"
OUTPUT_FILE="src/data-source/data/clickstream-enwiki-2024-10.tsv.gz"
OUTPUT_FILE_SAMPLE="src/data-source/data/clickstream-enwiki-2024-10_sample.csv"

mkdir -p src/data-source/data

if [[ -f $OUTPUT_FILE_SAMPLE ]]; then
    echo "$OUTPUT_FILE_SAMPLE already generated. Exiting download script."
    exit 0
fi
 

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

echo "Generating data sample..."
python src/data-source/load_data.py

rm "${OUTPUT_FILE%.gz}"

if [[ -f $OUTPUT_FILE_SAMPLE ]]; then
    echo "Sample generated. Exiting script"
    exit 0
else
    echo "An error occurred generating the sample."
    exit 1
fi
        