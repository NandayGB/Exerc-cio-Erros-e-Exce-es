import statistics

def calcular_estatisticas(valores):
    if not valores:
        return None
    
    try:
        media = statistics.mean(valores)
        mediana = statistics.median(valores)
        desvio_padrao = statistics.stdev(valores)
        
        return {
            'media': round(media, 2),
            'mediana': round(mediana, 2),
            'desvio_padrao': round(desvio_padrao, 2),
            'minimo': min(valores),
            'maximo': max(valores)
        }
    except statistics.StatisticsError as e:
        print(f"Erro ao calcular estatísticas: {str(e)}")
        return None

def main():
    valores = []
    
    while True:
        print("\nOpções:")
        print("1. Adicionar valor")
        print("2. Calcular estatísticas")
        print("3. Limpar valores")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            while True:
                valor = input("Digite um número positivo ou 'voltar' para retornar: ").strip()
                
                if valor.lower() == 'voltar':
                    break
                
                try:
                    numero = float(valor)
                    
                    if numero < 0:
                        print("❌ Por favor, digite um número positivo.")
                    else:
                        valores.append(numero)
                        print(f"✅ Valor {numero} adicionado com sucesso!")
                except ValueError:
                    print("❌ Por favor, digite um número válido.")
        
        elif escolha == '2':
            if not valores:
                print("⚠️ Nenhum valor inserido. Por favor, adicione alguns valores primeiro.")
            else:
                estatisticas = calcular_estatisticas(valores)
                
                if estatisticas:
                    print("\nResumo Estatístico:")
                    print(f"Média: {estatisticas['media']}")
                    print(f"Mediana: {estatisticas['mediana']}")
                    print(f"Desvio Padrão: {estatisticas['desvio_padrao']}")
                    print(f"Mínimo: {estatisticas['minimo']}")
                    print(f"Máximo: {estatisticas['maximo']}")
        
        elif escolha == '3':
            valores.clear()
            print("✅ Valores limpos com sucesso!")
        
        elif escolha == '4':
            print("Até logo!")
            break
        
        else:
            print("❌ Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()