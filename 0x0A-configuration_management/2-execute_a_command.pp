# This manifest kills the process 'Killmenow' using the command 'pkill'

exec { 'Killmenow':

    path => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => 'pkill killmenow',
    provider => 'shell',

}