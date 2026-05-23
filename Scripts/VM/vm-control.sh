#!/bin/bash

case "$1" in
  list)
    ssh epyc "virsh list --all"
    ;;
  start)
    ssh epyc "virsh start $2"
    ;;
  stop)
    ssh epyc "virsh shutdown $2"
    ;;
  force-stop)
    ssh epyc "virsh destroy $2"
    ;;
  reboot)
    ssh epyc "virsh reboot $2"
    ;;
  vnc)
    ssh epyc "virsh vncdisplay $2"
    ;;
  *)
    echo "BBB VM Control"
    echo ""
    echo "Usage:"
    echo "  vm-control list"
    echo "  vm-control start VMNAME"
    echo "  vm-control stop VMNAME"
    echo "  vm-control force-stop VMNAME"
    echo "  vm-control reboot VMNAME"
    echo "  vm-control vnc VMNAME"
    ;;
esac
