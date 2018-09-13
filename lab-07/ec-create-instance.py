import boto3


def create_instance():
<<<<<<< HEAD
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(ImageId='ami-6871a115)',
=======
    
    ec2_resource = boto3.resource('ec2', region_name='us-east-1')
    
    instances = ec2_resource.create_instances(ImageId='ami-6871a115',
>>>>>>> 814d7a14c70ff1674856c79aea58d06aa664815b
                MinCount=1, MaxCount=3,InstanceType='t2.micro',
                SecurityGroupIds=['launch-wizard-5'],KeyName='fullstack')
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance.id)
    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=instance_ids)
    print ("Instance is Running now!")

create_instance()
