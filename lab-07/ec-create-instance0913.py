import boto3


def create_instance():
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(ImageId='ami-0552e3455b9bc8d50',
                MinCount=1, MaxCount=3,InstanceType='t2.micro',
                SecurityGroupIds=['launch-wizard-1'],KeyName='fullstack2')
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance.id)
    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=instance_ids)
    print ("Instance is Running now!")

create_instance()
