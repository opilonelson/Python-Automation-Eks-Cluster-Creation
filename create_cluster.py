import boto3

eks_client = boto3.client('eks')
#replace name with the desired cluster name
#replace the subnet ids with actual subnet ids from the vpc where the cluster is to be created
#replace the security group with actual security group in the relevant vpc 
response=eks_client.create_cluster(name='nellz-demo-cluster', roleArn='arn:aws:iam::987654321098:role/eks-cluster-role', resourcesVpcConfig={'subnetIds':['subnet-4567de56', 'sg-6587jh42'], 'securityGroupIds':['sg-1234fe89'])
print(response['cluster']['status'])





