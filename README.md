# Teste Técnico Remoto

Este repositório possui uma automação em Python que lê solicitações de cadastro em formato JSON, com os campos: id, nome, cpf e status. A automação valida os dados de entrada e filtra as solicitações com status "APROVADO" e informações válidas, logo após exporta um arquivo CSV, além de registrar todas as operações dentro de um arquivo de log.

## Pré-requisitos

Para a execução da automação é necessário o python 3.10+, e como foram utilizadas apenas bibliotecas nativas, não requer instalação de nenhum outro pacote.

## Instruções de Execução

Para executar a automação basta seguir os seguintes passos:

1. Baixar o .zip ou fazer o `git clone` desse repositório:

```bash
    git clone https://github.com/PedroIvoKuhn/testeSicredi.git
```

2. Abrir a pasta do repositório (Descompactar antes caso tenha optado pelo .zip)

3. Abrir o terminal e executar o seguinte comando:

```
    python main.py
    ou python3 main.py
```

4. O arquivo CSV e o de LOG serão gerados dentro da pasta

## Premissas e Decisões Adotadas

- **Separador CSV:** O Separador CSV utilizado foi a vírgula por ser o padrão oficial do CSV e ter uma maior compatibilidade, tanto que está no nome _Comma-Separated Values_(Valores separados por vírgula).
- **Validação de CPF:** Como solicitado não houve o cálculo dos dígitos verificadores, mas adicionei uma validação garantindo que o CPF tenha 11 dígitos numéricos sem espaço.
- **Critério de Registros Incompletos:** Os registros com campos nulos (`None`) ou ausentes são ignorados e rastreados no log.
- **Erros e Logs:** Os registros com problemas não interrompem a automação, apenas são logados com o motivo do descarte. Enquanto erros mais importantes, como a ausência ou arquivo corrompido são tratados com mensagens no terminal e registro no log.

## Integração com processos

> Como você adaptaria essa solução para um processo de BPM, no qual os registros fossem recebidos por um formulário e o arquivo CSV fosse gerado após uma etapa de aprovação?

Como os dados viriam de um formulário, não seria mais necessário ter a leitura de um arquivo JSON, com essa automação podendo ser chamada via Webhook ou chamada de API REST. Por mais que possamos assumir que o formulário possua uma validação prévia do CPF para evitar chamadas desnecessárias, eu ainda manteria as validações e adicionaria o verificador de dígitos. Da mesma forma, mesmo que o disparo tenha ocorrido após a aprovação, manteria a verificação de status, garantindo mais segurança.

## Transparência no Uso de Ferramentas

Foi utilizado o Google para pesquisa de documentação para realizar o Log utilizando o `logging`. E foi utilizado IA como suporte para validação de boas práticas e levantamentos de cenários de teste. A implementação, decisões arquiteturais e validação do código foram feitas por mim.
