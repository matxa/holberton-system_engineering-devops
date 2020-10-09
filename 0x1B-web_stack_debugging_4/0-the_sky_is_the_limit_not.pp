#Fixing nginx ULIMIT

file { '/etc/default/nginx':
  content => 'ULIMIT="-n 4096"',
}

exec { 'nginx_restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/',
}

