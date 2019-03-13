import paramiko

p_key = paramiko.RSAKey.from_private_key_file("/Users/secuof/ssh/auth.pem")
con = paramiko.SSHClient()
con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
con.connect(hostname = "52.78.93.195", username = "ubuntu", pkey = p_key)
print("connected")

commands = ["ls -al", "ls -alh"]
command = "df -h"

print("Executing {$",command,"}")
# stdin , stdout, stderr = con.exec_command(command)
# print(stdout.readlines())
# print("Errors")
# print(stderr.readlines())

for command in commands:
	print("Executing {$", f"{command}", "}")
	stdin , stdout, stderr = con.exec_command(command)
	print(stdout.read())
	print("Errors")
	print(stderr.read())

# stdin , stdout, stderr = con.exec_command(command)
# print(stdout.read())

con.close()