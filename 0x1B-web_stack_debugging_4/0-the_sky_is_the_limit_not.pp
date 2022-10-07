# Update nginx open files limit from 15 to 2000 to be able to  make 2000 requests
exec { 'update_nginx_open_files_limit':
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
  provider => shell,
}

exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => shell,
  require  => Exec['update_nginx_open_files_limit'],
}