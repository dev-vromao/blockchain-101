"""
Exemplos Práticos de Uso da Biblioteca Blockchain101
"""

from blockchain import Blockchain, Block, Transaction, CryptoUtils, ConcurrentMiner


def exemplo_1_blockchain_simples():
    """Exemplo 1: Criar uma blockchain simples."""
    print("\n" + "="*70)
    print("EXEMPLO 1: Blockchain Simples".center(70))
    print("="*70)
    
    # Criar blockchain
    bc = Blockchain(difficulty=3)
    
    # Adicionar alguns blocos
    bc.add_block(Block(1, '01/01/2024 10:00', 'Primeiro bloco de dados'))
    bc.add_block(Block(2, '01/01/2024 11:00', 'Segundo bloco de dados'))
    bc.add_block(Block(3, '01/01/2024 12:00', 'Terceiro bloco de dados'))
    
    # Validar e exibir
    bc.is_chain_valid()
    bc.print_chain()


def exemplo_2_sistema_bancario():
    """Exemplo 2: Sistema bancário simples."""
    print("\n" + "="*70)
    print("EXEMPLO 2: Sistema Bancário".center(70))
    print("="*70)
    
    bc = Blockchain(difficulty=2)
    
    # Simular transações bancárias
    print("\n📝 Dia 1: Transações iniciais")
    bc.add_transaction(Transaction("Alice", "Bob", 100))
    bc.add_transaction(Transaction("Alice", "Carol", 50))
    bc.mine_pending_transactions("Miner1")
    
    print("\n📝 Dia 2: Mais transações")
    bc.add_transaction(Transaction("Bob", "Carol", 30))
    bc.add_transaction(Transaction("Carol", "Alice", 20))
    bc.mine_pending_transactions("Miner2")
    
    print("\n📝 Dia 3: Transações finais")
    bc.add_transaction(Transaction("Bob", "Alice", 40))
    bc.mine_pending_transactions("Miner1")
    
    # Relatório final
    print("\n" + "="*70)
    print("RELATÓRIO FINANCEIRO".center(70))
    print("="*70)
    print(f"Alice:  {bc.get_balance('Alice'):>10.2f} moedas")
    print(f"Bob:    {bc.get_balance('Bob'):>10.2f} moedas")
    print(f"Carol:  {bc.get_balance('Carol'):>10.2f} moedas")
    print(f"Miner1: {bc.get_balance('Miner1'):>10.2f} moedas (2 blocos minerados)")
    print(f"Miner2: {bc.get_balance('Miner2'):>10.2f} moedas (1 bloco minerado)")
    
    # Validar integridade
    print()
    bc.is_chain_valid()


def exemplo_3_comparacao_hashes():
    """Exemplo 3: Comparação de algoritmos de hash."""
    print("\n" + "="*70)
    print("EXEMPLO 3: Comparação de Algoritmos de Hash".center(70))
    print("="*70)
    
    mensagem = "Blockchain é revolucionário!"
    
    print(f"\nMensagem: '{mensagem}'")
    print(f"Tamanho: {len(mensagem)} caracteres")
    
    print("\n--- Diferentes Algoritmos ---")
    
    md5 = CryptoUtils.hash_md5(mensagem)
    print(f"MD5:     {md5} ({len(md5)} chars)")
    
    sha256 = CryptoUtils.hash_sha256(mensagem)
    print(f"SHA-256: {sha256} ({len(sha256)} chars)")
    
    sha512 = CryptoUtils.hash_sha512(mensagem)
    print(f"SHA-512: {sha512} ({len(sha512)} chars)")
    
    print("\n💡 Observação:")
    print("   - MD5: 32 caracteres (não recomendado para segurança)")
    print("   - SHA-256: 64 caracteres (usado em Bitcoin)")
    print("   - SHA-512: 128 caracteres (mais seguro, mas mais lento)")


def exemplo_4_teste_adulteracao():
    """Exemplo 4: Testar diferentes tipos de adulteração."""
    print("\n" + "="*70)
    print("EXEMPLO 4: Testes de Adulteração".center(70))
    print("="*70)
    
    bc = Blockchain(difficulty=2)
    bc.add_block(Block(1, '01/01/2024', 'Dados originais do bloco 1'))
    bc.add_block(Block(2, '02/01/2024', 'Dados originais do bloco 2'))
    
    print("\n✅ Blockchain criada e válida")
    bc.is_chain_valid()
    
    # Teste 1: Modificar dados
    print("\n🔨 Teste 1: Modificando dados do bloco 1")
    bc.chain[1].data = 'Dados ADULTERADOS'
    bc.is_chain_valid()
    
    # Restaurar
    bc.chain[1].data = 'Dados originais do bloco 1'
    bc.chain[1].hash = bc.chain[1].create_hash()
    
    # Teste 2: Modificar hash anterior
    print("\n🔨 Teste 2: Modificando hash anterior do bloco 2")
    original_prior = bc.chain[2].prior_hash
    bc.chain[2].prior_hash = '0' * 64
    bc.is_chain_valid()
    
    # Restaurar
    bc.chain[2].prior_hash = original_prior
    
    # Teste 3: Modificar nonce
    print("\n🔨 Teste 3: Modificando nonce do bloco 1")
    bc.chain[1].nonce = 999999
    bc.is_chain_valid()
    
    print("\n💡 Conclusão: Qualquer modificação é detectada!")


