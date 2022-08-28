# Configure an Nginx server using Puppet to to automatically configure your Nginx server (when you install it) so that /redirect_me is “301 Moved Permanently” to another page by modifying the virtual hosts configuration file: /etc/nginx/sites-enabled/default and show a custom error page when the page is not found, ie: curl IP/bla_bla_bla

package { 'nginx':
}
 
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'redirect permaently 301':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}