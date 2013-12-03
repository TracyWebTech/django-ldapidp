# update the packages on the system
exec { "apt-get update":
  path => "/usr/bin",
}

# Bootstrap ldap
node default {
  class { 'ldap':
    server      => true,
    ssl         => false,
  }
}
ldap::define::domain {'puppetlabs.test':
  basedn   => 'dc=puppetlabs,dc=test',
  rootdn   => 'cn=admin',
  rootpw   => 'test',
  auth_who => 'anonymous'
}

# req to install python pkgs
package { 'python-pip':
  ensure => installed,
}

# req to create virtualenvs
package { 'virtualenvwrapper':
  ensure   => installed,
  provider => pip,
  require  => Package['python-pip'],
}

# req for any compilation
package { 'build-essential':
  ensure => installed,
}

# req for compiling every python pkg
package { 'python-dev':
  ensure => installed,
}

# req for compiling python-ldap
package { 'libldap2-dev':
  ensure => installed,
}

# req for compiling python-ldap
package { 'libsasl2-dev':
  ensure => installed,
}

# req for cloning code
package { 'git':
  ensure => installed,
}

package { 'mercurial':
  ensure => installed,
}
