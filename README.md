# Pêndulo Duplo com Manim

Este projeto implementa a simulação de um **pêndulo duplo** utilizando a biblioteca **Manim**.

## 📌 Sobre o Projeto
O pêndulo duplo é um sistema dinâmico conhecido pelo seu comportamento caótico. Neste projeto, utilizamos **Manim** para visualizar sua dinâmica em um espaço 3D.

## 📂 Estrutura dos Dados (JSON)
A simulação pode exportar dados em formato **JSON**, contendo informações sobre a posição e velocidade dos pêndulos ao longo do tempo. Abaixo está um exemplo de estrutura JSON utilizada para registrar os dados da simulação:

```json

{
    "g": 9.8,        // Aceleração da gravidade (m/s²)
    "L1": 2,         // Comprimento da primeira haste do pêndulo (metros)
    "L2": 2,         // Comprimento da segunda haste do pêndulo (metros)
    "M1": 1,         // Massa da primeira esfera (kg)
    "M2": 2,         // Massa da segunda esfera (kg)
    "dt": 0.05,      // Intervalo de tempo para a simulação (segundos)
    "theta1": 1.5708, // Ângulo inicial do primeiro pêndulo (radianos, π/2)
    "theta2": 1.5708, // Ângulo inicial do segundo pêndulo (radianos, π/2)
    "omega1": 0,     // Velocidade angular inicial do primeiro pêndulo (rad/s)
    "omega2": 0      // Velocidade angular inicial do segundo pêndulo (rad/s)
}


```

### 🔍 Explicação dos Campos
- **tempo**: Lista com os instantes de tempo em que os dados foram coletados.
- **theta1**: Lista com os ângulos (em radianos) do primeiro pêndulo ao longo do tempo.
- **theta2**: Lista com os ângulos do segundo pêndulo ao longo do tempo.
- **omega1**: Lista com as velocidades angulares do primeiro pêndulo.
- **omega2**: Lista com as velocidades angulares do segundo pêndulo.

Esse formato de dados permite fácil análise e visualização do comportamento do sistema em softwares como **Matplotlib** ou **Pandas**.

## 🚀 Como Executar
### 📌 Pré-requisitos
Antes de rodar o código, instale o Manim e as dependências necessárias:

```sh
pip install manim numpy
```

### 📌 Rodando a Simulação
Para executar a animação, basta rodar o script:

```sh
manim -pql nome_do_arquivo.py
```

## 📖 Referências
- [Documentação do Manim](https://docs.manim.community/)

---

