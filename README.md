# Atividade Prática: Desenvolvimento Guiado por Testes (TDD)

Este projeto é uma atividade prática para a disciplina de Tópicos Especiais em Web, focada em aplicar os conceitos de Desenvolvimento Guiado por Testes (TDD) para construir um módulo de pontuação de fidelidade em Python.

## 🎯 Objetivo

O objetivo é seguir o ciclo **Red-Green-Refactor** para implementar, passo a passo, as regras de negócio de um programa de fidelidade, garantindo que cada nova funcionalidade seja introduzida apenas após a criação de um teste que falhe.

## 🛠️ Requisitos

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)

## ⚙️ Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd AtividadePraticaTDD
    ```

2.  **Instale as dependências:**
    O único pacote externo necessário é o `pytest` para uma execução de testes mais limpa e informativa.
    ```bash
    pip install pytest
    ```

## 🚀 Como Executar os Testes

Todos os testes estão localizados no diretório `src/` e são projetados para serem executados com o `pytest`.

Para rodar a suíte de testes, execute o seguinte comando a partir da **raiz do projeto** (`AtividadePraticaTDD/`):

```bash
python -m pytest -v
```

-   A flag `-v` (verbose) exibe um relatório detalhado de quais testes passaram (`PASSED`) e quais falharam (`FAILED`).

## 📂 Estrutura do Projeto

```
.
├── pytest.ini            # Arquivo de configuração do Pytest
├── README.md             # Este arquivo
└── src/
    ├── fidelidade.py     # Código de produção (a ser criado/modificado)
    └── test_fidelidade.py  # Código de testes
```

-   **`test_fidelidade.py`**: Contém os casos de teste para cada regra de negócio.
-   **`fidelidade.py`**: Contém a função `calcular_pontos` que implementa a lógica do programa.
-   **`pytest.ini`**: Configura o `pytest` para encontrar os testes automaticamente no diretório `src`.

## 🔄 Fluxo TDD Aplicado

O desenvolvimento segue estritamente o ciclo:

1.  **RED**: Escrever um novo teste em `test_fidelidade.py` para uma funcionalidade que ainda não existe. Rodar `python -m pytest -v` e ver o teste falhar (vermelho).
2.  **GREEN**: Escrever o mínimo de código possível em `fidelidade.py` para fazer o novo teste passar. Rodar `python -m pytest -v` e ver todos os testes passarem (verde).
3.  **REFACTOR**: Analisar o código em `fidelidade.py` e `test_fidelidade.py` em busca de melhorias, como remover duplicação, melhorar a clareza e simplificar a lógica, sem alterar o comportamento (os testes devem continuar passando).
