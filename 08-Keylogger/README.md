# Projeto 08: Implementação de Keylogger para Fins Educativos

## Visão Geral
Este projeto demonstra o funcionamento técnico de um **Keylogger**, uma ferramenta
de monitorização desenhada para capturar e registar todas as teclas premidas num
dispositivo de entrada. O objetivo desta demonstração é entender como este tipo de
malware opera para melhor desenvolver estratégias de deteção e mitigação.

---

## Conceito Técnico
O Keylogger atua na camada de interface entre o hardware (teclado) e o sistema
operativo. Ele interceta os eventos de input antes de serem processados pelas
aplicações finais, permitindo a captura de:
* **Credenciais de Acesso:** Passwords e nomes de utilizador.
* **Comandos de Sistema:** Comandos executados no terminal (ex: sudo).
* **Comunicações:** Mensagens e e-mails escritos em texto limpo.

### Implementação Utilizada
Nesta PoC (Proof of Concept), utilizei um script em **Python** com a biblioteca
'pynput'. Esta abordagem é comum em ataques de "User Mode", onde o script monitoriza
as APIs de eventos do sistema operativo para registar o input.

---

## Demonstração de Execução (PoC)

1. **Ativação:** O script 'keylogger.py' é executado no sistema alvo.
2. **Captura:** O listener interceta as teclas e envia-as para um ficheiro local chamado 'keylog.txt'
3. **Análise de Dados:** O ficheiro gerado revela a sequência exata de caracteres
inseridos, incluindo teclas especiais como '[Key.backspace]' ou '[Key.enter]'.

### Exemplo de Output Capturado:
No meu teste prático, o ficheiro 'keylog.txt' registou com sucesso:
```text
sudo apt update [Key.enter]
kali123 [Key.enter]
```

# Estratégias de Defesa e Mitigação
Como profissional de Cibersegurança, a compreensão desta ameaça permite recomendar as
seguintes defesas:
* **Utilização de MFA (Multi-Factor Authentication):** Mesmo que a password seja
capturada, o atacante não consegue aceder sem o segundo fator.
* **Soluçóes EDR/Antivírus:** Identificam processos anómalos que tentam injetar hooks no
sistema de input.
* **Teclados Virtuais: Úteis em ambientes de alto risco para evitar a interceção física ou de
drivers.

**Nota:** Este projeto foi realizado em ambiente controlado para fins estritamente educacionais
e de portfólio. O uso destas técnicas sem autorização explícita é ilegal e antiético.

