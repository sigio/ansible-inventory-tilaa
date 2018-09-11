# ansible-inventory-tilaa
Ansible Dynamic Inventory script for Tilaa.com Virtual Machines

This script will talk to the Tilaa.com API to query the configured
virtual machines.  It needs access to the Tilaa API credentials in
the form of the environment-variables

TILAA_USERNAME
TILAA_PASSWORD

At this time it's not 100% conformant to what AWX/Tower expects a
dynamic inventory to do, but it works good enough to provide the hosts
to AWX/Tower and ansible-playbook.

# Installation

Make the tilaa.py script executable and place it in your inventory
directory, or use it directly as your inventory

# Api Access

From the Tilaa api documentation at https://www.tilaa.com/en/api/docs:

  All endpoints require Basic Authentication. For security reasons you
  cannot use your main Tilaa user account to access this API. Instead,
  you should add an API user to your customer account and use the
  specified login credentials to authenticate.
