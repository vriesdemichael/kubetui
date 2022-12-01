from functools import lru_cache
from typer import Typer
from kubernetes.config import load_kube_config
from kubernetes.client import CoreV1Api



@lru_cache
def get_client() -> CoreV1Api:
    load_kube_config()
    return CoreV1Api()
    


get_typer: Typer = Typer()

@get_typer.command()
def get_pods(namespace: str):
    
    client: CoreV1Api = get_client()
    client.list_pod_for_all_namespaces_with_http_info
    pods: Any = client.api_client.call_api(
        f'/api/v1/namespaces/{namespace}/pods', 'GET')