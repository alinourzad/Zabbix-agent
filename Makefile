.PHONY: run

run:
	ansible-playbook -i hosts.yml -K ansible-playbook.yml
	python run.py
