# 📖 Sócrates Bot

Fruto de reflexões da disciplina "**LabTec Cultura Digital**", do [Curso de Filosofia](https://ead.unisinos.br/cursos-graduacao/filosofia) da UNISINOS, ministrada em 2025/1 pela [Profa. Me. Tatiana Costa Leite](http://lattes.cnpq.br/6897855276768211), este projeto consiste em um chatbot de **Inteligência Artificial** que, mimetizando a persona de **Sócrates**, proporciona ao usuário um instigante diálogo com o filósofo! 🤔

<div align="center">
  <img style="max-width: 100%; height: auto;" src="assets/socrates.jpg" />
  <p>
    <i>Recorte de "A Morte de Sócrates", de Jacques-Louis David. Uma representação clássica da coragem intelectual diante da injustiça. Um lembrete atemporal sobre o impacto transformador das ideias e da busca pela verdade, valores que também guiam a inovação tecnológica.</i>
  </p>
</div>

# 🚀 Funcionalidades

- **Chatbot Interativo:** 🤖 Ferramenta poderosa para estimular o pensamento crítico e a reflexão filosófica.
- **Modelo Inteligente:** 🧠 Utilização do modelo GPT-4o da OpenAI, levando a respostas mais coerentes.
- **Interface Amigável:** 🎨 Interação através de uma interface gráfica minimalista e visualmente agradável.

# 🤗 Hugging Face

Para facilitar a experimentação, o projeto também se encontra disponível na plataforma Hugging Face, permitindo que qualquer pessoa possa interagir com o chatbot de maneira eficiente, sem necessidade de instalação local. Para tanto, basta acessar [**este link**](https://huggingface.co/spaces/germanocastanho/socrates-bot) e começar a filosofar com Sócrates! 💭

# ✅ Pré-requisitos

- Python 3.12 ou superior, disponível através do [**site oficial**](https://www.python.org/downloads/).
- Chave API da OpenAI, acessível através da [**plataforma**](https://platform.openai.com/login).
- Arquivo `.env` com a variável `OPENAI_API_KEY` configurada.

# 🛠️ Instalação Local

```bash
# Clone o repositório
git clone https://github.com/germanocastanho/socrates-bot.git

# Acesse o diretório
cd socrates-bot

# Configure um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o script "demo.py"
python3 demo.py
```

# 📜 Software Livre

Distribuído sob a [Licença GPLv3](LICENSE), garantindo liberdade de uso, modificação e redistribuição do software, desde que preservadas estas liberdades em quaisquer versões derivadas. Utilizando ou contribuindo, você apoia a filosofia de **software livre** e auxilia na construção de um ambiente tecnológico libertário! ✊
