"""
Módulo de Blocos
Define a estrutura de blocos da blockchain
"""

import hashlib
import json
import threading
from typing import Any, Dict, Optional


class Block:
    """
    Representa um bloco na blockchain.
    
    Um bloco contém:
    - Índice: posição na cadeia
    - Timestamp: momento de criação
    - Dados: informações armazenadas (transações)
    - Hash anterior: liga ao bloco anterior
    - Nonce: número usado na prova de trabalho
    - Hash: identificador único do bloco
    
    Attributes:
        index: Posição do bloco na blockchain
        timestamp: Momento de criação do bloco
        data: Dados ou transações armazenadas
        prior_hash: Hash do bloco anterior
        nonce: Número usado na mineração (Prova de Trabalho)
        hash: Hash calculado do bloco atual
    """
    
    def __init__(self, index: int, timestamp: str, data: Any, prior_hash: str = ''):
        """
        Inicializa um novo bloco.
        
        Args:
            index: Posição na blockchain
            timestamp: Carimbo de data/hora
            data: Dados a serem armazenados
            prior_hash: Hash do bloco anterior (padrão: string vazia)
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prior_hash = prior_hash
        self.nonce = 0
        self.hash = self.create_hash()
    
    def create_hash(self) -> str:
        """
        Calcula o hash SHA-256 do bloco.
        
        O hash é calculado concatenando todos os atributos do bloco:
        índice + hash anterior + timestamp + dados + nonce
        
        Returns:
            String hexadecimal de 64 caracteres representando o hash
        """
        # Serializa os dados para garantir consistência
        if isinstance(self.data, (dict, list)):
            data_str = json.dumps(self.data, sort_keys=True)
        else:
            data_str = str(self.data)
        
        # Concatena todos os componentes do bloco
        block_string = f"{self.index}{self.prior_hash}{self.timestamp}{data_str}{self.nonce}"
        
        # Gera e retorna o hash SHA-256
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int, stop_event: Optional[threading.Event] = None) -> bool:
        """
        Executa a Prova de Trabalho (PoW) para minerar o bloco.
        
        A mineração consiste em encontrar um nonce que, quando incluído
        no cálculo do hash, produza um hash que comece com N zeros
        (onde N é o nível de dificuldade).
        
        Args:
            difficulty: Número de zeros à esquerda necessários no hash
            stop_event: Evento para interromper mineração concorrente
            
        Returns:
            True se mineração foi concluída, False se foi interrompida
            
        Exemplo:
            Com difficulty=4, o hash deve começar com '0000'
        """
        # Define o prefixo necessário (ex: '0000' para difficulty=4)
        prefix = '0' * difficulty
        
        print(f"⛏️  Minerando bloco {self.index} (dificuldade: {difficulty})...")
        attempts = 0
        
        # Loop até encontrar hash válido ou ser interrompido
        while not self.hash.startswith(prefix):
            # Verifica se deve parar (mineração concorrente)
            if stop_event and stop_event.is_set():
                return False
            
            # Incrementa nonce e recalcula hash
            self.nonce += 1
            self.hash = self.create_hash()
            attempts += 1
            
            # Feedback a cada 10000 tentativas
            if attempts % 10000 == 0:
                print(f"   Tentativa {attempts}: {self.hash[:10]}...")
        
        print(f"✓ Bloco {self.index} minerado! Nonce: {self.nonce}, Hash: {self.hash[:16]}...")
        
        # Sinaliza que encontrou solução (mineração concorrente)
        if stop_event:
            stop_event.set()
        
        return True
    
    def to_dict(self) -> Dict:
        """
        Converte bloco para dicionário para serialização.
        
        Returns:
            Dicionário com todos os atributos do bloco
        """
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'prior_hash': self.prior_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }
    
    def __repr__(self) -> str:
        """Representação legível do bloco."""
        return f"Block(index={self.index}, hash={self.hash[:10]}...)"