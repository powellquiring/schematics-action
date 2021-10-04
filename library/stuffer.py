#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import env_fallback
import json

module_args = dict(
    msg=dict(
        required=True,
        type='str'),
)

def run_module():

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    #module.log(msg="stuffer-log")
    print('sss')
    module.exit_json(msg=(f"all good stuffer 4 {json.dumps(module.params)}"))

def main():
    run_module()

if __name__ == '__main__':
    main()