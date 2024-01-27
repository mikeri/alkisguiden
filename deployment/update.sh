#!/bin/bash
# Run this from project root
ANSIBLE_STDOUT_CALLBACK=yaml ansible-playbook -i deployment/production deployment/deploy.yml