def exemplo_5_benchmark_dificuldade():
    """Exemplo 5: Benchmark de diferentes dificuldades."""
    print("\n" + "="*70)
    print("EXEMPLO 5: Impacto da Dificuldade na Mineração".center(70))
    print("="*70)
    
    import time
    
    dificuldades = [2, 3, 4, 5]
    resultados = []
    
    for diff in dificuldades:
        bc = Blockchain(difficulty=diff)
        bloco = Block(1, '01/01/2024', 'Teste de dificuldade')
        
        inicio = time.time()
        bloco.mine_block(diff)
        tempo = time.time() - inicio
        
        resultados.append((diff, tempo, bloco.nonce))
        
        print(f"\nDificuldade {diff}: {tempo:.2f}s | Nonce: {bloco.nonce}")
    
    print("\n" + "="*70)
    print("ANÁLISE DE CRESCIMENTO".center(70))
    print("="*70)
    
    tempo_base = resultados[0][1]
    for diff, tempo, nonce in resultados:
        fator = tempo / tempo_base
        print(f"Dificuldade {diff}: {fator:.1f}x mais lento que dificuldade {dificuldades[0]}")


def exemplo_6_rede_distribuida_simulada():
    """Exemplo 6: Simular rede distribuída com múltiplos nós."""
    print("\n" + "="*70)
    print("EXEMPLO 6: Rede Distribuída Simulada".center(70))
    print("="*70)
    
    # Criar 3 "nós" (blockchains independentes)
    no1 = Blockchain(difficulty=2)
    no2 = Blockchain(difficulty=2)
    no3 = Blockchain(difficulty=2)
    
    print("\n📡 3 nós criados na rede")
    
    # Adicionar bloco no nó 1
    print("\n⛏️  Nó 1 minera bloco...")
    no1.add_block(Block(1, '01/01/2024', 'Dados do nó 1'))
    
    # "Propagar" para outros nós (copiar bloco)
    print("📤 Propagando bloco para outros nós...")
    no2.add_block(Block(1, '01/01/2024', 'Dados do nó 1'))
    no3.add_block(Block(1, '01/01/2024', 'Dados do nó 1'))
    
    # Verificar consenso
    print("\n🔍 Verificando consenso...")
    hash1 = no1.chain[1].hash
    hash2 = no2.chain[1].hash
    hash3 = no3.chain[1].hash
    
    if hash1 == hash2 == hash3:
        print("✅ Consenso alcançado! Todos os nós têm o mesmo bloco")
        print(f"   Hash: {hash1[:16]}...")
    else:
        print("❌ Falha no consenso!")
    
    print(f"\n📊 Estado da rede:")
    print(f"   Nó 1: {len(no1.chain)} blocos")
    print(f"   Nó 2: {len(no2.chain)} blocos")
    print(f"   Nó 3: {len(no3.chain)} blocos")


# Menu de exemplos
def menu_exemplos():
    """Menu interativo de exemplos."""
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║                   📚 EXEMPLOS PRÁTICOS                         ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    
    exemplos = {
        '1': exemplo_1_blockchain_simples,
        '2': exemplo_2_sistema_bancario,
        '3': exemplo_3_comparacao_hashes,
        '4': exemplo_4_teste_adulteracao,
        '5': exemplo_5_benchmark_dificuldade,
        '6': exemplo_6_rede_distribuida_simulada
    }
    
    while True:
        print("\n" + "="*70)
        print("MENU DE EXEMPLOS".center(70))
        print("="*70)
        print("1. Blockchain Simples")
        print("2. Sistema Bancário")
        print("3. Comparação de Algoritmos de Hash")
        print("4. Testes de Adulteração")
        print("5. Benchmark de Dificuldade")
        print("6. Rede Distribuída Simulada")
        print("7. Executar Todos os Exemplos")
        print("0. Voltar")
        print("="*70)
        
        escolha = input("\nEscolha um exemplo: ").strip()
        
        if escolha == '0':
            break
        elif escolha == '7':
            for func in exemplos.values():
                func()
                input("\n⏸️  Pressione ENTER para continuar...")
        elif escolha in exemplos:
            exemplos[escolha]()
        else:
            print("\n❌ Opção inválida!")
        
        if escolha != '7' and escolha in exemplos:
            input("\n⏸️  Pressione ENTER para continuar...")


if __name__ == "__main__":
    menu_exemplos()
