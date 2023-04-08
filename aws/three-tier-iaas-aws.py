from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC
from diagrams.aws.network import PublicSubnet
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.compute import EC2
from diagrams.aws.database import Aurora
from diagrams.aws.network import ALB 
from diagrams.aws.network import ClientVpn


with Diagram("Three tier web application", show=False):
    with Cluster("VPC"):
        ALBFI = ALB("ALB (Facing internet)")
        with Cluster ("Private Subnet"):
            with Cluster ("ASG Web Tier"):
                EC2_Web_Tier = EC2("Web Tier")
            ALBFP = ALB("ALB (Facing Private)")
            with Cluster ("ASG App Tier"):
                EC2_App_Tier = EC2("App Tier")
            with Cluster("Database Tier"):
                DB = Aurora("Amazon Aurora")
            