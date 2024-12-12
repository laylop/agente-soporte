# Agente Soporte

## Descripción del Proyecto

**Agente Soporte** es una aplicación basada en inteligencia artificial diseñada para brindar soporte automatizado y personalizado a los usuarios de una tienda de tecnología. Utilizando la API de **OpenAI** y desarrollada con **Streamlit**, esta solución permite a los usuarios recibir respuestas automáticas en tiempo real a sus preguntas sobre productos, órdenes, entregas, y más.

El bot aprovecha el poder de **GPT-3** (OpenAI) para generar respuestas precisas, proporcionando una experiencia de soporte fluida y eficiente para los usuarios.

## Características

- **Soporte automático**: El bot responde a preguntas comunes sobre productos, pedidos y otros temas relacionados con la tienda.
- **Interfaz de usuario intuitiva**: Utiliza **Streamlit** para crear una interfaz sencilla y atractiva.
- **Generación de respuestas con OpenAI**: Se integra con la API de **OpenAI** para generar respuestas contextuales y naturales.
- **Memoria de conversaciones**: Opcionalmente, el sistema puede almacenar el historial de conversaciones, mejorando la interacción con los usuarios a través de un almacenamiento en memoria.
- **Escalabilidad**: Fácil de ampliar para incluir más características, como integración con bases de datos o soporte en múltiples idiomas.

## Tecnologías Utilizadas

- **Streamlit**: Framework de Python para construir aplicaciones web interactivas de manera rápida y sencilla.
- **OpenAI (GPT-3)**: Modelo de lenguaje natural utilizado para generar respuestas automáticas.
- **Python**: Lenguaje de programación utilizado para el desarrollo de la lógica principal del bot.
- **Redis** (Opcional): Base de datos en memoria para almacenar las interacciones y mejorar la memoria del bot.
- **API de OpenAI**: Se usa para generar las respuestas automatizadas que el bot ofrece.

## Requisitos

Asegúrate de tener las siguientes dependencias instaladas para ejecutar el proyecto:

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu-usuario/agente-soporte.git
   cd agente-soporte
   ```
