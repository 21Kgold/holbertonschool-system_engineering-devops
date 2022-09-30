# Puppet manifests that fix all occurrences of a typo in a Wordpress website code, by running it at the web server from the command line
exec { 'fix_wordpresss': # exec resource named 'fix_wordpresss'
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php', # Wordpress configuration file
    provider => shell,
}