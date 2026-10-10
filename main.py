import json

FILE_NAME = "solicitacoes.json"

def main():
    try:
        requests = read_json(FILE_NAME)
        print(f"Registros lidos: {len(requests)}")
        filtered_requests = filter_registry(requests)
        print(f"Registros Aprovados: {len(filtered_requests)}")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{FILE_NAME}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Arquivo '{FILE_NAME}' está em um formato inválido.")
    except Exception as e:
        print(f"Erro inesperado ao carregar arquivo: {e}")

def read_json(file: str):
    with open(file, "r", encoding="utf-8") as document:
        return json.load(document)

def filter_registry(registry):
    filtered_registry = []
    for record in registry:
        record_id = record.get("id")
        cpf = record.get("cpf")
        status = record.get("status")
        nome = record.get("nome")

        if ((record_id is None) or (nome is None) or (cpf is None) or (status is None)):
            print(f"Solicitação {record_id} sem os campos necessários.")
            continue
        if (not str(cpf).strip()):
            print(f"Solicitação {record_id} com CPF inválido ou vazio.")
            continue
        if (status != "APROVADO"):
            print(f"Solicitação {record_id} não é APROVADO.")
            continue

        filtered_registry.append(record)

    return filtered_registry

if __name__ == "__main__":
    main()