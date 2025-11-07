"""
Arquivo principal para executar a biblioteca EduChain
"""

# from demos import BlockchainDemo


from demos import BlockchainDemo


def print_header():
    """Imprime cabeçalho da aplicação."""
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║              📚 EDUCHAIN - BIBLIOTECA EDUCACIONAL              ║
    ║                  Aprenda Blockchain na Prática                ║
    ║                         Versão 1.0.0                           ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)


def print_menu():
    """Imprime menu de opções."""
    print("\n" + "="*70)
    print("MENU DE DEMONSTRAÇÕES".center(70))
    print("="*70)
    print("1. Blockchain Básica")
    print("2. Detecção de Adulteração")
    print("3. Sistema de Transações")
    print("4. Mineração Concorrente")
    print("5. Fundamentos de Criptografia")
    print("6. Executar Todas as Demos")
    print("0. Sair")
    print("="*70)


def main():
    """Função principal do programa."""
    print_header()
    
    while True:
        print_menu()
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == '1':
            BlockchainDemo.demo_basic_blockchain()
        elif choice == '2':
            BlockchainDemo.demo_tampering_detection()
        elif choice == '3':
            BlockchainDemo.demo_transactions()
        elif choice == '4':
            BlockchainDemo.demo_concurrent_mining()
        elif choice == '5':
            BlockchainDemo.demo_crypto_basics()
        elif choice == '6':
            print("\n🚀 Executando todas as demonstrações...\n")
            BlockchainDemo.demo_crypto_basics()
            BlockchainDemo.demo_basic_blockchain()
            BlockchainDemo.demo_tampering_detection()
            BlockchainDemo.demo_transactions()
            BlockchainDemo.demo_concurrent_mining()
            print("\n✅ Todas as demonstrações concluídas!")
        elif choice == '0':
            print("\n👋 Obrigado por usar EduChain! Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")
        
        input("\n⏸️  Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()