### Isssue Summary:
----------------------------

##### Duration, Impact and Root cause: 
* 10:00 minutes.10:02 AM - 10:12 AM PST on 5/14/18.
* Users recieved 500 internal server error page when accessing the website.
        100% of the users seeking service during this time were affected.
* Root cause was a typographical error of the file `class-wp-locale.php` as `class-wp-locale.phpp`

##### Timeline (PST):
  10:02 AM - User twitted a 500 server error page to the company.
  
  10:04 AM - On-duty engineer was informed regarding the issue.
  
  10:06 AM - `ps -auxf` command ran to check for running procesess.
  
           -  Apache2 server was found to be running as expected.
           
  10:07 AM - `strace -r -f -p` command with the running process id was ran and the a `curl` was used to request the page.
  
           - The strace report indicated an unexpected error `could not find file class-wp-locale.phpp`
           
  10: 08 AM - 'ls' command on the `/var/www/html/wp-includes/` was used to confirm existence of ` class-wp-locale.php` file.
  
            - The `.phpp` extension was detected as an invalid extension, indicating typographical error in the configuration.
  
  10: 09 AM - `sed -i 's/phpp/php/' /var/www/html/wp-settings.php` command was used to fix the error.
  
  10: 10 AM - The service was tested and confirmed to be running as expected.
  
  10: 11 AM - Puppet manifest developed for large scale deployment.
  
  10: 12 AM - 100% of the servers were confirmed running and serving content correctly.
  
 ##### Root cause and Resolution:
 
 A required file `class-wp-locale.php` in `/var/www/html/wp-settings.php` had been included as `class-wp-locale.phpp` by human error. The typo of the extension `.php` as `.phpp` caused the correct file `.php` to not be recognized and thus not found leading to the 500 server error. A puppet manifest containing the script the fix of this error was developed and deployed to all the servers, resolving the issue and reinstating the service.
 
 ##### Corrective and preventative measures:
 
 The issue indicates issue of code being deployed without tests. Every code should be tested for full-functioning before being deployed to all servers. The issue also points to no test being done to confirm the affect the of code after its deployment in any stage, thus every code change and deployment should be tested to confirm expected output.
