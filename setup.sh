#!/bin/bash

aws s3 cp main.nf s3://fh-nextflow-script-bucket/hello/
aws s3 cp nextflow.config s3://fh-nextflow-script-bucket/hello/
