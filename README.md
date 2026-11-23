# CTF 08: Segredo esquecido no repositório

Projeto criado a partir do [template-seguranca](https://github.com/renanscarmo/template-seguranca)
para praticar segurança em Python.

## Objetivo

Mostrar que uma chave apagada do código continua no histórico do Git e usar um scanner de segredos para achá-la.

## Como foi

1. **Antes:** a chave da API foi escrita no `config.py` e enviada ao GitHub. No commit seguinte ela foi trocada por uma leitura de variável de ambiente, e o programador achou que isso resolvia.
2. **Detecção:** abrindo o histórico de commits, a chave antiga aparece no commit que a escreveu e também no que a removeu. O Bandit e o pip-audit ficaram verdes. O Gitleaks, rodando manualmente e com uma regra própria, varreu todo o histórico e achou o segredo.
3. **Depois:** a chave passou a vir de uma variável de ambiente. Mas a correção completa é **revogar a chave antiga e gerar uma nova**, porque a que está no histórico continua válida para quem a copiou.

## O que aprendi

- Apagar um segredo do código não o apaga do histórico do Git
- Uma chave que foi para um repositório deve ser considerada exposta: a atitude certa é revogar e gerar outra
- A chave fica numa variável de ambiente, nunca escrita no código
- O Gitleaks procura segredos em todos os commits, o que o Bandit não faz
- No push o scanner olha só os commits novos, e para varrer o passado é preciso rodá-lo manualmente
- Regras prontas reconhecem formatos conhecidos de chaves, e dá para criar uma regra própria

## Ferramentas

- SAST com Bandit
- SCA com pip-audit
- Scanner de segredos com Gitleaks
- GitHub Actions
