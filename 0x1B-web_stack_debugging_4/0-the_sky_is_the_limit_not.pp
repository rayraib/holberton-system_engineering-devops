# update the worker limit to suppress too many file open error msg 
exec { 'update ulimit':
  command => "sed -i '5s/.*/ULIMIT=\"-n 3000\"/' /etc/default/nginx && sudo service nginx restart",
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
