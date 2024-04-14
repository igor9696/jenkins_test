import boto3


def main():
   client  = boto3.client('ec2')

   resp = client.describe_instances()
   print(type(resp))
   print(resp['ResponseMetadata'])


if __name__ == "__main__":
    main()

