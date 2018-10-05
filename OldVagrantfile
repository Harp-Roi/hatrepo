# -*- mode: ruby -*-
# vi: set ft=ruby :

begin
  require 'devops-vagrant'
rescue LoadError
  puts "You need to run (in a directory that isn't this one):"
  puts "vagrant plugin install devops-vagrant --plugin-source https://artifactory.vant.com/artifactory/api/gems/roivant-gems"
  exit 1
end
include Devops::Vagrant

Vagrant.configure("2") do |config|
  set_basebox(config)

  # This defines a default VM. If you only have one VM, you don't need this
  # level of indentation. However, Vagrant can support multiple machines in one
  # definition. For example, a webserver and a database.
  config.vm.define :default do |machine|
    machine.vm.hostname = :somename

    # Uncomment this line if you have multiple machines and want to assign each
    # one a specific IP address.
    #
    # private_network(machine, 10)

    # Uncomment this line if you want to forward a port from your laptop to the
    # VM. This is most useful if you want to point your browser at a webserver
    # running on the VM.
    #
    # machine.vm.network :forwarded_port, guest:80, host: 8080

    provision_chef(machine) do |chef|
      # Add all the roles you want.
      chef.add_role(:hello_world)

      # Add any Vagrant-specific configuration here.
      chef.json = {}
    end
  end
end
