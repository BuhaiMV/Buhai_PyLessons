import subprocess

result = subprocess.run(['python', 'threads_example.py'], shell=True, capture_output=True, text=True)
print(result.stdout)
