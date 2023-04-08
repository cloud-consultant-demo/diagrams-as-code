from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC     
from diagrams.aws.compute import EC2               
from diagrams.aws.database import RDS
from diagrams.aws.network import ALB 
from diagrams.aws.network import ClientVpn  
from diagrams.aws.general import Users    
from diagrams.aws.general import InternetAlt2    


web_app_name = "Three tier web application"
with Diagram(web_app_name, show=False):
    clients = Users("Clients")
    internet = InternetAlt2("Internet")
    with Cluster("VPC"):
        ALBFI = ALB("ALB (Facing internet)")
        with Cluster ("Private Subnet"):
            ALBFP = ALB("ALB (Facing Private)")
            with Cluster ("Auto Scaling Group"):
                EC2_Web_Tier = [EC2("Web Tier"), EC2("Web Tier"), EC2("Web Tier")]
            with Cluster ("ASG App Tier"):
                EC2_App_Tier = [EC2("App Tier"), EC2("App Tier"), EC2("App Tier")]
            with Cluster("Database Tier"):
                DB = RDS("RDS")
    
    clients >> internet >> ALBFI >> EC2_Web_Tier >> ALBFP >> EC2_App_Tier >> DB
