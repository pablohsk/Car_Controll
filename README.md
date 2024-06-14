# Norktown Carford - README
Este projeto consiste em um sistema de gerenciamento de carros e proprietários, desenvolvido com Flask. Abaixo, você encontrará detalhes sobre a estrutura do projeto, suas funcionalidades, configuração e como executar localmente.

<details>
  <summary><b>Estrutura do Projeto</b></summary>
  <ul>
    <li>
      <details>
        <summary><b>norktown_carford</b></summary>
        <ul>
          <li>
            <details>
              <summary><b>app</b></summary>
              <ul>
                <li><code>__init__.py</code></li>
                <li><code>config.py</code></li>
                <li><code>config_test.py</code></li>
                <li>
                  <details>
                    <summary><b>models</b></summary>
                    <ul>
                      <li><code>__init__.py</code></li>
                      <li><code>car.py</code></li>
                      <li><code>owner.py</code></li>
                      <li><code>user.py</code></li>
                    </ul>
                  </details>
                </li>
                <li>
                  <details>
                    <summary><b>dtos</b></summary>
                    <ul>
                      <li><code>__init__.py</code></li>
                      <li><code>car_dto.py</code></li>
                      <li><code>owner_dto.py</code></li>
                    </ul>
                  </details>
                </li>
                <li>
                  <details>
                    <summary><b>controllers</b></summary>
                    <ul>
                      <li><code>__init__.py</code></li>
                      <li><code>car_controller.py</code></li>
                      <li><code>owner_controller.py</code></li>
                      <li><code>user_controller.py</code></li>
                    </ul>
                  </details>
                </li>
                <li>
                  <details>
                    <summary><b>views</b></summary>
                    <ul>
                      <li><code>__init__.py</code></li>
                      <li><code>car_view.py</code></li>
                      <li><code>owner_view.py</code></li>
                      <li><code>user_view.py</code></li>
                    </ul>
                  </details>
                </li>
                <li>
                  <details>
                    <summary><b>tests</b></summary>
                    <ul>
                      <li><code>__init__.py</code></li>
                      <li><code>test_car.py</code></li>
                      <li><code>test_owner.py</code></li>
                      <li><code>test_user.py</code></li>
                    </ul>
                  </details>
                </li>
              </ul>
            </details>
          </li>
          <li><code>docker-compose.yml</code></li>
          <li><code>Dockerfile</code></li>
          <li><code>requirements.yml</code></li>
          <li><code>wait-for-it.sh</code></li>
          <li><code>run.py</code></li>
        </ul>
      </details>
    </li>
  </ul>
</details>

## Funcionalidades
O sistema oferece diversas funcionalidades, descritas abaixo:

### Funcionalidades Principais
#### 1. Gestão de Carros
- **Adicionar Carro:** Adiciona um novo carro ao sistema.
- **Obter Carro:** Recupera informações de um carro específico.
- **Atualizar Carro:** Atualiza os dados de um carro.
- **Excluir Carro:** Remove um carro do sistema.

#### 2. Gestão de Proprietários
- **Adicionar Proprietário:** Adiciona um novo proprietário ao sistema.
- **Obter Proprietário:** Recupera informações de um proprietário específico.
- **Atualizar Proprietário:** Atualiza os dados de um proprietário.
- **Excluir Proprietário:** Remove um proprietário do sistema (desde que não possua carros).

#### 3. Autenticação de Usuários
- **Registrar Usuário:** Cria uma nova conta de usuário.
- **Login de Usuário:** Autentica um usuário e retorna um token JWT.

## Configurações
### Requisitos do Ambiente
- Python 3.x instalado.
- PostgreSQL instalado e configurado.
- Docker e Docker Compose instalados.

### Configuração do Ambiente de Desenvolvimento
1. Clone o repositório do projeto do GitHub:
    ```bash
    git clone https://github.com/seu-usuario/seu-projeto.git
    cd seu-projeto
    ```

2. Crie um ambiente virtual Python e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    ```

3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados PostgreSQL:
    - Abra o arquivo `config.py` em `app/config.py`.
    - Verifique as configurações em `SQLALCHEMY_DATABASE_URI` e ajuste conforme necessário, incluindo o nome do banco de dados, usuário e senha.
    - Certifique-se de que o PostgreSQL esteja em execução e acessível.

5. Utilize Docker Compose para iniciar os serviços:
    ```bash
    docker-compose up --build
    ```

## Execução do Servidor
### Para iniciar o servidor Flask, execute:
```bash
python run.py
```

## Endpoints
A seguir estão os endpoints disponíveis neste projeto:

### Adicionar Carro

```
Método: POST
URL: /cars
Descrição: Adiciona um novo carro ao sistema.
```

### Obter Carro


```
Método: GET
URL: /cars/<int:car_id>
Descrição: Retorna os detalhes de um carro específico.
```

### Atualizar Carro


```
Método: PUT
URL: /cars/<int:car_id>
Descrição: Atualiza os dados de um carro existente.
```

### Excluir Carro


```
Método: DELETE
URL: /cars/<int:car_id>
Descrição: Remove um carro do sistema.
```

### Adicionar Proprietário


```
Método: POST
URL: /owners
Descrição: Adiciona um novo proprietário ao sistema.
```

### Obter Proprietário

```
Método: GET
URL: /owners/<int:owner_id>
Descrição: Retorna os detalhes de um proprietário específico.
```

### Atualizar Proprietário


```
Método: PUT
URL: /owners/<int:owner_id>
Descrição: Atualiza os dados de um proprietário existente.
```
### Excluir Proprietário

```
Método: DELETE
URL: /owners/<int:owner_id>
Descrição: Remove um proprietário do sistema (desde que não possua carros).
```

### Registrar Usuário


```
Método: POST
URL: /users/register
Descrição: Cria uma nova conta de usuário.
```

### Login de Usuário


```
Método: POST
URL: /users/login
Descrição: Autentica um usuário e retorna um token JWT.
```

## Desenvolvedor
Este projeto foi desenvolvido por Pablo Fidelis Dias. Para mais detalhes, consulte o link: https://github.com/pablohsk/Car_Controll.


Qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato. Obrigado por utilizar o Norktown Carford!

<!-- Me contrata! -->
