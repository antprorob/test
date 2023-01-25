
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

from pprint import pprint 
# pprint(access_template)

vlan = input ("Введите номер vlan: ")
intf = input ("Введите номер интерфейса: ")
input ("Нажимте любую клавишу для продложения")
print(f"interface {intf}")
access_str = "\n".join(access_template)
# pprint(access_str)
print(access_str.format(vlan))
