#!/bin/bash

# Descargar los archivos de fail2ban
echo "Descargando fail2ban.deb..."
wget -O fail2ban.deb https://github.com/fail2ban/fail2ban/releases/download/1.1.0/fail2ban_1.1.0-1.upstream1_all.deb

echo "Descargando fail2ban.deb.asc..."
wget -O fail2ban.deb.asc https://github.com/fail2ban/fail2ban/releases/download/1.1.0/fail2ban_1.1.0-1.upstream1_all.deb.asc

# Instalar fail2ban
echo "Instalando fail2ban..."
sudo dpkg -i fail2ban.deb

# Instalar dependencias faltantes
echo "Instalando dependencias faltantes..."
sudo apt -f install -y

# Iniciar el servicio fail2ban
echo "Iniciando el servicio fail2ban..."
sudo systemctl start fail2ban

# Habilitar el servicio fail2ban para que se inicie automáticamente al arrancar el sistema
echo "Habilitando el servicio fail2ban para que se inicie automáticamente al arrancar el sistema..."
sudo systemctl enable fail2ban

echo "Instalación y configuración de fail2ban completada."
