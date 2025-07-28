#!/usr/bin/env python3
"""
Script de execução simplificado para o projeto BI Call Center
"""

import subprocess
import sys
import os

def run_data_generation():
    """Executa a geração de dados fictícios"""
    print("🔄 Gerando dados fictícios...")
    try:
        subprocess.run([sys.executable, "src/generate_data.py"], check=True)
        print("✅ Dados gerados com sucesso!")
    except subprocess.CalledProcessError:
        print("❌ Erro ao gerar dados")
        return False
    return True

def run_dashboard():
    """Executa o dashboard Streamlit"""
    print("🚀 Iniciando dashboard...")
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "app/dashboard.py", 
            "--server.port", "8501",
            "--server.address", "0.0.0.0"
        ], check=True)
    except subprocess.CalledProcessError:
        print("❌ Erro ao iniciar dashboard")
        return False
    except KeyboardInterrupt:
        print("\n👋 Dashboard encerrado pelo usuário")
    return True

def main():
    """Função principal"""
    print("📞 BI Call Center - Projeto Didático")
    print("=" * 40)
    
    # Verificar se os dados existem
    if not os.path.exists("data/call_center_data.csv"):
        print("📊 Dados não encontrados. Gerando dados fictícios...")
        if not run_data_generation():
            return
    else:
        print("📊 Dados encontrados!")
    
    print("\n🎯 Iniciando dashboard interativo...")
    print("📱 Acesse: http://localhost:8501")
    print("🛑 Pressione Ctrl+C para encerrar")
    print("-" * 40)
    
    run_dashboard()

if __name__ == "__main__":
    main()

