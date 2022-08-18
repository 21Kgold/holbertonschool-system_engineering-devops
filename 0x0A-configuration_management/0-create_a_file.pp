# Create a puppet manifest - Puppet + Ruby programming language + .pp extension

file { '/tmp/school':
    ensure  => 'file',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}