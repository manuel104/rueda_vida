# code
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Definir las áreas y sus preguntas específicas
areas = {
    "Área 1": [
        "Pregunta 1.1: ¿Pregunta relacionada con Área 1?",
        "Pregunta 1.2: ¿Pregunta relacionada con Área 1?"
    ],
    "Área 2": [
        "Pregunta 2.1: ¿Pregunta relacionada con Área 2?",
        "Pregunta 2.2: ¿Pregunta relacionada con Área 2?"
    ],
    "Área 3": [
        "Pregunta 3.1: ¿Pregunta relacionada con Área 3?",
        "Pregunta 3.2: ¿Pregunta relacionada con Área 3?"
    ],
    "Área 4": [
        "Pregunta 4.1: ¿Pregunta relacionada con Área 4?"
    ],
    "Área 5": [
        "Pregunta 5.1: ¿Pregunta relacionada con Área 5?",
        "Pregunta 5.2: ¿Pregunta relacionada con Área 5?"
    ],
    "Área 6": [
        "Pregunta 6.1: ¿Pregunta relacionada con Área 6?"
    ],
    "Área 7": [
        "Pregunta 7.1: ¿Pregunta relacionada con Área 7?"
    ],
    "Área 8": [
        "Pregunta 8.1: ¿Pregunta relacionada con Área 8?"
    ],
}

# Diccionario para guardar las respuestas
respuestas = {}

def mostrar_resultados():
    # Calcular puntajes por área
    puntajes_por_area = {area: 0 for area in areas.keys()}
    
    for area, preguntas in areas.items():
        for pregunta in preguntas:
            # Obtener el número de la pregunta (esto lo asumimos a partir del texto de la pregunta)
            pregunta_num = preguntas.index(pregunta) + 1
            if respuestas.get(f"Pregunta {pregunta_num}", 0) == 1:  # Si es "Sí"
                if area == "Área 8":
                    puntajes_por_area[area] += 2  # Cada "Sí" en Área 8 vale 2 puntos
                else:
                    puntajes_por_area[area] += 1

        # Asegurar que los valores no superen el máximo (10 por área)
        puntajes_por_area[area] = min(puntajes_por_area[area], 10)

    # Crear el gráfico de radar
    labels = list(puntajes_por_area.keys())
    valores = list(puntajes_por_area.values())
    valores.append(valores[0])  # Repetir el primer valor para cerrar el círculo

    angulos = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})
    ax.plot(angulos, valores, 'o-', linewidth=2, label="Resultados")
    ax.fill(angulos, valores, alpha=0.25)

    ax.set_yticks(range(0, 11, 2))  # Escala de 0 a 10
    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(labels)
    ax.set_title("Resultados por Área", size=16, weight='bold')
    ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
    st.pyplot(fig)

# Crear la interfaz con Streamlit
st.title("Encuesta de 75 Preguntas")

# Agregar preguntas
for area, preguntas in areas.items():
    st.subheader(area)
    for pregunta in preguntas:
        respuesta = st.radio(pregunta, options=["Sí", "No"], key=f"Pregunta {preguntas.index(pregunta) + 1}")
        respuestas[f"Pregunta {preguntas.index(pregunta) + 1}"] = 1 if respuesta == "Sí" else 0

# Botón para mostrar resultados
if st.button("Ver Resultados"):
    mostrar_resultados()
