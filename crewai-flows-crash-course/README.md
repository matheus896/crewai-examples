
```markdown
# Configuração do Projeto

Este projeto requer a instalação de certas dependências para funcionar corretamente. Siga as instruções abaixo para configurar seu ambiente.

## Ambiente Conda

Para criar um ambiente conda com Python 3.12, use o seguinte comando:

```bash
conda create --name crewai-flows python=3.12
```

Para ativar o ambiente conda, use:

```bash
conda activate crewai-flows
```

## Virtualenv

Se preferir usar virtualenv, primeiro instale-o:

```bash
pip install virtualenv
```

Em seguida, crie um ambiente virtual com Python 3.12:

```bash
virtualenv -p python3.12 myenv
```

Ative o ambiente virtualenv com:

- No Windows:
  ```bash
  myenv\Scripts\activate
  ```
- No macOS/Linux:
  ```bash
  source myenv/bin/activate
  ```

## Instalando Dependências

Para instalar as dependências listadas no arquivo `requirements.txt`, use:

```bash
pip install -r requirements.txt
```
```
