"""
Módulo de Demonstrações Educacionais
Exemplos práticos de uso da biblioteca
"""

# from blockchain import Blockchain
# from block import Block
# from transaction import Transaction
# from crypto_utils import CryptoUtils
# from miner import ConcurrentMiner


from block import Block
from blockchain import Blockchain
from crypto_utils import CryptoUtils
from miner import ConcurrentMiner
from transaction import Transaction


class BlockchainDemo:
    """
    Classe com demonstrações educacionais dos conceitos de blockchain.
    """
    
    @staticmethod
    def demo_basic_blockchain():
        """Demonstração básica: criar blockchain e adicionar blocos."""
        print("\n" + "="*70)
        print("DEMO 1: Blockchain Básica".center(70))
        print("="*70)
        
        # Cria blockchain
        bc = Blockchain(difficulty=3)
        
        # Adiciona blocos
        print("\n📝 Adicionando blocos...")
        bc.add_block(Block(1, '01/01/2024 10:00', 'Transação: Alice -> Bob 50 moedas'))
        bc.add_block(Block(2, '01/01/2024 11:00', 'Transação: Bob -> Carol 30 moedas'))
        
        # Valida
        bc.is_chain_valid()
        
        # Exibe
        bc.print_chain()
    
    @staticmethod
    def demo_tampering_detection():
        """Demonstração: detecção de adulteração."""
        print("\n" + "="*70)
        print("DEMO 2: Detecção de Adulteração".center(70))
        print("="*70)
        
        bc = Blockchain(difficulty=2)
        bc.add_block(Block(1, '01/01/2024', 'Dados originais'))
        
        print("\n✓ Blockchain válida inicialmente:")
        bc.is_chain_valid()
        
        print("\n🔨 Adulterando dados do bloco 1...")
        bc.chain[1].data = 'Dados adulterados!'
        
        print("\n❌ Verificando blockchain após adulteração:")
        bc.is_chain_valid()
        
        print("\n💡 Conclusão: A adulteração foi detectada!")
        print("   O hash armazenado não corresponde ao hash calculado.")
    
    @staticmethod
    def demo_transactions():
        """Demonstração: sistema de transações."""
        print("\n" + "="*70)
        print("DEMO 3: Sistema de Transações".center(70))
        print("="*70)
        
        bc = Blockchain(difficulty=2)
        
        # Adiciona transações
        print("\n📝 Adicionando transações...")
        bc.add_transaction(Transaction("Alice", "Bob", 50))
        bc.add_transaction(Transaction("Bob", "Carol", 30))
        
        print("\n⛏️  Minerando bloco 1...")
        bc.mine_pending_transactions("Miner1")
        
        # Mais transações
        print("\n📝 Adicionando mais transações...")
        bc.add_transaction(Transaction("Carol", "Alice", 20))
        print("\n⛏️  Minerando bloco 2...")
        bc.mine_pending_transactions("Miner2")
        
        # Verifica saldos
        print("\n" + "="*70)
        print("SALDOS FINAIS".center(70))
        print("="*70)
        print(f"💰 Saldo Alice: {bc.get_balance('Alice')} moedas")
        print(f"💰 Saldo Bob: {bc.get_balance('Bob')} moedas")
        print(f"💰 Saldo Carol: {bc.get_balance('Carol')} moedas")
        print(f"💰 Saldo Miner1: {bc.get_balance('Miner1')} moedas")
        print(f"💰 Saldo Miner2: {bc.get_balance('Miner2')} moedas")
    
    @staticmethod
    def demo_concurrent_mining():
        """Demonstração: mineração concorrente."""
        print("\n" + "="*70)
        print("DEMO 4: Mineração Concorrente".center(70))
        print("="*70)
        
        # Cria bloco para minerar
        test_block = Block(1, '01/01/2024', 'Teste de mineração concorrente')
        
        # Benchmark com diferentes números de threads
        ConcurrentMiner.benchmark_mining(test_block, difficulty=4, max_threads=8)
    
    @staticmethod
    def demo_crypto_basics():
        """Demonstração: fundamentos de criptografia."""
        print("\n" + "="*70)
        print("DEMO 5: Fundamentos de Criptografia".center(70))
        print("="*70)
        
        # Demonstra resistência a colisões
        CryptoUtils.demonstrate_collision_resistance()
        
        # Demonstra salting
        print("\n=== Demonstração de Salting ===")
        password = "senha123"
        salt1 = "abc123"
        salt2 = "xyz789"
        
        hash1 = CryptoUtils.hash_with_salt(password, salt1)
        hash2 = CryptoUtils.hash_with_salt(password, salt2)
        
        print(f"Senha: '{password}'")
        print(f"\nCom salt '{salt1}': {hash1}")
        print(f"Com salt '{salt2}': {hash2}")
        print(f"\nMesma senha, salts diferentes = hashes diferentes!")