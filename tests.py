"""
Testes Unitários para EduChain
Arquivo de exemplo para testes (pode ser expandido com pytest)
"""

from block import Block
from blockchain import Blockchain
from crypto_utils import CryptoUtils
from transaction import Transaction


def test_crypto_utils():
    """Testa utilitários de criptografia."""
    print("\n🧪 Testando CryptoUtils...")
    
    # Teste 1: Hash determinístico
    hash1 = CryptoUtils.hash_sha256("teste")
    hash2 = CryptoUtils.hash_sha256("teste")
    assert hash1 == hash2, "Hash deve ser determinístico"
    print("✅ Hash determinístico")
    
    # Teste 2: Hashes diferentes para entradas diferentes
    hash3 = CryptoUtils.hash_sha256("teste2")
    assert hash1 != hash3, "Hashes devem ser diferentes"
    print("✅ Hashes únicos")
    
    # Teste 3: Tamanho do hash
    assert len(hash1) == 64, "SHA-256 deve ter 64 caracteres"
    print("✅ Tamanho correto do hash")
    
    # Teste 4: Verificação de hash
    assert CryptoUtils.verify_hash("teste", hash1), "Verificação deve passar"
    print("✅ Verificação de hash")


def test_block():
    """Testa criação e mineração de blocos."""
    print("\n🧪 Testando Block...")
    
    # Teste 1: Criação de bloco
    bloco = Block(0, '01/01/2024', 'dados teste')
    assert bloco.index == 0, "Índice deve ser 0"
    assert bloco.nonce == 0, "Nonce inicial deve ser 0"
    print("✅ Criação de bloco")
    
    # Teste 2: Hash é calculado
    assert len(bloco.hash) == 64, "Hash deve existir"
    print("✅ Hash calculado")
    
    # Teste 3: Mineração
    bloco.mine_block(2)
    assert bloco.hash.startswith('00'), "Hash deve começar com 00"
    assert bloco.nonce > 0, "Nonce deve ter sido incrementado"
    print("✅ Mineração funcional")


def test_blockchain():
    """Testa funcionalidades da blockchain."""
    print("\n🧪 Testando Blockchain...")
    
    # Teste 1: Inicialização
    bc = Blockchain(difficulty=2)
    assert len(bc.chain) == 1, "Deve ter bloco gênese"
    print("✅ Inicialização")
    
    # Teste 2: Adicionar bloco
    bc.add_block(Block(1, '01/01/2024', 'dados'))
    assert len(bc.chain) == 2, "Deve ter 2 blocos"
    print("✅ Adição de bloco")
    
    # Teste 3: Validação
    assert bc.is_chain_valid(), "Blockchain deve ser válida"
    print("✅ Validação")
    
    # Teste 4: Detecção de adulteração
    bc.chain[1].data = 'adulterado'
    assert not bc.is_chain_valid(), "Deve detectar adulteração"
    print("✅ Detecção de adulteração")


def test_transactions():
    """Testa sistema de transações."""
    print("\n🧪 Testando Transações...")
    
    # Teste 1: Criar transação
    tx = Transaction("Alice", "Bob", 50)
    assert tx.sender == "Alice", "Remetente correto"
    assert tx.receiver == "Bob", "Destinatário correto"
    assert tx.amount == 50, "Valor correto"
    print("✅ Criação de transação")
    
    # Teste 2: Sistema de saldos
    bc = Blockchain(difficulty=2)
    bc.add_transaction(Transaction("Alice", "Bob", 50))
    bc.mine_pending_transactions("Miner1")
    
    assert bc.get_balance("Alice") == -50, "Alice deve ter -50"
    assert bc.get_balance("Bob") == 50, "Bob deve ter 50"
    assert bc.get_balance("Miner1") == 100, "Miner1 deve ter recompensa"
    print("✅ Sistema de saldos")


def run_all_tests():
    """Executa todos os testes."""
    print("\n" + "="*70)
    print("EXECUTANDO TESTES".center(70))
    print("="*70)
    
    try:
        test_crypto_utils()
        test_block()
        test_blockchain()
        test_transactions()
        
        print("\n" + "="*70)
        print("✅ TODOS OS TESTES PASSARAM!".center(70))
        print("="*70)
        
    except AssertionError as e:
        print(f"\n❌ TESTE FALHOU: {e}")
    except Exception as e:
        print(f"\n❌ ERRO: {e}")


if __name__ == "__main__":
    run_all_tests()