import subprocess

process = subprocess.Popen(["echo","here"],stdout=subprocess.PIPE)
process_2 =subprocess.Popen(["cat","-"],stdin=process.stdout)

assert process.wait()==0 and process_2.wait()==0