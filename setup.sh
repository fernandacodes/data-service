#!/bin/bash

# Nome do ambiente virtual
VENV_DIR="venv_charge"

# Caminho dos arquivos CSV
STUDENT_CSV_PATH="/code/charge/data/students.csv"
ADMIN_CSV_PATH="/code/charge/data/admin.csv"

# Função para criar o ambiente virtual e instalar dependências
create_virtual_env() {
  # Verifica se o ambiente virtual já existe
  if [ ! -d "$VENV_DIR" ]; then
    echo "🔧 Criando ambiente virtual Python..."
    python3 -m venv "$VENV_DIR"
    echo "✅ Ambiente virtual criado!"
  else
    echo "ℹ️ Ambiente virtual já existe."
  fi

  # Ativa o ambiente virtual
  source "$VENV_DIR/bin/activate"

  # Instala dependências
  echo "📦 Instalando dependências..."
  pip install --upgrade pip
  pip install -r requirements.txt
  echo "✅ Dependências instaladas!"
}

# Função para popular o banco de dados
populate_database() {
  local role=$1
  local csv_path=$2

  # Verifica se o arquivo CSV existe
  if [ ! -f "$csv_path" ]; then
    echo "❌ Arquivo CSV não encontrado: $csv_path"
    exit 1
  fi

  echo "🚀 Populando o banco com $role..."
  python charge_script.py --role "$role" --csv "$csv_path"
}

# Menu de opções
echo "---------------------------------------------"
echo "🔧 Script de Configuração e População do Banco"
echo "---------------------------------------------"
echo "1. Popular o banco com alunos"
echo "2. Popular o banco com administradores"
echo "3. Sair"
echo "---------------------------------------------"
read -p "Escolha uma opção (1-3): " option

# Executa a ação com base na escolha do usuário
case $option in
  1)
    create_virtual_env
    populate_database "student" "$STUDENT_CSV_PATH"
    ;;
  2)
    create_virtual_env
    populate_database "admin" "$ADMIN_CSV_PATH"
    ;;
  3)
    echo "👋 Saindo..."
    exit 0
    ;;
  *)
    echo "❌ Opção inválida. Tente novamente."
    ;;
esac
