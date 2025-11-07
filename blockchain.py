"""
Módulo Blockchain Principal
Implementa a estrutura completa da blockchain
"""

import json
from typing import List
from datetime import datetime

from block import Block
from transaction import Transaction

# Assumindo imports dos módulos anteriores
# from block import Block
# from transaction import Transaction


class Blockchain:
    """
    Implementação completa de uma blockchain educacional.
    
    Gerencia a cadeia de blocos, validação, mineração e consenso.
    
    Attributes:
        chain: Lista de blocos na cadeia
        difficulty: Nível de dificuldade da mineração
        pending_transactions: Transações aguardando inclusão
        mining_reward: Recompensa para mineradores
    """
    
    def __init__(self, difficulty: int = 4):
        """
        Inicializa blockchain com bloco gênese.
        
        Args:
            difficulty: Nível de dificuldade da mineração (padrão: 4)
        """
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.pending_transactions: List[Transaction] = []
        self.mining_reward = 100
        
        # Cria o bloco gênese (primeiro bloco da cadeia)
        self.chain.append(self.create_genesis_block())
        
        print("🎉 Blockchain inicializada!")
        print(f"   Dificuldade: {self.difficulty}")
        print(f"   Bloco Gênese: {self.chain[0].hash[:16]}...")
    
    def create_genesis_block(self) -> Block:
        """
        Cria o bloco gênese (bloco inicial da blockchain).
        
        O bloco gênese é especial porque:
        - Tem índice 0
        - Não possui bloco anterior (prior_hash = '0')
        - Contém dados iniciais fixos
        
        Returns:
            Bloco gênese da blockchain
        """
        return Block(
            index=0,
            timestamp='01/01/2024 00:00:00',
            data='Genesis Block - EduChain v1.0',
            prior_hash='0'
        )
    
    def get_last_block(self) -> Block:
        """
        Retorna o último bloco da cadeia.
        
        Returns:
            Último bloco adicionado à blockchain
        """
        return self.chain[-1]
    
    def add_transaction(self, transaction: Transaction) -> int:
        """
        Adiciona transação à lista de pendentes.
        
        Args:
            transaction: Transação a ser adicionada
            
        Returns:
            Índice do próximo bloco que incluirá esta transação
        """
        self.pending_transactions.append(transaction)
        print(f"📝 Transação adicionada: {transaction}")
        return self.get_last_block().index + 1
    
    def mine_pending_transactions(self, miner_address: str) -> Block:
        """
        Minera bloco com transações pendentes e recompensa minerador.
        
        Args:
            miner_address: Endereço do minerador (recebe recompensa)
            
        Returns:
            Bloco minerado
        """
        # Cria transação de recompensa para o minerador
        reward_tx = Transaction(
            sender="SYSTEM",
            receiver=miner_address,
            amount=self.mining_reward
        )
        self.pending_transactions.append(reward_tx)
        
        # Cria novo bloco com transações pendentes
        new_block = Block(
            index=len(self.chain),
            timestamp=datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            data=[tx.to_dict() for tx in self.pending_transactions],
            prior_hash=self.get_last_block().hash
        )
        
        # Minera o bloco
        new_block.mine_block(self.difficulty)
        
        # Adiciona à cadeia e limpa transações pendentes
        self.chain.append(new_block)
        self.pending_transactions = []
        
        print(f"💎 Minerador {miner_address} recebeu {self.mining_reward} moedas!")
        
        return new_block
    
    def add_block(self, new_block: Block) -> None:
        """
        Adiciona novo bloco à blockchain após mineração.
        
        Args:
            new_block: Bloco a ser adicionado
        """
        new_block.prior_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    
    def is_chain_valid(self) -> bool:
        """
        Valida integridade completa da blockchain.
        
        Verifica:
        1. Hash de cada bloco está correto
        2. Cada bloco aponta corretamente para o anterior
        3. Hash atende ao nível de dificuldade
        
        Returns:
            True se blockchain é válida, False caso contrário
        """
        print("\n🔍 Validando blockchain...")
        
        # Começa do segundo bloco (índice 1), pois gênese não tem prior
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verifica 1: Hash do bloco atual está correto?
            if current_block.hash != current_block.create_hash():
                print(f"❌ Bloco {i}: Hash inválido!")
                print(f"   Hash armazenado: {current_block.hash}")
                print(f"   Hash calculado: {current_block.create_hash()}")
                return False
            
            # Verifica 2: Bloco atual aponta para o anterior?
            if current_block.prior_hash != previous_block.hash:
                print(f"❌ Bloco {i}: Encadeamento quebrado!")
                print(f"   Prior hash esperado: {previous_block.hash}")
                print(f"   Prior hash atual: {current_block.prior_hash}")
                return False
            
            # Verifica 3: Hash atende dificuldade?
            prefix = '0' * self.difficulty
            if not current_block.hash.startswith(prefix):
                print(f"❌ Bloco {i}: Não atende dificuldade!")
                print(f"   Esperado: hash começando com '{prefix}'")
                print(f"   Obtido: {current_block.hash[:10]}...")
                return False
        
        print("✅ Blockchain válida! Todos os blocos estão íntegros.")
        return True
    
    def get_balance(self, address: str) -> float:
        """
        Calcula saldo de um endereço analisando toda a blockchain.
        
        Args:
            address: Endereço a consultar
            
        Returns:
            Saldo total do endereço
        """
        balance = 0
        
        for block in self.chain:
            if isinstance(block.data, list):
                for tx in block.data:
                    if isinstance(tx, dict):
                        if tx.get('sender') == address:
                            balance -= tx.get('amount', 0)
                        if tx.get('receiver') == address:
                            balance += tx.get('amount', 0)
        
        return balance
    
    def print_chain(self) -> None:
        """Imprime representação visual da blockchain."""
        print("\n" + "="*70)
        print("BLOCKCHAIN COMPLETA".center(70))
        print("="*70)
        
        for block in self.chain:
            print(f"\n📦 Bloco #{block.index}")
            print(f"   Timestamp: {block.timestamp}")
            print(f"   Hash Anterior: {block.prior_hash[:16]}...")
            print(f"   Hash: {block.hash}")
            print(f"   Nonce: {block.nonce}")
            
            # Formata dados de forma legível
            if isinstance(block.data, list):
                print(f"   Transações: {len(block.data)}")
                for tx in block.data[:3]:  # Mostra até 3 transações
                    if isinstance(tx, dict):
                        print(f"      • {tx.get('sender')} -> {tx.get('receiver')}: {tx.get('amount')}")
            else:
                print(f"   Dados: {str(block.data)[:50]}...")
        
        print("\n" + "="*70)
        print(f"Total de blocos: {len(self.chain)}")
        print("="*70)
    
    def to_json(self, indent: int = 4) -> str:
        """
        Exporta blockchain para JSON.
        
        Args:
            indent: Espaçamento da formatação
            
        Returns:
            String JSON da blockchain
        """
        return json.dumps(
            [block.to_dict() for block in self.chain],
            indent=indent
        )
    
    def save_to_file(self, filename: str) -> None:
        """
        Salva blockchain em arquivo JSON.
        
        Args:
            filename: Nome do arquivo para salvar
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.to_json())
        print(f"💾 Blockchain salva em '{filename}'")