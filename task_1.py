import subprocess


subprocess.run(["python", "-m", "venv", "myenv"])


subprocess.run(["myenv\\Scripts\\activate"], shell=True)


subprocess.run(["pip", "install", "python-docx"])


subprocess.run(["deactivate"], shell=True)