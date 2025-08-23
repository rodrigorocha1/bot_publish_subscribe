# Explorando o Padrão Publish/Subscribe com RabbitMQ: Construindo um Bot que mostra a disponibilidade de bikes para a cidade de curitiba.
## 1. 🎯 Objetivo do projeto  
O objetivo do projeto é explorar o padrão **Publish/Subscribe** utilizando o **RabbitMQ**, para construir um bot que fornece a quantidade de bicicletas disponíveis para a cidade de Curitiba, em **tempo real**.

---


## 2. 🛠️ Tecnologias utilizadas  

- 🐍 **Python**: Linguagem para desenvolvimento do bot.  
- 📡 **RabbitMQ**: Serviço de mensageria para implementação do padrão Publish/Subscribe.
- 🎮 **Discord**: Plataforma de comunicação para interação com o bot.
- 💬 **Telegram**: Alternativa de mensageria para interação com o bot.
- 🚲 **CityBikes API**: API que disponibiliza as estações com bikes disponíveis.  

---

## 3. 🏗️ Arquitetura da solução  

O bot será dividido em duas partes principais:  
1. O **Produtor** envia a requisição da API para uma fila do RabbitMQ.  
2. Os **Consumidores** (bots do **Telegram** e **Discord**) recebem a requisição da fila e retornam as informações para os usuários.  

[![Fluxo](https://github.com/rodrigorocha1/bot_publish_subscribe/blob/master/fig/animacao.gif?raw=true)](https://github.com/rodrigorocha1/bot_publish_subscribe/blob/master/fig/animacao.gif?raw=true)


---

### 3.1 – 📌 Requisitos funcionais  

- **RF1** - O sistema deve se conectar à API de bicicletas compartilhadas de Curitiba e coletar os dados em tempo real.  
- **RF2** - O sistema deve publicar as informações coletadas em uma fila do RabbitMQ.  
- **RF3** - O sistema deve seguir o padrão Publish/Subscribe, permitindo múltiplos consumidores simultâneos.  
- **RF4** - O bot do Discord deve consumir a fila e responder aos usuários com a quantidade de bicicletas disponíveis.  
- **RF5** - O bot do Telegram deve consumir a fila e responder aos usuários com a quantidade de bicicletas disponíveis.  
- **RF6** - O bot deve permitir que o usuário solicite informações em tempo real sobre bicicletas disponíveis em Curitiba.  

---

### 3.2 – ⚙️ Requisitos não funcionais  

- **RNF1** - As respostas do bot devem ser fornecidas em tempo real (latência < 2 segundos em média).  
- **RNF2** - A arquitetura deve suportar múltiplos consumidores e filas sem alteração no código do publisher.  
- **RNF3** - Todo o sistema deve ser empacotado em **Docker Compose** para fácil implantação em qualquer ambiente.  
- **RNF4** - O código deve ser modular, seguindo boas práticas de clean code e separação de responsabilidades.  

---

### 3.3 – 📐 Diagrama de Classes  

A organização do sistema segue a seguinte estrutura:  

- **Módulo `config`**: Responsável por gerenciar as credenciais de serviços externos.  
- **Módulo `conexao_api`**: Define o contrato de consulta à API de bicicletas.  
- **Módulo `mensageiro`**: Define o contrato de execução dos bots (Discord e Telegram).  
- **Classe `Produtor`**: Responsável por publicar (Publisher) no padrão Publish/Subscribe.  
- **Classe `Consumidor`**: Recebe mensagens da fila e envia para os bots de Telegram e Discord.  

[![Fluxo](https://github.com/rodrigorocha1/bot_publish_subscribe/blob/master/fig/diagrama_de_classe.png?raw=true)](https://github.com/rodrigorocha1/bot_publish_subscribe/blob/master/fig/diagrama_de_classe.png?raw=true)


---

### 3.4 – 🧩 Padrões de Projetos Utilizados  

- **Publish/Subscribe (Observer)** → O RabbitMQ faz o gerenciamento entre o produtor e consumidores.  
- **Strategy** → Permite o uso de diferentes bots que implementam a interface `IBots`.  
- **Princípio da Inversão da Dependência (DIP)** → Uso da interface `IBikesAPI` em vez de depender diretamente da implementação `BikesAPI`.  

---




## 4. Vídeo com a demonstração do projeto 
[![Assistir ao vídeo de demonstração do projeto](https://img.shields.io/badge/🎬%20Assistir%20ao%20vídeo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/UJc8KMvbApc)



[Link do reposítório](https://github.com/rodrigorocha1/bot_publish_subscribe)