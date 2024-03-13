from promptflow import tool
from promptflow.connections import CustomConnection
from agent_connector.tools.nexus_client import NexusClient

@tool
def call_agent(connection: CustomConnection, input_text: str) -> str:
    client = NexusClient(connection.base_url) 
    agents = [agent["name"] for agent in client.get_agent_names()]
    return ",".join(agents)