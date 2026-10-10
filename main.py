import json, csv, logging

FILE_NAME = "solicitacoes.json"
CSV_NAME = "aprovados.csv"
LOG_NAME = "processamento.log"

logging.basicConfig(
    filename=LOG_NAME,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
    filemode="w"
)

def main():
    try:
        logging.info("Inicio do processamento.")
        requests = read_json(FILE_NAME)
        print(f"Registros lidos: {len(requests)}.")
        logging.info(f"Total de registros lidos: {len(requests)}.")
        filtered_requests = filter_registry(requests)
        print(f"Registros Aprovados: {len(filtered_requests)}")
        generate_csv(filtered_requests, CSV_NAME)
        logging.info(f"Total de registros exportados: {len(filtered_requests)}.")
        logging.info("Processamento concluído com sucesso.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{FILE_NAME}' não encontrado.")
        logging.error(f"Erro: Arquivo '{FILE_NAME}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Arquivo '{FILE_NAME}' está em um formato inválido.")
        logging.error(f"Erro: Arquivo '{FILE_NAME}' está em um formato inválido.")
    except (IOError, OSError) as e:
        print(f"Erro de E/S ao ler ou gravar arquivos: {e}")
        logging.error(f"Erro de E/S ao ler ou gravar arquivos: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        logging.error(f"Erro inesperado: {e}")

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
            logging.info(f"Registro {record_id} ignorado: Sem os campos necessários.")
            continue
        clean_cpf = str(cpf).strip()
        if ((not clean_cpf) or (len(clean_cpf) != 11) or (not clean_cpf.isdigit())):
            print(f"Solicitação {record_id} com CPF inválido.")
            logging.info(f"Registro {record_id} ignorado: CPF deve conter exatamente 11 dígitos numéricos.")
            continue
        if (status != "APROVADO"):
            print(f"Solicitação {record_id} não é APROVADO.")
            logging.info(f"Registro {record_id} ignorado: Status diferente de APROVADO.")
            continue

        filtered_registry.append([record_id, nome, clean_cpf])

    return filtered_registry

def generate_csv(approved_csv, csv_name):
    with open(csv_name, mode="w", encoding="utf-8", newline="") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(["id", "nome", "cpf"])
        writer.writerows(approved_csv)

if __name__ == "__main__":
    main()