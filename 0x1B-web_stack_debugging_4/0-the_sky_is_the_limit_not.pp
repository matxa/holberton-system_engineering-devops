#Fixing nginx ULIMIT

exec { 'replace_limit':
  command => 'sed -i "/ULIMIT=/c\ULIMIT=\'-n 4096\'" /etc/default/nginx',
  path    => '/usr/bin:/usr/sbin:/bin',
}

exec { 'nginx_restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/',
}

