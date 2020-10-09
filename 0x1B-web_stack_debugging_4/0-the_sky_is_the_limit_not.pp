#Fixing nginx ULIMIT

exec { 'replace_limit':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i "/ULIMIT=/c\ULIMIT=\'-n 4096\'" /etc/default/nginx',
}

exec { 'nginx_restart':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sudo service nginx restart',
}

