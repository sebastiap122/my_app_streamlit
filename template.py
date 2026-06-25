import streamlit as st

# ══════════════════════════════════════════════════════════════
# Mercasazón · Streamlit
# Ficha 3387591 · SENA CTM Itagüí · 2026
# ══════════════════════════════════════════════════════════════

st.set_page_config(page_title="Mercasazón", page_icon="🛒", layout="wide")

# ── ESTILOS ──
st.markdown("""
<style>
.stApp {
    background-color: #f0f7f0;
    font-family: 'Segoe UI', sans-serif;
}
h1 {
    color: #2e7d32 !important;
}
h3 {
    color: #388e3c !important;
}
[data-testid="stMetricBlock"] {
    background-color: #ffffff;
    border-left: 5px solid #2e7d32;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}
[data-testid="stSidebar"] {
    background-color: #e8f5e9;
}
</style>
""", unsafe_allow_html=True)

# ── DATOS ──
datos = [
    {"id": 1,  "nombre": "Arroz x 500g",       "precio": 2800,  "categoria": "Granos"},
    {"id": 2,  "nombre": "Frijol x 500g",       "precio": 3500,  "categoria": "Granos"},
    {"id": 3,  "nombre": "Lenteja x 500g",      "precio": 3200,  "categoria": "Granos"},
    {"id": 4,  "nombre": "Banano x kg",         "precio": 1800,  "categoria": "Frutas"},
    {"id": 5,  "nombre": "Mango x kg",          "precio": 3400,  "categoria": "Frutas"},
    {"id": 6,  "nombre": "Naranja x kg",        "precio": 2200,  "categoria": "Frutas"},
    {"id": 7,  "nombre": "Agua x 600ml",        "precio": 1500,  "categoria": "Bebidas"},
    {"id": 8,  "nombre": "Jugo Hit x 300ml",    "precio": 2300,  "categoria": "Bebidas"},
    {"id": 9,  "nombre": "Papa x kg",           "precio": 1900,  "categoria": "Verduras"},
    {"id": 10, "nombre": "Zanahoria x kg",      "precio": 2100,  "categoria": "Verduras"},
    {"id": 11, "nombre": "Pechuga x kg",        "precio": 11500, "categoria": "Proteína"},
    {"id": 12, "nombre": "Huevos x 30 und",     "precio": 14500, "categoria": "Proteína"},
]

# ── SIDEBAR ──
st.sidebar.title("Filtros")
categoria = st.sidebar.selectbox("Categoría", ["Todas", "Granos", "Frutas", "Bebidas", "Verduras", "Proteína"])

# ── FILTRO ──
if categoria != "Todas":
    datos_filtrados = [d for d in datos if d["categoria"] == categoria]
else:
    datos_filtrados = datos

# ── BANNER ──
st.markdown("""
<div style="
    background-image: url('https://images.unsplash.com/photo-1542838132-92c53300491e?w=1200&q=80');
    background-size: cover;
    background-position: center;
    border-radius: 16px;
    padding: 60px 20px;
    text-align: center;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
">
    <div style="
        position: absolute; inset: 0;
        background: rgba(27, 94, 32, 0.72);
        border-radius: 16px;
    "></div>
    <div style="position: relative; z-index: 1;">
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@800&display=swap" rel="stylesheet">
        <h1 style="color:b; font-size:58px; margin:0; font-weight:800; font-family:'Playfair Display', serif; letter-spacing:2px; text-shadow: 2px 3px 8px rgba(0,0,0,0.4);">
            🛒 Mercasazón
        </h1>
        <p style="color:#c8e6c9; font-size:18px; margin-top:12px; margin-bottom:0;">
            Calidad, frescura y confianza en cada compra.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── MÉTRICAS ──
precios = [d["precio"] for d in datos_filtrados]

col1, col2, col3 = st.columns(3)
col1.metric("Total productos", len(datos_filtrados))
col2.metric("Precio máximo", f"${max(precios):,}" if precios else "$0")
col3.metric("Precio promedio", f"${int(sum(precios)/len(precios)):,}" if precios else "$0")

# ── TABLA ──
st.subheader("Registros")
st.dataframe(datos_filtrados, use_container_width=True)

# ── GRÁFICA ──
st.subheader("Estadísticas")
st.bar_chart(data={d["nombre"]: d["precio"] for d in datos_filtrados})

# ── FOOTER ──
st.divider()
st.caption("Domo ProopTech · SENA CTM Itagüí · 2026")