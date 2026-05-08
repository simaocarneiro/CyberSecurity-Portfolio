# Projeto 14: Secure Web App - Demonstração de SQL Injection e Correção

## Visão Geral
Este projeto consiste num laboratório prático desenvolvido em Python para demonstrar uma das vulnerabilidades web mais críticas: o **SQL Injection**. O objetivo foi criar um ambiente controlado (sandbox) que simula um sistema de
autenticação para testar ataques de bypass e validar medidas defensivas.

## O Conceito do Ataque (Fase 1)
Na fase vulnerável do script, o código utiliza a concatenação direta de strings para construir SQL. Isto permite que um atacante insira caracteres de controlo para manipular a lógica da base de dados.

* **Payload utilizado:** 'admin' --'
* **Mecânica:** A aspa fecha prematuramente o campo do utilizador e os dois traços transforma o resto da query (incluindo a verificação da password num comentário.
* **Resultado:** O sistema permite o acesso como administrador sem que seja necessária uma password válida.

## A Defesa: Paranetrização (Fase 2)
Para neutralizar a ameaça, o projeto demonstra a implementação de **Prepared Statements** (Consultas Parametrizadas).

* **Técnicas:** Em vez de inserir os dados diretamente na query, utilizamos placeholders ('?').
* **Segurança:** O motor da base de dados (SQLite) é instruído a tratar o input do utilizador estritamente como dados (texto) e nunca como código executável.
* **Resultado:** O ataque 'admin' --' é bloqueado com sucesso, pois o sistema procura literalmente um utilizador com esse nome em vez de executar o comando de comentário.

## Tecnologias e Aprendizagem
* **Python 3**: Linguagem utilizada para o motor de simulação
* **SQLite3**: Base de dados em memória para testes rápidos e seguros.
* **Sanitização de Dados**: Aprendizagem crítica sobre o princícpio de "Nunca confiar o input do utilizador".
