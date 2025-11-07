"""
EduChain - Biblioteca Educacional de Blockchain
================================================

Pacote Python para aprendizado de tecnologia blockchain.

Módulos:
    - crypto_utils: Utilitários de criptografia e hashing
    - transaction: Estrutura de transações
    - block: Estrutura de blocos
    - blockchain: Implementação da blockchain
    - miner: Mineração concorrente
    - demos: Demonstrações educacionais

Uso básico:
    from educhain import Blockchain, Transaction, Block
    
    # Criar blockchain
    bc = Blockchain(difficulty=4)
    
    # Adicionar transação
    bc.add_transaction(Transaction("Alice", "Bob", 50))
    
    # Minerar bloco
    bc.mine_pending_transactions("Miner1")
    
    # Validar
    bc.is_chain_valid()

Autor: Biblioteca Educacional
Versão: 1.0.0
Licença: MIT
"""

__version__ = "1.0.0"
__author__ = "EduChain Team"
__license__ = "MIT"

# Imports principais para facilitar uso
from crypto_utils import CryptoUtils
from transaction import Transaction
from block import Block
from blockchain import Blockchain
from miner import ConcurrentMiner
from demos import BlockchainDemo

__all__ = [
    'CryptoUtils',
    'Transaction',
    'Block',
    'Blockchain',
    'ConcurrentMiner',
    'BlockchainDemo'
]