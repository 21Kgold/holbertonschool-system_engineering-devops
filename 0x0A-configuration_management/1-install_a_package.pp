# Install a package using Puppet - flask version 2.1.0 from pip3

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}