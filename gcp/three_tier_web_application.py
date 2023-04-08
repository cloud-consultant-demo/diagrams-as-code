from diagrams import Cluster, Diagram
from diagrams.gcp.compute import GCE
from diagrams.gcp.database import SQL
from diagrams.gcp.network import LoadBalancing, VPC
from diagrams.gcp.network import FirewallRules

with Diagram("Arquitectura GCP", show=False):
    with Cluster("Frontend"):
        frontend_instance_group = GCE("Frontend Instance Group")
        frontend_vm = GCE("Frontend VMs") << frontend_instance_group
        frontend_lb = LoadBalancing("HTTP(S) LB") >> frontend_vm

    with Cluster("Backend"):
        backend_instance_group = GCE("Backend Instance Group")
        backend_vm = GCE("Backend VMs") << backend_instance_group
        backend_lb = LoadBalancing("HTTP(S) LB") >> backend_vm

    frontend_vm >> VPC("VPC") >> backend_vm

    with Cluster("Capa de Datos"):
        db = SQL("Cloud SQL")

    backend_vm >> db

    frontend_lb << FirewallRules("Firewall Rules")
    backend_lb << FirewallRules("Firewall Rules")
