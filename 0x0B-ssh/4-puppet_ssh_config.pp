# 4. Client configuration file (w/ Puppet)

file {'/home/vagrant/.ssh/config':
    ensure  => 'present',
    path    => '/home/vagrant/.ssh/config',
    content => 'Host ubuntu
  IdentityFile ~/.ssh/holberton',
}

exec {'touch /home/vagrant/.ssh/config':
    command => '/usr/bin/touch /home/vagrant/.ssh/config',
    before  => File['/home/vagrant/.ssh/config'],
}
