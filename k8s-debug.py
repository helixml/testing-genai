import subprocess
import requests
import json
import os

def get_pod_logs(pod_name):
    try:
        # Get last 10 lines of logs for the pod
        logs = subprocess.check_output(
            ['kubectl', 'logs', '--tail=10', pod_name],
            stderr=subprocess.PIPE
        ).decode('utf-8')
        return logs
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"

# Get kubectl output and pod logs
try:
    # Get pod list
    kubectl_output = subprocess.check_output(['kubectl', 'get', 'po']).decode('utf-8')
    
    # Get pod names and statuses
    pod_lines = kubectl_output.splitlines()[1:]  # Skip header line
    pods = [line.split() for line in pod_lines]
    
    # Build the message with structured information about each pod
    message = "Here's the current state of the Kubernetes cluster:\n\n"
    message += "Pod List:\n```\n" + kubectl_output + "```\n\n"
    message += "Detailed pod logs:\n\n"
    
    for pod_info in pods:
        pod_name = pod_info[0]
        pod_status = pod_info[2]  # STATUS column
        
        message += f"Pod: {pod_name} (Status: {pod_status})\n"
        logs = get_pod_logs(pod_name)
        message += f"Last 10 log lines:\n```\n{logs}```\n\n"
    
except subprocess.CalledProcessError as e:
    print(f"Error running kubectl: {e}")
    exit(1)

# API configuration
HELIX_URL = os.getenv("HELIX_URL")
HELIX_API_KEY = os.getenv("HELIX_API_KEY")
APP_ID = os.getenv("APP_ID", "app_01jenr1cghg6mz2qxr03dsy22k")

# Prepare request payload
payload = {
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    "app_id": APP_ID,
    "session_id": "",
    "messages": [
        {
            "role": "user",
            "content": {"content_type": "text", "parts": [message]}
        }
    ]
}

# Make API request
try:
    response = requests.post(
        f"{HELIX_URL}/api/v1/sessions/chat",
        headers={
            "Authorization": f"Bearer {HELIX_API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )
    response.raise_for_status()
    session_id = response.json()["id"]
    
    # Print the session URL
    print(f"{HELIX_URL}/session/{session_id}")

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
    exit(1)