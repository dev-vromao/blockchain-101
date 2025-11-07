"""
Módulo de Utilitários Criptográficos
Implementa funções de hashing e demonstrações de segurança
"""

import hashlib
from typing import Tuple


class CryptoUtils:
    """
    Utilitários criptográficos para demonstração de conceitos de hashing.
    
    Esta classe implementa diferentes algoritmos de hash e demonstra
    conceitos fundamentais de segurança em blockchain.
    """
    
    @staticmethod
    def hash_sha256(data: str) -> str:
        """
        Gera hash SHA-256 de uma string.
        
        Args:
            data: String a ser hasheada
            
        Returns:
            Hash hexadecimal de 64 caracteres
            
        Exemplo:
            >>> CryptoUtils.hash_sha256("Hello World")
            'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
        """
        return hashlib.sha256(data.encode()).hexdigest()
    
    @staticmethod
    def hash_md5(data: str) -> str:
        """
        Gera hash MD5 de uma string (apenas para fins educacionais).
        
        AVISO: MD5 não é seguro para uso em produção!
        """
        return hashlib.md5(data.encode()).hexdigest()
    
    @staticmethod
    def hash_sha512(data: str) -> str:
        """Gera hash SHA-512 de uma string."""
        return hashlib.sha512(data.encode()).hexdigest()
    
    @staticmethod
    def hash_with_salt(data: str, salt: str) -> str:
        """
        Gera hash com salt para aumentar segurança.
        
        O salt adiciona aleatoriedade, protegendo contra ataques de
        tabelas rainbow e força bruta.
        
        Args:
            data: Dados a serem hasheados
            salt: String aleatória para adicionar entropia
            
        Returns:
            Hash do dado combinado com salt
        """
        return hashlib.sha256((data + salt).encode()).hexdigest()
    
    @staticmethod
    def verify_hash(data: str, expected_hash: str) -> bool:
        """
        Verifica integridade comparando hash calculado com esperado.
        
        Args:
            data: Dados originais
            expected_hash: Hash esperado
            
        Returns:
            True se os hashes coincidem, False caso contrário
        """
        return CryptoUtils.hash_sha256(data) == expected_hash
    
    @staticmethod
    def demonstrate_collision_resistance():
        """
        Demonstra a resistência a colisões do SHA-256.
        Pequenas mudanças nos dados resultam em hashes completamente diferentes.
        """
        data1 = "Blockchain"
        data2 = "Blockchail"  # Apenas uma letra diferente
        
        hash1 = CryptoUtils.hash_sha256(data1)
        hash2 = CryptoUtils.hash_sha256(data2)
        
        print("=== Demonstração de Resistência a Colisões ===")
        print(f"Dado 1: '{data1}'")
        print(f"Hash 1: {hash1}")
        print(f"\nDado 2: '{data2}'")
        print(f"Hash 2: {hash2}")
        print(f"\nHashes são diferentes: {hash1 != hash2}")
        print(f"Diferença de caracteres: 1 letra")
        print(f"Similaridade dos hashes: ~0% (completamente diferentes)")