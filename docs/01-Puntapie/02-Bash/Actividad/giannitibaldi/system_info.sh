#!/bin/bash

sistema_operativo=$(lsb_release -ds 2>/dev/null || cat /etc/*release 2>/dev/null | head -n1 || uname -om)
kernel=$(uname -r)
cpu=$(lscpu | awk 'NR==8{print $4, $5, $6, $7}')
memoria_total=$(free -m | awk 'NR==2{print $2}')
espacio_disco=$(df -h / | awk 'NR==2{print $2}')
version_bash=$(bash --version | head -n1 | awk '{print $4}')
version_python=$(python3 --version)

json=$(cat <<EOF
{
   'sistema_operativo': '$sistema_operativo',
   'kernel': '$kernel',
   'cpu': '$cpu',
   'memoria_total': '$memoria_total',
   'espacio_disco': '$espacio_disco',
   'version_bash': '$version_bash',
   'version_python': '$version_python'
}
EOF
)

echo "$json"
echo "$json" > system_info.json
