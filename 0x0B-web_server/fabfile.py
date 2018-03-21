from fabric.api import *
#create a tar gzipped archive of the current directory
#+ name of archive is "holbertonwebapp.tar.gz"
#+ placed in the local directory
--tar -czf holbertonwebapp.tar.gz .
# Create a directory (i.e. folder)
run("mkdir /tmp/holbertonwebapp/")
# Upload a tar archive of an application
put("holbertonwebapp.tar.gz", "/tmp/holbertonwebapp/holbertonwebapp.tar.gz")
# Extract the contents of a tar archive
local("tar xzvf /tmp/holbertonwebapp/holbertonwebapp.tar.gz")
# Remove a file
local("rm holbertonwebapp.tar.gz")
