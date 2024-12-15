#!/bin/bash

# Script de configuração e população do banco
echo "---------------------------------------------"
echo "🔧 Script de Configuração e População do Banco"
echo "---------------------------------------------"
echo "1. Popular o banco com alunos"
echo "2. Popular o banco com administradores"
echo "3. Sair"
echo "---------------------------------------------"

read -p "Escolha uma opção (1-3): " opcao

# Função para verificar e configurar o ambiente virtual
configurar_ambiente() {
  echo "🔧 Configurando o ambiente..."

  # Verifica se o Python 3.11 está instalado
  if ! command -v python3.11 &> /dev/null; then
    echo "🚨 Python 3.11 não encontrado. Instalando..."
    sudo apt update
    sudo apt install -y software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install -y python3.11 python3.11-venv python3.11-dev python3.11-distutils python3-pip

    # Configura o Python 3.11 como padrão
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
    sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
  else
    echo "✅ Python 3.11 já está instalado."
  fi

  # Verifica se o módulo venv está instalado
  if ! dpkg -l | grep -q python3-venv; then
    echo "🚨 python3-venv não encontrado. Instalando..."
    sudo apt update
    sudo apt install -y python3-venv
  else
    echo "✅ python3-venv já está instalado."
  fi

  # Criação do ambiente virtual
  if [ ! -d "venv_charge" ]; then
    echo "🔧 Criando ambiente virtual Python 3.11..."
    python3.11 -m venv venv_charge
  fi

  # Ativa o ambiente virtual
  source venv_charge/bin/activate

  # Atualiza o pip e instala dependências
  echo "📦 Instalando dependências..."
  python -m ensurepip --upgrade
  pip install --upgrade pip

  # Verifica se o arquivo requirements.txt existe
  if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Dependências instaladas!"
  else
    echo "❌ Arquivo requirements.txt não encontrado!"
    deactivate
    exit 1
  fi
}

# Verifica a opção escolhida
case $opcao in
  1)
    configurar_ambiente

    # Verificação do arquivo CSV de alunos
    if [ ! -f "charge/data/students.csv" ]; then
      echo "❌ Arquivo CSV não encontrado: charge/data/students.csv"
      deactivate
      exit 1
    fi

    # Executa o script Python para alunos
    echo "🚀 Populando banco com alunos..."
    python -m charge.main_students

    # Desativa o ambiente virtual
    deactivate
    echo "✅ População de alunos concluída!"
    ;;

  2)
    configurar_ambiente

    # Verificação do arquivo CSV de administradores
    if [ ! -f "charge/data/admin.csv" ]; then
      echo "❌ Arquivo CSV não encontrado: charge/data/admin.csv"
      deactivate
      exit 1
    fi

    # Executa o script Python para administradores
    echo "🚀 Populando banco com administradores..."
    python -m charge.main_admins

    # Desativa o ambiente virtual
    deactivate
    echo "✅ População de administradores concluída!"
    ;;

  3)
    echo "Saindo..."
    exit 0
    ;;

  *)
    echo "Opção inválida! Tente novamente."
    ;;
esac
