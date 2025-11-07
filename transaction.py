"""
Módulo de Transações
Define a estrutura de transações na blockchain
"""

import time
import json
from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class Transaction:
    """
    Representa uma transação na blockchain.
    
    Attributes:
        sender: Endereço do remetente
        receiver: Endereço do destinatário
        amount: Quantidade transferida
        timestamp: Momento da transação
    """
    sender: str
    receiver: str
    amount: float
    timestamp: float = None
    
    def __post_init__(self):
        """Inicializa timestamp se não fornecido."""
        if self.timestamp is None:
            self.timestamp = time.time()
    
    def to_dict(self) -> Dict:
        """
        Converte transação para dicionário.
        
        Returns:
            Dicionário com atributos da transação
        """
        return asdict(self)
    
    def to_string(self) -> str:
        """
        Converte transação para string para hashing.
        
        Returns:
            String JSON ordenada da transação
        """
        return json.dumps(self.to_dict(), sort_keys=True)
    
    def __repr__(self) -> str:
        """Representação legível da transação."""
        return f"Transaction({self.sender} -> {self.receiver}: {self.amount})"
