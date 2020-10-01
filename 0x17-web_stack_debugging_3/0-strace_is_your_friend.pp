exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

package { 'apache2':
  ensure  => installed,
  require => Exec['apt-update'],
}

service { 'apache2':
  ensure => running,
}

exec { '/var/www/html/wp-setting.php':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
