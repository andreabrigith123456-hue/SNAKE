# SNAKE
Proyecto: Desarrollo del Videojuego "Snake" en Python
Ofrecer una experiencia de juego fluida mientras se gestionan estructuras de datos dinámicas para el cuerpo de la serpiente. 
 
**Nombre:** Andrea Pumisacho
* **Materia:** LOGICA DE PROGRAMACION
* **Institución:** UNIVERSIDAD INTERNACIONAL DEL ECUADOR
* **Fecha:** Abril de 2026

**OBJETIVO**
Desarrollar una aplicación funcional del clásico juego "Snake" utilizando la librería **Pygame**. El proyecto busca aplicar conceptos de **desarollo de software, programacion basica**, diagramas y la gestión de estructuras de datos dinámicas (listas para el cuerpo) y el control de colisiones en tiempo real.

**FUNCIONALIDADES DEL CODIGO**

El software implementa las siguientes capacidades técnicas:

1. **Gestión de Movimiento** En la captura de eventos del teclado *KEYDOWN* para actualizar vectores de dirección en los ejes X e Y.
2. La lógica de Crecimiento Modelo donde el sistema inserta una nueva coordenada en la cabeza de la lista *cuerpo* y utiliza la función *pop()* para eliminar la cola, a menos que se detecte una colisión con la comida.
3. Detección de Colisiones,entorno para la vlidación de límites de la ventana (500x500).
    En la **autocolisión** que sera la verificación de superposición de coordenadas entre la cabeza y los segmentos del cuerpo.
4. El sistema ajusta los FPS *fps.tick* dinámicamente según el puntaje alcanzado (incremento de velocidad tras los primeros 3 puntos).
5. Interfaz de Usuario donde renderizado en tiempo real de gráficos 2D y visualización del puntaje en pantalla.

**REQUISITOS PARA SU INSTALACION**
Tener instalado **Python 3.12.0**.
Instalar la librería Pygame
  
