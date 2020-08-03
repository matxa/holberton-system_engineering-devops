# Using Puppet, create a manifest that kills a process named

exec {'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
}

