# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:03:34 2025

@author: Aaron

Claud:
    
In SSH:
    
find / -name relauncher.py 2>/dev/null

cat /path/to/webui/relauncher.py

here:
cat /workspace/stable-diffusion-webui/relauncher.py
 
copy paset to file here

wget https://raw.githubusercontent.com/Akehorn/ComfyUIReq/refs/heads/main/relauncher.py -O /workspace/stable-diffusion-webui/relauncher.py


chmod 644 /path/to/existing/relauncher.py

chmod 644 /workspace/stable-diffusion-webui/relauncher.py
"""
import os
import time


def relaunch_process(launch_counter=0):
    '''

    '''
    while True:
        print('Relauncher: Launching...')
        if launch_counter > 0:
            print(f'\tRelaunch count: {launch_counter}')

        try:
            # launch_string = "/workspace/stable-diffusion-webui/webui.sh -f"
            # launch_string = "/workspace/stable-diffusion-webui/webui.sh -f --xformers --api --enable-insecure-extension-access --no-half-vae"
            launch_string = "/workspace/stable-diffusion-webui/webui.sh -f --xformers --api --controlnet-allow-ip-adapter"
            os.system(launch_string)
        except Exception as err:
            print(f"An error occurred: {err}")
        finally:
            print('Relauncher: Process is ending. Relaunching in 2s...')
            launch_counter += 1
            time.sleep(2)


if __name__ == "__main__":
    relaunch_process()
