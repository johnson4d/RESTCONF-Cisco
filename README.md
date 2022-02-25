# RESTCONF-Cisco

This python script will retrieve the Cisco router clock and ARP cache every 10 seconds, via RESTCONF (using the Cisco YANG interface). Once run, the Python script will ask for the login credentials of the Cisco router (username/password) as well as its IP address.

Here is an example.

Username?yang

Password?yang

IP Address?192.168.0.239

{
  "Cisco-IOS-XE-device-hardware-oper:current-time": "2022-02-25T05:04:15+00:00"
}

{
  "Cisco-IOS-XE-arp-oper:arp-data": {
    "arp-vrf": [
      {
        "vrf": "Default",
        "arp-oper": [
          {
            "address": "192.168.0.1",
            "enctype": "ios-encaps-type-arpa",
            "interface": "GigabitEthernet1",
            "type": "ios-linktype-ip",
            "mode": "ios-arp-mode-dynamic",
            "hwtype": "ios-snpa-type-ieee48",
            "hardware": "bc:30:d9:d3:91:46",
            "time": "2022-02-25T05:01:45.000419+00:00"
          },
