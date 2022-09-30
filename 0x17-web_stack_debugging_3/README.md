Puppet manifest to fix a typo at the code of a web server. To find the bug:
- Run the curl -sI 127.0.0.1 command at the web server where the Wordpress code is running. The curl command is used to transfer data to or from a server, the -I option is used to Fetch the headers only and the -s option is used as silent option. the 127.0.0.1 is the IP of the localhost (the server we are workin on)

- By running the curl command we receive a 500 error, which is a server error.

- Then we run the ps auxf to find the process that are asociated with the apache server

- By runnig strace -p <proces_number> we are able to see the sys calls and find the bug