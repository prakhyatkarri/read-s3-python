import boto3
from botocore.handlers import disable_signing
from botocore import UNSIGNED
from botocore.config import Config

S3_BUCKET = "genome-browser"
DIRECTORY = "cells/acute-myeloid-leuk/SCPCS000223/metaFields/"

s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

s3_resource = boto3.resource('s3')
s3_resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing) # equivalent to --no-sign-request
bucket = s3_resource.Bucket(S3_BUCKET)
file_names = []

for object in bucket.objects.filter(Prefix=DIRECTORY):
    file_names.append(object.key)


print(f"Available {len(file_names)} files to download")

s3_client.download_file(S3_BUCKET, 'cells/acute-myeloid-leuk/SCPCS000223/metaFields/ExpressedGenes.bin.gz', 'tempfile.bin.gz')