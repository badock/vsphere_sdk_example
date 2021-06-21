# vsphere_sdk_example

## Installation

Install the required libraries via the pip command:
```shell
pip3 install -r requirements.txt
```

## Getting started

### Configure credentials

edit `conf/credentials.conf` and configure how your vsphere may be contacted=

```yaml
vsphere:
  host: 192.168.3.11
  user: administrator@vsphere.local
  password: <Put your password here>
```


### Run the example

run the example via the following command:

```shell
python3 example.py
```

## Use the documentation of the vmware sdk to understand what you can do with the sdk

You can find the documentation here:
https://code.vmware.com/apis/968/vsphere

For example, by clicking on the items on the left `Managed Object Types > HostSystem`,
you can get a description of what capabilities the sdk provides for Hosts:

![https://raw.githubusercontent.com/badock/vsphere_sdk_example/main/images/vmware_sdk1.png](https://raw.githubusercontent.com/badock/vsphere_sdk_example/main/images/vmware_sdk1.png)

We can see that a `HostSystem` object (i.e. a host) provides a vm property that contains a list of `VirtualMachine` (i.e. virtual machines).
![https://raw.githubusercontent.com/badock/vsphere_sdk_example/main/images/vmware_sdk2.png](https://raw.githubusercontent.com/badock/vsphere_sdk_example/main/images/vmware_sdk2.png)

Each object of type `VirtualMachine` is also described in the documentation, and inherits the property `name`:
![https://raw.githubusercontent.com/badock/vsphere_sdk_example/main/images/vmware_sdk3.png](https://raw.githubusercontent.com/badock/vsphere_sdk_example/main/images/vmware_sdk3.png)

Thus, it is perfectly valid to write this code:

```python
hosts = get_entities(config, vim.HostSystem)
for host in hosts:
    for vm in host.vm:
        print(f"   - {vm.name}")
```
