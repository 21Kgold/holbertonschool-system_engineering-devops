# Puppet script to update Per-User soft and hard limits of open files
exec { 'fix_user_hard':
    command  => 'sed -i "s/holberton hard nofile.*/holberton hard nofile 1048576/g" /etc/security/limits.conf',
    provider => shell,
}
exec { 'fix_user_soft':
    command  => 'sed -i "s/holberton soft nofile.*/holberton soft nofile 1048576/g" /etc/security/limits.conf',
    provider => shell,
}