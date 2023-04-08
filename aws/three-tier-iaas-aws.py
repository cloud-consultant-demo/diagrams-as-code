from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC
from diagrams.aws.network import PublicSubnet
from diagrams.aws.network import PrivateSubnet           
from diagrams.aws.compute import EC2               
from diagrams.aws.database import Aurora
from diagrams.aws.network import ALB 
from diagrams.aws.network import ClientVpn          


web_app_name = "Three tier web application"
with Diagram(web_app_name, show=False):
    with Cluster("VPC"):
        VPC_Global = VPC("VPC")
        ALBFI = ALB("ALB (Facing internet)")
        with Cluster ("Private Subnet"):
            ALBFP = ALB("ALB (Facing Private)")
            with Cluster ("Auto Scaling Group"):
                EC2_Web_Tier = [EC2("Web Tier"), EC2("Web Tier"), EC2("Web Tier")]
            with Cluster ("ASG App Tier"):
                EC2_App_Tier = [EC2("App Tier"), EC2("App Tier"), EC2("App Tier")]
            with Cluster("Database Tier"):
                DB = Aurora("Amazon Aurora")
    ALBFI >> EC2_Web_Tier >> ALBFP >> EC2_App_Tier >> DB
