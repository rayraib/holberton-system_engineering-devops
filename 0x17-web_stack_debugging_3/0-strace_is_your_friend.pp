# fix class-wp-locale.phpp to class-wp-locale.php
exec { 'change-extensionspelling':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
