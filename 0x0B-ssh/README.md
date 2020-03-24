# 0x0B-SSH

This project is focused on ssh and remote server conections.

### Tasks

#### Task 0

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.

Requirements:

	Only use ssh single-character flags
	You cannot use -l
	You do not need to handle the case of a private key protected by a passphrase


#### Task 1

Write a Bash script that creates an RSA key pair.

Requirements:

	Name of the created private key must be holberton
	Number of bits in the created key to be created 4096
	The created key must be protected by the passphrase betty


#### Task 2

Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

	Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
	Your SSH client configuration must be configured to refuse to authenticate using a password


#### Task 3
Now that you have successfully connected to your server, we would also like to join the party.