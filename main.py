import json

FILE_NAME = "solicitacoes.json"

def main():
    try:
        requests = read_json(FILE_NAME)
        print(f"Registros lidos: {len(requests)}")
        print(requests[0])
    except FileNotFoundError:
        print(f"Erro: Arquivo '{FILE_NAME}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Arquivo '{FILE_NAME}' está em um formato inválido.")
    except Exception as e:
        print(f"Erro inesperado ao carregar arquivo: {e}")

def read_json(file: str):
    with open(file, "r", encoding="utf-8") as document:
        return json.load(document)

if __name__ == "__main__":
    main()