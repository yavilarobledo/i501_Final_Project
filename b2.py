import boto3

from dotenv import load_dotenv
from pprint import pprint

ENDPOINT_URL='https://s3.us-east-005.backblazeb2.com'

load_dotenv()

client=boto3.client('s3',endpoint_url=ENDPOINT_URL)

response=client.list_buckets()
pprint(response)
