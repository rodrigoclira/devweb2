Reproduza o material "[Do Zero a Implantação](https://cassiobotaro.dev/do_zero_a_implantacao)" que utiliza FAST API para desenvolver uma API com TDD. 

A entrega da atividade será o repositório com todos os arquivos e commits indicados no tutorial. 
As seguintes etapas precisam constar no tutorial: 

Atividades que precisam ser realizads
- [x] ▶️ [Introdução](https://cassiobotaro.dev/do_zero_a_implantacao/)
- [x] 💭 [Planejando o que será desenvolvido](https://cassiobotaro.dev/do_zero_a_implantacao/planejando/)
- [x] 🔨 [Escolhendo as melhores ferramentas](https://cassiobotaro.dev/do_zero_a_implantacao/ferramentas/)
- [x] 📖 [Iniciando o projeto](https://cassiobotaro.dev/do_zero_a_implantacao/projeto/)
- [x] 🌎 [Um pouco sobre a web](https://cassiobotaro.dev/do_zero_a_implantacao/web/)
- [ ] 🐍 [Primeiros passos com python](https://cassiobotaro.dev/do_zero_a_implantacao/python/)
- [x] 🐐 [Desenvolvimento guiado por testes](https://cassiobotaro.dev/do_zero_a_implantacao/testes/)
- [x] ⚡️ [Hello Fastapi](https://cassiobotaro.dev/do_zero_a_implantacao/hello_fastapi/)
- [x] ✔️ [Integração contínua](https://cassiobotaro.dev/do_zero_a_implantacao/integracao/)
- [ ] 🚀 [Mandando um foguete pro espaço](https://cassiobotaro.dev/do_zero_a_implantacao/deploy/)
- [x] 📝 [Criando uma tarefa](https://cassiobotaro.dev/do_zero_a_implantacao/criar/)
- [x] 🏆 [O desafio](https://cassiobotaro.dev/do_zero_a_implantacao/desafio/)
- [ ] 📑 [Referências e Dicas](https://cassiobotaro.dev/do_zero_a_implantacao/referencias/)

As seções "Primeiros passos com python" e "Mandando um foguete para o espaço" não são obrigatórios.

## Informações adicionais: 

### Criação do arquivo dev-requirements.txt

Use pip freeze para criar o arquivo de requirements
```
pip freeze > dev-requirements.txt
```
Dessa forma as bibliotecas instaladas no ambiente virtual são obtidas de forma automática. 

## Erro na action criada na etapa de 'Integração contínua'

 A action 'actions/setup-python@v3' usada no arquivo '.github/workflows/main.yml' foi modificado quebrando a etapa 'Integração contínua'. 
 Para resolver o erro será necessário criar um arquivo vazio chamado 'requirements.txt' no repositório nessa etapa. 
