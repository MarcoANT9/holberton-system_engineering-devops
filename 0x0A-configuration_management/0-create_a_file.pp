# This program creates a new file with the characteristics:
#    File path is /tmp/holberton
#    File permission is 0744
#    File owner is www-data
#    File group is www-data
#    File contains I love Puppet

file { '/tmp/holberton':
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}