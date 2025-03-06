# 🌍 Classificador de Nacionalidade com Árvore de Decisão

Este projeto utiliza a biblioteca `scikit-learn` para criar um modelo de aprendizado de máquina baseado em **Árvore de Decisão**. O objetivo é prever a possível **nacionalidade** de uma pessoa com base em suas características físicas, como cor dos olhos, cabelo, altura e tom de pele.

## 🚀 Como Funciona?
1. O usuário insere suas características físicas.
2. O modelo de **Árvore de Decisão** faz a predição com base em dados pré-treinados.
3. O programa retorna a **probabilidade** de você pertencer a determinada nacionalidade.

---

## 🛠 Tecnologias Utilizadas

- `Python 3.x`
- `scikit-learn` (Machine Learning)
- `colorama` (Para saída colorida no terminal)
- `time` (Para efeitos visuais)

---

## 📥 Instalação e Configuração

1. **Clone o repositório:**
```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
```
2. **Entre no diretório:**
```bash
    cd seu-repositorio
```
3. **Crie um ambiente virtual (opcional):**
```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
```
4. **Instale as dependências:**
```bash
    pip install -r requirements.txt
```

---

## 🎯 Como Usar

1. **Execute o script:**
```bash
    python script.py
```
2. **Responda às perguntas sobre suas características físicas:**
   - Cor dos olhos (verdes, azuis, castanhos)
   - Cor do cabelo (castanhos, loiros, ruivos)
   - Altura (em cm ou metros)
   - Cor da pele (branca, amarela, negra)

3. **Resultado:** O modelo irá exibir a nacionalidade mais provável com a porcentagem de confiança!

---

## 🧠 Explicação do Modelo

O modelo é treinado com um conjunto de dados fictício que mapeia características físicas a diferentes nacionalidades. Ele usa uma **Árvore de Decisão** para prever a nacionalidade mais provável com base nas entradas do usuário.

### 🔹 Exemplo de Entrada e Saída
```
Qual a Cor dos Seus Olhos? ➜ azuis
Qual a Cor dos seus Cabelos? ➜ loiros
Qual é a sua Altura? ➜ 1.75
Qual é a Cor de Sua Pele? ➜ branca
```
**Saída esperada:**
```
Existe uma Probabilidade de 85% de Você ser/ter Descendência do País: PAÍSES NÓRDICOS
```

---

## ⚠️ Observação
Este programa é apenas uma simulação e **não deve ser usado para fins científicos ou antropológicos reais**. O modelo foi criado para fins educacionais e recreativos.

---

## 📌 Melhorias Futuras
- [ ] Adicionar mais características para melhorar a precisão.
- [ ] Expandir a base de dados para incluir mais nacionalidades.
- [ ] Criar uma interface gráfica para melhor experiência do usuário.

🚀 **Divirta-se explorando suas possíveis origens!** 🌎

