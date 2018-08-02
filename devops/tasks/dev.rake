begin
  require 'tasks/dev/bundler'
rescue LoadError
  puts "Make sure to run 'bundle install' first\n"
  exit 1
end

Tasks::Dev::Bundler.new
