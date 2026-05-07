#!/bin/bash

echo "[*] A resetar configurações anteriores..."
sudo ufw --force reset

echo "[*] Definindo política: Bloquear tudo por defeito (Inbound)..."
sudo ufw default deny incoming
sudo ufw default allow outgoing

echo "[*] A permitir serviços essenciais..."
# Permitir SSH (Porta 22) - Essencial para gestão remota
sudo ufw allow 22/tcp
#Permitir HTTP (Porta 80) e HTTPS (Porta 443)
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

echo "[*] A ativar a Firewall..."
sudo ufw --force enable

echo "[*] Estado atual da Firewall:"
sudo ufw status verbose
