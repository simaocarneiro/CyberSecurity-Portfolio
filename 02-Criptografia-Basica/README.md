# Projeto 02: Criptografia Simétrica com Python (Fernet)

## Descrição do Projeto
Neste projeto, desenvolvi um script em Python para demonstrar os conceitos fundamentais de criptografia simétrica. O código utiliza a especificação **Fernet**, que garante que uma mensagem enccriptada não possa ser lida ou manipulada sem a chave correspondente.

Este laboratório foca-se em três pilares da cibersegurança:
1. **Geração de Chave:** Criação de uma chave aleatória e segura.
2. **Confidencialidade:** Encriptação de uma mensagem de texto.
3. **Integridade:** Desencriptação bem-sucedida para validar o conteúdo original.

--

## Ferramentas Utilizadas
* **Kali Linux:** Ambiente de desenvolvimento.
* **Python3:** Linguagem de programação.
* **Biblioteca Cryptography (Fernet):** Implementação de criptografia simétrica de nível industrial.

--

## Como o Script Funciona
O script executa o seguinte fluxo lógico:
1. **Gera uma chave única** através do método 'Fernet.generate_key()'
2. **Instancia um objeto Cipher** com essa chave.
3. **Encripta** a mensagem definida ('Criptografia basica concluida com sucesso!').
4. **Exibe os resultados** no terminal (Chave e Texto Cifrado).
5. **Realiza a desencriptação** para provar que a chave é válida e o processo foi concluído.

## Como Executar
1. Certicar de que temos a biblioteca necessária instalada:
	'''bash
	pip instal cryptography

## Resultados e Aprendizagem
Este projeto permitiu-me entender a diferença entre cifragens simples e algoritmos modernos.
Ao utilizar o Fernet, estou a trabalhar com encriptação simétrica, onde a mesma chave é
necessária tanto para revelar a informação.

Diferente de métodos básicos (como a Cifra de César), este método é computacionalmente
seguro e impossível de quebrar por força bruta num tempo úti, sendo a base para muitos
sistemas de proteção de dados atuais.
