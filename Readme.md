# Colny

O Clony é um projeto realizado como um hobby, com a função de identificar arquivos duplicados dentro de um determinado diretório. Seu algoritmo é recursivo, o que significa que ele verifica todas as sub-rotas dentro do diretório informado e utiliza o hash dos binários de cada arquivo como base para identificar duplicatas, desconsiderando informações como nome e metadados, focando apenas no conteúdo em si.

Vale mencionar que em caso de variações mínimas entre dois arquivos, pode ser impossível para o Clony identificar a "quase cópia", já que os hashes dos arquivos serão diferentes e não haverá nenhum outro indício de que ambos os arquivos derivam de um arquivo em comum.

## Como Utilizar
1. Baixe o projeto como .zip ou execute um `git colne` no repositório
2. Caso tenha baixado, descompacte o diretório
3. Agora que você já tem o diretório de projeto, é só dar dois cliques no `main.py`
4. Após iniciada a execução, será necessário inserir a rota do diretório a ser vasculhado

OBS: É importante salientar que para executar o `git clone` é preciso ter o Git instalado. Da mesma forma, para rodar este programa, o seu computador deve ter o Python 3 devidamente instalado e configurado.

## Bibliotecas Usadas
- `os`: Utilizada para leitura e manipulação dos diretórios e arquivos do sistema.
- `hashlib`: Usada para a geração do hash dos binários de cada arquivo.

## Estrutura Interna

### Atributos
- `results`: Uma lista contendo todos os arquivos mapeados com a estrutura {path, hash}.
- `position`: Um valor inteiro que indica a posição do diretório que está sendo mapeado recursivamente.
- `origin`: Diretório inicial a partir do qual todo o mapeamento de diretórios e arquivos é realizado.
- `dir_list`: Lista contendo todos os diretórios e subdiretórios de dentro do diretório de origem.
- `file_list`: Lista contendo todos os arquivos de todos os diretórios e subdiretórios de dentro do diretório de origem.

### Métodos
- `_get_all_dirs(current_dir, dir_list)`: Recebe o diretório a ser listado e uma lista contendo todos os diretórios catalogados anteriormente. Atua de forma recursiva, identificando novos diretórios dentro do diretório atual e os insere na lista de diretórios mapeados, retornando a lista completa ao final do processo.
- `_get_all_files()`: Utiliza a lista de diretórios mapeados para iterar sobre cada diretório, extraindo os arquivos presentes em cada um deles e, em seguida, retornando uma lista contendo todos os arquivos encontrados.
- `_list_files()`: Itera sobre a lista de arquivos encontrados aplicando a função de hashing para obter o identificador de cada arquivo. É responsável por montar a lista final com os `results` e sua estrutura {path, hash}.
- `find_duplicate()`: É o único método público. Quando chamado, itera sobre a lista `results` para buscar elementos com o mesmo hash, indicando duplicação de arquivos. Torna-se seguro retornar o caminho de cada um dos arquivos com o mesmo hash.

## Detalhes Adicionais
- A geração do hash é realizada através de um buffer de 64 KB para evitar o estouro da RAM em caso de arquivos grandes.
- Ainda é possível ocorrer um estouro de memória em caso de uma estrutura de diretório muito aninhada ou com muitos arquivos, uma vez que todos os nomes de diretórios, arquivos e resultados são armazenados em memória.
- Dependendo do número de subdiretórios, é possível que o Python retorne um erro de `RecursionError: maximum recursion depth exceeded while calling a Python object`.
- Arquivos triplicados não são exibidos de forma conjunta, mas sim em três pares de dois, o que é um problema a ser tratado no longo prazo.

## Próximas Etapas
- [ ] Tratar a exibição de arquivos triplicados ou em maior número.
- [ ] Permitir a visualização dos arquivos.
- [ ] Tratar o possível estouro de memória.
- [ ] Resolver o problema do limite de recursividade.
