"""
Módulo de Mineração Concorrente
Implementa mineração com múltiplas threads
"""

import time
import threading
from typing import Dict, List

from block import Block

# from block import Block


class ConcurrentMiner:
    """
    Sistema de mineração concorrente com múltiplas threads.
    
    Simula competição entre mineradores na rede blockchain.
    """
    
    @staticmethod
    def mine_with_threads(block: Block, difficulty: int, num_threads: int) -> Dict:
        """
        Minera bloco usando múltiplas threads competindo.
        
        Args:
            block: Bloco a ser minerado
            difficulty: Nível de dificuldade
            num_threads: Número de threads mineradoras
            
        Returns:
            Dicionário com estatísticas da mineração
        """
        stop_event = threading.Event()
        threads = []
        start_time = time.time()
        winner = {'thread_id': None, 'nonce': None, 'hash': None}
        
        def mine_worker(thread_id: int):
            """Worker de mineração para cada thread."""
            # Cada thread trabalha com cópia do bloco
            local_block = Block(
                block.index,
                block.timestamp,
                block.data,
                block.prior_hash
            )
            # Offset inicial diferente para cada thread
            local_block.nonce = thread_id * 10000
            
            prefix = '0' * difficulty
            attempts = 0
            
            while not stop_event.is_set():
                if local_block.hash.startswith(prefix):
                    # Encontrou! Sinaliza outras threads
                    stop_event.set()
                    winner['thread_id'] = thread_id
                    winner['nonce'] = local_block.nonce
                    winner['hash'] = local_block.hash
                    print(f"🏆 Thread {thread_id} venceu! Nonce: {local_block.nonce}")
                    break
                
                local_block.nonce += num_threads  # Incrementa por num_threads
                local_block.hash = local_block.create_hash()
                attempts += 1
                
                # Feedback periódico
                if attempts % 5000 == 0 and not stop_event.is_set():
                    print(f"   Thread {thread_id}: {attempts} tentativas...")
        
        # Inicia threads
        print(f"\n⛏️  Iniciando mineração concorrente com {num_threads} threads...")
        print(f"   Dificuldade: {difficulty} (hash deve começar com {'0'*difficulty})")
        
        for i in range(num_threads):
            t = threading.Thread(target=mine_worker, args=(i,))
            t.start()
            threads.append(t)
        
        # Aguarda conclusão
        for t in threads:
            t.join()
        
        elapsed = time.time() - start_time
        
        print(f"\n✅ Mineração concluída em {elapsed:.2f} segundos")
        
        return {
            'threads': num_threads,
            'time': elapsed,
            'winner_thread': winner['thread_id'],
            'nonce': winner['nonce'],
            'hash': winner['hash']
        }
    
    @staticmethod
    def benchmark_mining(block: Block, difficulty: int, max_threads: int = 8) -> List[Dict]:
        """
        Realiza benchmark de mineração com diferentes números de threads.
        
        Args:
            block: Bloco a ser minerado
            difficulty: Nível de dificuldade
            max_threads: Número máximo de threads para testar
            
        Returns:
            Lista de resultados do benchmark
        """
        results = []
        thread_counts = [1, 2, 4, max_threads]
        
        print("\n" + "="*70)
        print("BENCHMARK DE MINERAÇÃO".center(70))
        print("="*70)
        
        for num_threads in thread_counts:
            result = ConcurrentMiner.mine_with_threads(block, difficulty, num_threads)
            results.append(result)
            print(f"\n📊 Resultado: {num_threads} thread(s) = {result['time']:.2f}s")
        
        # Análise dos resultados
        print("\n" + "="*70)
        print("ANÁLISE DE DESEMPENHO".center(70))
        print("="*70)
        
        baseline = results[0]['time']
        for r in results:
            speedup = baseline / r['time']
            efficiency = (speedup / r['threads']) * 100
            print(f"{r['threads']} thread(s): {r['time']:.2f}s | "
                  f"Speedup: {speedup:.2f}x | Eficiência: {efficiency:.1f}%")
        
        return results