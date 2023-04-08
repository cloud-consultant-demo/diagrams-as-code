from diagrams import Diagram, Cluster
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.network import Subnets
from diagrams.azure.compute import VM
from diagrams.azure.database import SQLDatabases
from diagrams.azure.network import ApplicationGateway 
from diagrams.azure.network import VirtualNetworkGateways


web_app_name = "Three tier web application"
with Diagram(web_app_name, show=False):
    with Cluster("Virtual Network"):
        ALBFI = ApplicationGateway("ALB (Facing internet)")
        with Cluster ("Private Subnet"):
            ALBFP = ApplicationGateway("ALB (Facing Private)")
            with Cluster ("AutoScale Web Tier"):
                VM_Web_Tier = [VM("Web"), VM("Web"), VM("Web")]
            with Cluster ("AutoScale App Tier"):
                VM_App_Tier = [VM("App"), VM("App"), VM("App")]
            with Cluster("Database Tier"):
                DB = SQLDatabases("Amazon Aurora")
    ALBFI >> VM_Web_Tier >> ALBFP >> VM_App_Tier >> DB