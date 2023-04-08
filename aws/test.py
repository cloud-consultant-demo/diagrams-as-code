from diagrams import Diagram, Cluster
from diagrams.aws.database import Aurora
from diagrams.aws.database import ElastiCache
from diagrams.aws.network import ALB
from diagrams.aws.network import CloudFront
from diagrams.aws.network import VPC
from diagrams.aws.storage import S3
from diagrams.aws.compute import EC2

with Diagram("DSO-1224", show=False, direction="TB"):
    with Cluster("VPC"):
        EC2 = EC2("Seth") 
        with Cluster ("DB"):
            DB = Aurora("Aurora PostgreSQL")
            Cache = ElastiCache("broadstream-dev")

                
    EC2 >> DB 
    EC2 >> Cache
     