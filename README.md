
# ✊✋✌️ Coddx Rock Paper Scissors - GUI Logic & Persistence

## 🧪 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-Library-blue?style=flat)
![JSON](https://img.shields.io/badge/Storage-JSON-yellow?style=flat)
![Standard Library](https://img.shields.io/badge/Built--in-Modules-green?style=flat)

## Preview

<div aligne="center">
	<img src="https://github.com/YisusDU/coddx_rock_paper_scissors_gui/blob/main/image/README/1769291746244.png" alt="Vista Juego piedra, papel o tijeras" />
</div>

## 📁 Overview

Este documento detalla la **arquitectura lógica y funcional** de **Coddx RPS**, una aplicación de escritorio que trasciende el simple juego para demostrar el manejo de estados y persistencia de datos local.

El sistema permite a los usuarios:**Interactuar** con una interfaz gráfica basada en eventos (Tkinter).

* **Competir** contra un oponente con lógica de selección pseudo-aleatoria.
* **Persistencia de Datos:** Mantener estadísticas globales que sobreviven al cierre de la aplicación.

Esta documentación incluye:

* **State Management:** Diferenciación entre puntajes de sesión y estadísticas históricas.
* **Data Persistence Strategy:** Implementación de serialización JSON para el Scoreboard.
* **GUI Orchestration:** Manejo de ventanas principales y secundarias (`Toplevel`).

> **Pregunta de reflexión:** En el proyecto anterior (Spotizer) la prioridad era el Layout. Aquí la prioridad es el Estado. ¿Cómo cambia esto la forma en que un usuario debe leer tu código?

---

## 🧭 System Overview

**Coddx RPS** opera bajo un modelo de **Programación Orientada a Objetos (OOP)**, donde una clase central orquestadora (`RockPaperScissorsGUI`) maneja tanto la renderización como las reglas del negocio.

### 🧠 Dual-Tier Score System

A diferencia de un juego básico, aquí implementamos dos capas de datos:

1. **Volatile Session:** Puntajes que se reinician al cerrar.
2. **Persistent Statistics:** Un "Libro Mayor" almacenado en disco que registra cada victoria, derrota y empate desde la creación del archivo.

### 🤖 Computer Logic

El oponente no es reactivo, sino determinista basado en el módulo `random`. La lógica de decisión reside en un método aislado para mantener la modularidad.

### 💾 Data Integrity

El sistema verifica la existencia de archivos locales antes de la carga, aplicando un manejo de excepciones para evitar errores de ejecución si el archivo `scoreboard.json` está corrupto o ausente.

> **Sources:**
>
> * `rock_paper_scissors_gui.py` (Líneas 189–209: Métodos de carga/guardado)

---

## 🏗️ Architecture & Component Mapping

El núcleo del proyecto es la clase `RockPaperScissorsGUI`, que actúa como el **Controlador** en un esquema simplificado:

1. **Initialization (`__init__`):** Define el estado inicial y carga los datos históricos.
2. **Game Loop (`play`):** El motor que procesa la entrada del usuario y dispara la actualización de la UI.
3. **Storage Interface (`save_scoreboard`):** La capa que comunica la lógica del juego con el sistema de archivos.

> **Pregunta de arquitectura:** Si decidieras cambiar JSON por una base de datos SQL en el futuro, ¿qué métodos específicos tendrías que refactorizar sin romper la interfaz visual?

---

## 🧰 Technology Stack and Project Structure

| Technology           | Purpose        | Implementation                |
| :------------------- | :------------- | :---------------------------- |
| **Python 3.x** | Core Engine    | Runtime & Logic               |
| **Tkinter**    | UI Framework   | Desktop Window Management     |
| **JSON**       | Data Format    | Persistent Scoreboard Storage |
| **OS Module**  | System Pathing | File checking & verification  |

### 🗂️ Project Structure

```text
coddx_rock_paper_scissors_gui/
├── rock_paper_scissors_gui.py   # Orquestador Principal (Clase y Lógica)
├── scoreboard.json              # Almacén de Datos (Generado en Runtime)
└── README.md                    # Documentación de alto nivel
```


## 🪟 Feature Spotlight: Persistent Scoreboard

El mayor desafío técnico resuelto en este código no es el juego en sí, sino la **persistencia**. Lograr que la experiencia del usuario no se pierda al cerrar el proceso es lo que separa un script básico de una aplicación real.

### 1. JSON Serialization

Se utiliza el formato **JSON** para estructurar los datos históricos. Esto no solo facilita la lectura por parte de la máquina, sino que permite que el programador (o el usuario curioso) pueda auditar los puntajes simplemente abriendo un archivo de texto plano.

### 2. Dashboard Dinámico

Al invocar el Scoreboard, la aplicación no solo muestra datos estáticos; genera una ventana secundaria (`Toplevel`) que realiza cálculos en tiempo real (como porcentajes de victoria) basándose en los datos crudos almacenados.

> **Sources:**
>
> * `rock_paper_scissors_gui.py` (Líneas 211–296: Lógica del Scoreboard)

---

## 📚 Relevant Source Files & Logic Map

Para navegar por la arquitectura del proyecto, utiliza este mapa de responsabilidades:

| File Path                                | Role                | Description                                                                                                                  |
| :--------------------------------------- | :------------------ | :--------------------------------------------------------------------------------------------------------------------------- |
| **`rock_paper_scissors_gui.py`** | 🧠**Brain**   | Contiene toda la lógica de Tkinter, el manejo de estados y el motor de reglas del juego.                                    |
| **`scoreboard.json`**            | 🗄️**Vault** | Almacena el historial de partidas en formato clave-valor, asegurando que los datos sobrevivan al ciclo de vida del programa. |

---

> [!NOTE]
> Puedes consultar la documentación completa y detallada  [- Aquí -](https://deepwiki.com/YisusDU/coddx_rock_paper_scissors_gui)
