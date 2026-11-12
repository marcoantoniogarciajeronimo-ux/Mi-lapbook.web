from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conceptos = [
        {
            "nombre": "HTML",
            "icono": "📄",
            "descripcion": "HTML significa Lenguaje de Marcado de Hipertexto. Es el esqueleto de cualquier página web: define qué elementos hay en ella, como títulos, párrafos, imágenes, enlaces, listas y botones. Sin HTML no hay contenido que mostrar.",
            "puntos": [
                "Significa HyperText Markup Language",
                "Proporciona la estructura del contenido",
                "Usa etiquetas: <h1>, <p>, <img>, <a>, <ul>",
                "No es un lenguaje de programación, sino de marcado",
                "Todos los navegadores lo interpretan para mostrar información al usuario"
            ]
        },
        {
            "nombre": "CSS",
            "icono": "🎨",
            "descripcion": "CSS significa Hojas de Estilo en Cascada. Se encarga de la apariencia y el diseño: colores, tipografías, tamaños, espaciados, fondos y cómo se organizan los elementos en pantalla. Convierte una estructura simple en algo visualmente atractivo.",
            "puntos": [
                "Significa Cascading Style Sheets",
                "Separa el contenido de su presentación visual",
                "Controla colores, fuentes, márgenes y diseños",
                "Permite crear diseños responsivos que se adaptan a cualquier pantalla",
                "Facilita mantener el mismo estilo en todo tu sitio web"
            ]
        },
        {
            "nombre": "JavaScript",
            "icono": "⚡",
            "descripcion": "JavaScript es el único lenguaje de programación que funciona de forma nativa en el navegador. Le da vida a tus páginas: puedes responder a clics, validar formularios, crear animaciones, cargar información sin recargar la página y mucho más.",
            "puntos": [
                "Es un lenguaje de programación completo",
                "Agrega interactividad y lógica a la web",
                "Responde a eventos: clics, teclado, desplazamiento",
                "Funciona tanto en el navegador como en el servidor (con Node.js)",
                "Junto con HTML y CSS, es una de las tecnologías fundamentales de la web"
            ]
        },
        {
            "nombre": "SQL",
            "icono": "🗄️",
            "descripcion": "SQL significa Lenguaje de Consulta Estructurado. Es el estándar para comunicarse con bases de datos relacionales: guardas, buscas, modificas y eliminas información. Casi todas las aplicaciones modernas usan SQL para almacenar datos de forma organizada y segura.",
            "puntos": [
                "Significa Structured Query Language",
                "Permite crear, leer, actualizar y borrar datos (CRUD)",
                "Se usa en sistemas como MySQL, PostgreSQL y SQLite",
                "Organiza la información en tablas con filas y columnas",
                "Es indispensable para aplicaciones que necesitan guardar información de usuarios"
            ]
        },
        {
            "nombre": "Jinja2",
            "icono": "🌹",
            "descripcion": "Jinja2 es el motor de plantillas más popular para Python y Flask. Te permite escribir plantillas con estructura HTML y luego insertar valores dinámicos desde tu código Python. Así reutilizas diseños y generas páginas de forma automática.",
            "puntos": [
                "Es un motor de plantillas para Python",
                "Permite mezclar HTML con variables y lógica",
                "Usa sintaxis sencilla: {{ variable }} y {% instrucciones %}",
                "Genera código HTML final que el navegador entiende",
                "Trabaja perfectamente con Flask para crear sitios web dinámicos"
            ]
        }
    ]
    return render_template('index.html', conceptos=conceptos)

if __name__ == "__main__":
    app.run(debug=True)

