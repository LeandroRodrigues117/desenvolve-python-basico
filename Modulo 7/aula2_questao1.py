def main():
   
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    
   
    dia, mes, ano = data.split('/')
    
  
    mes = int(mes)
    
    data_formatada = f"{dia} de {meses[mes - 1]} de {ano}"
    
    
    print(f"Sua data de nascimento é: {data_formatada}")

if __name__ == "__main__":
    main()
