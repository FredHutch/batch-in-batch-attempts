#!/usr/bin/env python3
import boto3 
import os
import random
import string

def lambda_handler(event,context):

    # Todo: Extract Job Params From Manifest.JSON trigger
    nextflowScript = 's3://fh-nextflow-script-bucket/hello'        
    # Specify Job Queue
    jobqueue = 'default-ff617610-e498-11e9-b92c-06a318773a24'
    jobdef = 'nextflow'
    # Create unique name for the job (this does not need to be unique)
    jobName = 'job' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    # Set up a batch client
    session = boto3.session.Session()
    client = session.client('batch')
    # Submit the job
    job = client.submit_job(
    jobName=jobName, jobQueue=jobqueue, jobDefinition=jobdef, parameters={
        'NextflowScript': nextflowScript
    },
    )
    print("Started Job: {}".format(job['jobName']))

if __name__ == "__main__":
    lambda_handler(None, None)
