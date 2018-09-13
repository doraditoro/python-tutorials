import boto3
import sys


def create_snapshot():
    ec2_resource = boto3.resource('ec2')
    snapshot = ec2_resource.create_snapshot(VolumeId=sys.argv[1], Description="Taking backup")

create_snapshot()

instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.state)
    for item in instance.volumes.all():
        print item.id

list_volumes()