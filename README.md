
# Introdução ao Tkinter

Tkinter é a biblioteca padrão do Python para criação de **interfaces gráficas (GUI)**.  
Ela permite desenvolver janelas, botões, campos de texto e outros componentes visuais sem a necessidade de instalar bibliotecas externas.

Apesar de simples, é amplamente utilizada em projetos educacionais e aplicações básicas, servindo como porta de entrada para o desenvolvimento de interfaces gráficas em Python.

Este repositório contém anotações iniciais e explicações básicas sobre o uso do Tkinter, organizadas como uma mini aula introdutória.

---

## Comandos básicos

```python
janela = tk.Tk()
janela.mainloop()
````

Esses dois comandos são fundamentais para qualquer aplicação Tkinter.

* `tk.Tk()` cria a **janela principal da aplicação**.
* `mainloop()` inicia o laço de execução da interface gráfica, mantendo a janela aberta e permitindo a interação do usuário.

Sem o `mainloop`, a janela é encerrada imediatamente após ser criada, fazendo a aplicação abrir e fechar instantaneamente.

Esses comandos formam a base de qualquer interface gráfica desenvolvida com Tkinter.

---

## Título da janela

```python
janela.title("Digite aqui o título da interface gráfica")
```

Define o texto exibido na barra superior da janela.
Esse título serve para identificar a aplicação e melhorar a apresentação visual da interface.

---

## Tamanho da janela

```python
janela.geometry("450x550+725+334")
```

Define o tamanho inicial e a posição da janela na tela.

* `450x550` representa a largura e a altura da janela.
* `+725+334` indica a posição inicial da janela nos eixos X e Y da tela.

Esses valores funcionam como coordenadas de posicionamento, controlando onde a janela será exibida ao iniciar a aplicação.

```python
janela.minsize(30, 100)
```

Define o tamanho mínimo permitido para a janela, impedindo que o usuário a reduza além desses valores.

```python
janela.maxsize(480, 550)
```

Define o tamanho máximo permitido para a janela, limitando o redimensionamento.

```python
janela.resizable(False, False)
```

Define se a janela pode ou não ser redimensionada pelo usuário.

* Primeiro parâmetro: largura
* Segundo parâmetro: altura

Quando definido como `False`, o redimensionamento é bloqueado, garantindo que o layout da interface permaneça fixo.

---

## Cor de fundo da janela

```python
janela.configure(bg="navajo white")
```

Define a cor de fundo da janela.
O Tkinter aceita nomes de cores predefinidos ou códigos hexadecimais.

Obs: No arquivo **coresTkinter.png** estão listadas diversas cores disponíveis para uso no Tkinter.

---

## Ícone da janela

```python
janela.iconbitmap("dedo_para_cima.ico")
```

Define o ícone exibido na barra de título da janela.

O arquivo deve estar no formato `.ico` e localizado no mesmo diretório do script ou com o caminho corretamente especificado.
Caso o ícone não apareça, normalmente o problema está no caminho ou no formato do arquivo.

---

## Transparência da janela

```python
janela.attributes("-alpha", 1)
```

Define o nível de transparência da janela.

* O valor varia entre `0` e `1`
* Quanto menor o valor, mais transparente a janela
* O valor `1` indica que a janela está totalmente opaca

Valores muito baixos tornam a janela quase invisível.

---

## Observações finais

Este material foi elaborado como uma forma de estudo inicial da biblioteca Tkinter, servindo como referência básica para consultas rápidas.

A organização do conteúdo tem como objetivo facilitar o entendimento dos principais comandos relacionados à criação e configuração da janela principal de uma aplicação gráfica em Python.

Este README pode ser expandido futuramente com exemplos práticos, imagens da interface, widgets adicionais e organização por módulos.

---

📌 **Status do repositório**: Em desenvolvimento
📚 **Objetivo**: Aprendizado e prática com Tkinter



