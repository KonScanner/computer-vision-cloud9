#!/usr/bin/env python3

import click
import boto3

@click.command(help="This code detects animals")
@click.option('--bucket', prompt='Insert your own bucket name!',
              help='This is where you insert your own s3 bucket name filled with images to test out')
@click.option('--file', prompt='Insert a file name!',
              help='This is where you type out the name of the file!')
def detect(bucket,file):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': file,
            },
        },
    )

    print(response)

if __name__ == '__main__':
    detect()