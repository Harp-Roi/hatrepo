To get project up and running I needed to:
1. Install node & npm
	curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
	sudo apt-get install -y nodejs
2. Install Vue-Cli and templates
	npm install -g @vue/cli
	npm install -g @vue/cli-service-global

###############################################
This approach did not work and I reverted to the old VUE CLI templates
npm install -g @vue/cli-init
vue init webpack my-project
cd my-project
npm install
npm run dev
###############################################

3.

4.

5.



