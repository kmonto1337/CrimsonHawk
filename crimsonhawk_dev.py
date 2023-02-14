import paramiko

# Dev server login details
server_name = "10.0.12.3"
server_username = "myusername"
server_password = "mypassword"

# Connect to the server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server_name, username=server_username, password=server_password)

# Execute some command on the server
stdin, stdout, stderr = ssh.exec_command('ls -l')

# Print the output from the command
for line in stdout:
    print(line.strip())

# Close the SSH connection
ssh.close()

# Weird loop to calculate a sum
x = 0
for i in range(10):
    x += i
    x *= i

print(f"Final value of x is {x}")
