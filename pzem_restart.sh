#!/bin/bash
# only restart service if server is available
if ping -c 1 mqtt.centanniventures.comx ; then
	systemctl restart pzem_monitor.service
fi
