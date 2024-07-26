# Algoritmos e Estrutura de Dados I | FURG
Repositório da disciplina de "Algoritmos e Estrutura de Dados I" do curso de bacharelado em Sistemas de Informação na FURG.

----------------------------------------------------------------------------------------------

# Comandos Básicos do Linux

## Navegação e Gerenciamento de Arquivos

- `ls` - Lista os arquivos e diretórios no diretório atual.
- `cd [diretório]` - Muda para o diretório especificado.
- `pwd` - Exibe o caminho completo do diretório atual.
- `cp [origem] [destino]` - Copia arquivos ou diretórios.
- `mv [origem] [destino]` - Move ou renomeia arquivos ou diretórios.
- `rm [arquivo]` - Remove arquivos.
- `rm -r [diretório]` - Remove diretórios e seu conteúdo recursivamente.
- `mkdir [diretório]` - Cria um novo diretório.
- `rmdir [diretório]` - Remove um diretório vazio.

## Visualização de Arquivos

- `cat [arquivo]` - Exibe o conteúdo de um arquivo.
- `more [arquivo]` - Exibe o conteúdo de um arquivo página por página.
- `less [arquivo]` - Exibe o conteúdo de um arquivo com navegação mais avançada.
- `head [arquivo]` - Exibe as primeiras linhas de um arquivo.
- `tail [arquivo]` - Exibe as últimas linhas de um arquivo.

## Manipulação de Texto

- `grep [padrão] [arquivo]` - Procura por um padrão dentro de arquivos.
- `sed [opções]` - Editor de fluxo para realizar transformações em texto.
- `awk [opções]` - Linguagem de programação para processamento de texto.

## Permissões

- `chmod [permissões] [arquivo]` - Altera as permissões de arquivos ou diretórios.
- `chown [usuário]:[grupo] [arquivo]` - Altera o proprietário e grupo de arquivos ou diretórios.

## Processos e Sistema

- `ps` - Exibe informações sobre processos em execução.
- `top` - Mostra processos em tempo real.
- `kill [PID]` - Envia um sinal para terminar um processo.
- `df` - Exibe o uso do espaço em disco.
- `du` - Exibe o uso de espaço em disco por arquivos e diretórios.

## Rede

- `ping [endereço]` - Verifica a conectividade com um endereço.
- `ifconfig` ou `ip a` - Exibe informações de interfaces de rede.
- `curl [URL]` - Faz uma requisição para um URL.

## Arquivos e Pacotes

- `tar -cvf [arquivo.tar] [diretório]` - Cria um arquivo tar.
- `tar -xvf [arquivo.tar]` - Extrai um arquivo tar.
- `gzip [arquivo]` - Comprime um arquivo.
- `gunzip [arquivo.gz]` - Descomprime um arquivo gzip.
- `apt-get install [pacote]` - Instala um pacote (para distribuições baseadas no Debian).
- `yum install [pacote]` - Instala um pacote (para distribuições baseadas no Red Hat).

## Git

- `git init` - Inicializa um repositório Git.
- `git clone [URL]` - Clona um repositório remoto.
- `git add [arquivo]` - Adiciona arquivos para o próximo commit.
- `git commit -m "mensagem"` - Cria um commit com uma mensagem.
- `git push` - Envia commits para o repositório remoto.
- `git pull` - Atualiza o repositório local com mudanças do remoto.
