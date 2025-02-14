# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:39:09 2025

@author: Aaron
"""
import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error details: {str(e)}")
        return False

def install_requirements():
    print("Installing ComfyUI custom nodes and requirements...")

    # Base directory
    base_dir = "/workspace/ComfyUI"
    custom_nodes_dir = os.path.join(base_dir, "custom_nodes")

    # Create custom_nodes directory if it doesn't exist
    os.makedirs(custom_nodes_dir, exist_ok=True)

    # List of repositories to clone
    repos = {
        "ComfyUI-Impact-Pack": "https://github.com/ltdrdata/ComfyUI-Impact-Pack.git",
        "rgthree-comfy": "https://github.com/rgthree/rgthree-comfy.git",
        "ComfyUI_UltimateSDUpscale": "https://github.com/ssitu/ComfyUI_UltimateSDUpscale.git"
    }

    # Clone repositories
    os.chdir(custom_nodes_dir)
    for repo_name, repo_url in repos.items():
        if not os.path.exists(repo_name):
            print(f"Cloning {repo_name}...")
            if not run_command(f"git clone {repo_url}"):
                print(f"Failed to clone {repo_name}")
                continue

    # Install Python packages
    packages = [
        "ultralytics",
        "opencv-python",
        "mediapipe",
        "torch",
        "torchvision",
        "torchaudio",
        "transformers",
        "safetensors"
    ]

    for package in packages:
        print(f"Installing {package}...")
        if not run_command(f"pip install {package}"):
            print(f"Failed to install {package}")

    # Install requirements from custom nodes
    requirement_files = [
        f"{custom_nodes_dir}/ComfyUI-Impact-Pack/requirements.txt",
        f"{custom_nodes_dir}/rgthree-comfy/requirements.txt",
        f"{custom_nodes_dir}/ComfyUI_UltimateSDUpscale/requirements.txt"
    ]

    for req_file in requirement_files:
        if os.path.exists(req_file):
            print(f"Installing requirements from {req_file}...")
            if not run_command(f"pip install -r {req_file}"):
                print(f"Failed to install requirements from {req_file}")

    # Download required models
    models_dir = os.path.join(base_dir, "models/ultralytics")
    os.makedirs(models_dir, exist_ok=True)

    model_url = "https://github.com/ltdrdata/ComfyUI-Impact-Pack/raw/main/models/face_yolov8n.pt"
    model_path = os.path.join(models_dir, "face_yolov8n.pt")

    if not os.path.exists(model_path):
        print("Downloading face detection model...")
        if not run_command(f"wget -P {models_dir} {model_url}"):
            print("Failed to download face detection model")

    # Set permissions
    print("Setting permissions...")
    run_command(f"chmod -R 755 {custom_nodes_dir}")

    print("\nInstallation completed!")
    print("\nPlease restart ComfyUI for changes to take effect.")
    print("Note: If you're using RunPod, remember these changes won't persist unless you save them in a template.")

if __name__ == "__main__":
    install_requirements()

# Created/Modified files during execution:
# /workspace/ComfyUI/custom_nodes/* (multiple directories and files)
# /workspace/ComfyUI/models/ultralytics/face_yolov8n.pt