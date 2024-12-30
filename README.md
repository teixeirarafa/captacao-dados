<h1 align="center">
    Construção de mecanismos de captação de dados
</h1>


# :pushpin: Lista de Conteúdo
* [Sobre](#recycle-sobre)
* [Tecnologias Utilizadas](#clipboard-tecnologias-utilizadas)
* [Licença](#scroll-licença)

# :recycle: Sobre
Mecanismo de extração de dados capaz de realizar Web Scrapping da seção de artigos científicos de Inteligência Artificial do Arxiv (ou seja, https://arxiv.org/list/cs.AI/recent) e armazenar alguns dados obtidos em um arquivo do tipo CSV.

# :clipboard: Tecnologias Utilizadas
* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
* [UV](https://docs.astral.sh/uv/)
* [Ruff](https://docs.astral.sh/ruff/)
* [Pre Commit](https://pre-commit.com/)
* [Bumpversion](https://github.com/peritus/bumpversion)

# :desktop_computer: Instalação e Execução
**Antes de iniciar, é necessário ter o [Python](https://www.python.org/) e uma ferramenta de empacotamento, como o [UV](https://docs.astral.sh/uv/) baixado na máquina**

## Comando para clonar o repositório:
```bash
  #Para clonar o projeto
  git clone https://github.com/teixeirarafa/captacao-dados.git
```
## Para rodar a parte do servidor:
```bash
  #Baixar as depêndencias e executar o script
  uv run web_scrapping.py
```

O arquivo **articles-arxiv.csv** será gerado

# :scroll: Licença
Este projeto está sob a [LICENÇA](https://opensource.org/licenses/MIT) do MIT

version = "1.0.0"
