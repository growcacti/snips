import os
import subprocess


def reformat_code(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                subprocess.run(["python", "-m", "black", filepath])
                if result.returncode == 0:
                    print(f"Successfully formatted: {filepath}")
                    print(stdout)
                else:
                    print(f"Error occurred while formatting: {filepath}")
                    print(result.stderr)


# Usage
reformat_code("/home/jh/Desktop/newOOPwidgets/*.py")
