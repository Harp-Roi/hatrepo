begin
  require 'tasks/git'
rescue LoadError
  puts "Make sure to run 'bundle install' first\n"
  exit 1
end

Tasks::Git::Tasks.new
