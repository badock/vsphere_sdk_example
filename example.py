import sys
import yaml
from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl


def get_entities(credentials, entity_type, names_only=True):
    # Get all the Vms from vCenter server inventory and print its name
    # Below is Python 2.7.x code, which can be easily converted to python 3.x version

    s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    s.verify_mode = ssl.CERT_NONE

    try:
        si = SmartConnect(host=credentials.get("vsphere").get("host"),
                          user=credentials.get("vsphere").get("user"),
                          pwd=credentials.get("vsphere").get("password"),
                          sslContext=s,
                          disableSslCertValidation=True)
    except:
        msg = "I cannot connect to vsphere, please check your credentials in config/config.yaml"
        print(msg)
        raise Exception(msg)
    content = si.content

    # Method that populates objects of type vimtype
    def get_all_objs(content, vimtype):
        obj = {}
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for managed_object_ref in container.view:
            if names_only:
                obj.update({managed_object_ref: managed_object_ref.name})
            else:
                obj.update({managed_object_ref: managed_object_ref})
        return obj

    # Calling above method
    entities = get_all_objs(content, [entity_type])
    return entities


def _main():
    # Fetch config
    with open("config/config.yaml") as f:
        config = yaml.load(f)

    # Print all vms
    vms = get_entities(config, vim.VirtualMachine)
    print("I am printing the names of all vms:")
    for vm in vms:
        print(f" * {vm.name}")

    # Print all hosts and their vms
    hosts = get_entities(config, vim.HostSystem)
    print("I am printing all hosts and their vms:")
    for host in hosts:
        print(f" * {host.name} is a host, and here are its vms:")
        for vm in host.vm:
            print(f"   - {vm.name}")


if __name__== "__main__":
    _main()
    sys.exit(0)
