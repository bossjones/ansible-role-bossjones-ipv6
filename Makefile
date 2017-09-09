mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

cookiecutter-init:
	cookiecutter --output-dir=./ansible-role-bossjones-ipv6 --no-input gh:retr0h/cookiecutter-molecule \
                        full_name="Malcolm Jones" \
                        email="bossjones@theblacktonystark.com" \
                        role_name="bossjones.ipv6" \
                        github_user="bossjones" \
                        repo_name="ansible-role-bossjones-ipv6" \
                        short_description="ansible role to install bossjones ipv6. Only works on fedora 24 currently" \
                        release_date="2017-09-09" \
                        year="2017" \
                        version="0.1.0" \
                        min_ansible_version="2.3.2.0" \
                        allow_duplicates="no" \
                        scenario_name="default" \
                        author="Malcolm Jones" \
                        description="ansible role to install bossjones ipv6. Only works on fedora 24 currently" \
                        company="Tony Dark Labs" \
                        license="Apache"

install-test-deps:
	pip install ansible==2.2.3.0
	pip install docker-py
	pip install molecule --pre

bootstrap-molecule:
	molecule init scenario --role-name $(current_dir) --scenario-name default

ci:
	molecule test

# NOTE: make this into a bash alias (pretty-yaml)
pretty-yaml:
	python -m pyaml /path/to/some/file.yaml
