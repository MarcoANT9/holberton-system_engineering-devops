# This manifest kills the process 'Killmenow'

exec { 'Killmenow':

    path => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => 'pkill killmenow',
    provider => 'shell',

}