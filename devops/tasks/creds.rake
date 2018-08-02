begin
  require 'tasks/creds/aws'
rescue LoadError
  puts "Make sure to run 'bundle install' first\n"
  exit 1
end

Tasks::Creds::AWS.new
