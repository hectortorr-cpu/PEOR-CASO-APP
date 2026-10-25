import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA E IDENTIDAD VISUAL PAF
# ---------------------------------------------------------
st.set_page_config(
    page_title="Evaluador de Peores Casos y Protocolos APS - PAF",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo visual en modo oscuro tecnológico (Azul Marino, Verde Esmeralda y Amarillo Dorado)
st.markdown("""
<style>
    .main { background-color: #0a192f; color: #e6f1ff; }
    .stApp { background-color: #0a192f; }
    h1, h2, h3 { color: #00e676 !important; font-family: 'Segoe UI', sans-serif; }
    .stButton>button { background-color: #00e676; color: #0a192f; font-weight: bold; border-radius: 8px; border: none; padding: 10px 24px; }
    .stButton>button:hover { background-color: #ffd54f; color: #0a192f; }
    .card { background-color: rgba(16, 36, 64, 0.8); padding: 20px; border-radius: 12px; border: 1px solid #00e676; margin-bottom: 20px; }
    .gold-card { background-color: rgba(16, 36, 64, 0.8); padding: 20px; border-radius: 12px; border: 1px solid #ffd54f; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ Evaluador de Peores Casos y Generador de Protocolos APS")
st.subheader("Innovación con Propósito | Llenado Aséptico Farmacéutico (OMS TRS 1044 / EU GMP Anexo 1 / FDA)")

# ---------------------------------------------------------
# NAVEGACIÓN Y MENÚ
# ---------------------------------------------------------
st.sidebar.title("📌 Menú Principal")
opcion = st.sidebar.radio(
    "Seleccione un Módulo:",
    [
        "1. Diagnóstico de Prerrequisitos (Go / No-Go)",
        "2. Evaluador de Peores Casos (Worst-Case)",
        "3. Generador de Borrador de Protocolo",
        "4. Cálculo de Volumen y Headspace",
        "5. Guía de Instalación en Celular (PWA) y PC"
    ]
)

# ---------------------------------------------------------
# MÓDULO 1: DIAGNÓSTICO DE PRERREQUISITOS (GO / NO-GO)
# ---------------------------------------------------------
if opcion == "1. Diagnóstico de Prerrequisitos (Go / No-Go)":
    st.header("📋 Módulo 1: Lista de Verificación de Prerrequisitos")
    st.write("Evalúe si la planta cuenta con todos los recursos críticos listos antes de dar inicio a la Simulación del Proceso Aséptico (APS / Media Fill).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏬 Servicios Críticos e Instalaciones")
        hvac = st.checkbox("Sistemas HVAC calificados (Grados A-D, presión 10-15 Pa, flujo UDAF 0.36-0.54 m/s)")
        wfi = st.checkbox("Agua WFI calificada y conforme en endotoxinas y biocarga")
        gases = st.checkbox("Vapor limpio y aire/gases estériles con filtros de 0.2 µm validados")
        
        st.markdown("### ⚙️ Equipos e Instrumentación")
        iq_oq = st.checkbox("Calificación IQ/OQ vigente de lavadora, túnel, llenadora y agrafadora")
        depiro = st.checkbox("Túnel de depirogenación validado con reducción ≥ 3-log")
        sip_cip = st.checkbox("Ciclos CIP/SIP de tuberías y agujas validados")

    with col2:
        st.markdown("### 👥 Personal y Vestimenta")
        gowning = st.checkbox("Operadores con calificación de gowning vigente (0 UFC en 3 muestras consecutivas)")
        aseptic_tech = st.checkbox("Técnicas asépticas y movimientos en Grado A/B calificados")
        
        st.markdown("### 🧫 Microbiología y Metrología")
        tsb_free = st.checkbox("Caldo Soja Triptona (SCDM/TSB) certificado TSE/BSE-Free y estéril")
        gpt = st.checkbox("Promoción de Crecimiento (GPT USP <71> + aislados nativos) con inóculo < 100 UFC")
        calib = st.checkbox("Sensores e instrumentos de medición calibrados con trazabilidad")

    st.markdown("---")
    criterios = [hvac, wfi, gases, iq_oq, depiro, sip_cip, gowning, aseptic_tech, tsb_free, gpt, calib]
    puntuacion = sum(criterios)
    total = len(criterios)
    
    st.markdown("### 📊 Dictamen DecisionAL")
    if puntuacion == total:
        st.success(f"✅ **ESTADO: GO ({puntuacion}/{total})** - Todos los prerrequisitos están cumplidos al 100%. Se habilita el inicio de la simulación de proceso.")
    else:
        st.error(f"❌ **ESTADO: NO-GO ({puntuacion}/{total})** - Faltan {total - puntuacion} prerrequisitos obligatorios por completar antes de iniciar.")

# ---------------------------------------------------------
# MÓDULO 2: EVALUADOR MINUCIOSO DE PEORES CASOS
# ---------------------------------------------------------
elif opcion == "2. Evaluador de Peores Casos (Worst-Case)":
    st.header("🎯 Módulo 2: Motor de Selección de Peores Casos")
    st.write("Ingrese los parámetros operativos de la línea para determinar automáticamente la matriz de peores casos según la norma OMS TRS 1044 Anexo 2, EU GMP Anexo 1 y PDA TR 22.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 🏭 Configuración de Barrera y Duración")
        tecnologia = st.selectbox("Tecnología de Barrera:", ["Aislador Robótico Sin Guantes", "Aislador VHP Convencional", "RABS Cerrado/Abierto", "Sala Limpia Convencional Grado A/B"])
        duracion = st.number_input("Duración de campaña pretendida (Horas):", min_value=1, max_value=72, value=8)
        operadores = st.number_input("Máximo de operadores en Grado A/B:", min_value=1, max_value=10, value=3)
        gas_inerte = st.selectbox("¿Utiliza Nitrógeno/CO2 en proceso comercial?", ["Sí", "No"])

    with col_b:
        st.markdown("### 🍾 Matriz de Envases y Velocidades")
        st.markdown("**Envase Opción A (Pequeño):**")
        boca_a = st.number_input("Diámetro de boca A (mm):", min_value=1.0, value=13.0)
        vol_a = st.number_input("Volumen nominal A (mL):", min_value=0.1, value=5.0)
        
        st.markdown("**Envase Opción B (Grande):**")
        boca_b = st.number_input("Diámetro de boca B (mm):", min_value=1.0, value=20.0)
        vol_b = st.number_input("Volumen nominal B (mL):", min_value=0.1, value=50.0)
        
        vel_min = st.number_input("Velocidad mínima (u/h):", min_value=100, value=1200)
        vel_max = st.number_input("Velocidad máxima (u/h):", min_value=100, value=6000)

    st.markdown("---")
    if st.button("🔍 Determinar Matriz de Peores Casos"):
        boca_max = max(boca_a, boca_b)
        env_max = "Envase B" if boca_b > boca_a else "Envase A"
        
        st.markdown(f"""
        <div class="card">
            <h4>1. Envase de Peor Caso Microbiológico</h4>
            <p><b>Selección:</b> {env_max} (Diámetro de apertura de boca: <b>{boca_max} mm</b>).</p>
            <p><i>Sustento Técnico (OMS TRS 1044 / EU GMP Anexo 1 9.36):</i> La abertura más ancha representa el peor caso por mayor superficie expuesta al flujo de aire y deposición de micropartículas.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="card">
            <h4>2. Estrategia Combinada de Velocidad de Llenado</h4>
            <p><b>Selección:</b> Alternar tramos a <b>Velocidad Mínima ({vel_min} u/h)</b> y <b>Velocidad Máxima ({vel_max} u/h)</b>.</p>
            <p><i>Sustento Técnico (FDA 2004 / PDA TR 22):</i> La velocidad mínima es el peor caso por tiempo de residencia y exposición. La velocidad máxima es el peor caso por estrés mecánico y vibración.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if gas_inerte == "Sí":
            st.markdown("""
            <div class="gold-card">
                <h4>3. Sustitución Obligatoria de Gas Inerte por Aire Estéril</h4>
                <p><b>ACCIÓN CRÍTICA:</b> Debe sustituir el Nitrógeno/CO2 por <b>AIRE ESTÉRIL FILTRADO</b> durante el Media Fill.</p>
                <p><i>Sustento Técnico (OMS TRS 1044 9.33.iii / PDA TR 22):</i> La purga con nitrógeno asfixia bacterias y hongos aerobios obligados, ocultando fallos de contaminación.</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------------
# MÓDULO 3: GENERADOR DE BORRADOR DE PROTOCOLO
# ---------------------------------------------------------
elif opcion == "3. Generador de Borrador de Protocolo":
    st.header("📝 Módulo 3: Generador de Borrador de Protocolo APS")
    st.write("Suministre los datos básicos del sitio para construir el documento inicial del protocolo.")
    
    with st.form("form_p"):
        empresa = st.text_input("Compañía / Planta:", "Farmacéutica PAF S.A.")
        linea = st.text_input("Nombre de la Línea de Llenado:", "Línea No. 3 - Viales Inyectables")
        lote = st.number_input("Tamaño de Lote del Media Fill (viales):", min_value=1000, value=10000)
        medio = st.text_input("Medio de Cultivo:", "Caldo Soja Triptona (SCDM / TSB)")
        btn = st.form_submit_button("📄 Redactar Protocolo")
        
    if btn:
        md_text = f"""# PROTOCOLO DE VALIDACIÓN DE SIMULACIÓN DE PROCESO ASÉPTICO (APS)
**Documento:** PRT-APS-{linea.replace(' ', '_').upper()}  
**Planta:** {empresa} | **Línea:** {linea}  

### 1. OBJETIVO
Demostrar de forma documental e irrefutable que la **{linea}** mantiene el estado estéril llenando **{lote:,} unidades** con **{medio}** bajo condiciones de peores casos.

### 2. CLASIFICACIÓN EN TRES POBLACIONES (Agalloco / OMS TRS 1044)
1. **Población 1 (SE INCUBAN):** Unidades integrales llenas con medio sin defectos.
2. **Población 2 (DESCARTES SOP):** Unidades retiradas durante intervenciones comerciales autorizadas por SOP.
3. **Población 3 (RECHAZOS FÍSICOS):** Unidades sin integridad física (rotas) descartadas sin incubar.

### 3. PROTOCOLO DE INCUBACIÓN SECUENCIAL DUAL
- Inversión manual del 100% de la Población 1 previo a la incubación.
- **Fase 1:** 7 días a 20–25 °C (posición normal).
- **Fase 2:** 7 días a 30–35 °C (posición invertida).

### 4. CRITERIO DE ACEPTACIÓN
- **CERO CRECIMIENTO ABSOLUTO (*Target of Zero Growth*)** según la OMS TRS 1044 Anexo 2.
"""
        st.success("✅ Protocolo borrador generado exitosamente.")
        st.text_area("Texto del Protocolo (.md):", md_text, height=350)
        st.download_button("💾 Descargar Protocolo (.md)", md_text, file_name="Protocolo_APS.md")

# ---------------------------------------------------------
# MÓDULO 4: CÁLCULO DE VOLUMEN MÍNIMO Y HEADSPACE
# ---------------------------------------------------------
elif opcion == "4. Cálculo de Volumen y Headspace":
    st.header("🧪 Módulo 4: Cálculo de Volumen de Medio y Headspace de Oxígeno")
    st.write("Determine el volumen exacto de Caldo Soja Triptona (SCDM/TSB) requerido para garantizar contacto con paredes y viabilidad de organismos aerobios (OMS TRS 1044 / PDA TR 22).")
    
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown("### 🍾 Dimensiones del Envase")
        vol_capacidad = st.number_input("Capacidad Total/Real del Envase hasta el borde (mL):", min_value=1.0, value=12.0, step=0.5)
        diametro_boca = st.number_input("Diámetro interno de boca (mm):", min_value=5.0, value=20.0, step=1.0)
        tipo_envase = st.selectbox("Tipo de Envase Primario:", ["Vial de Vidrio", "Ampolleta de Vidrio/Plástico", "Jeringa Prellenada", "Contenedor BFS"])

    with col_v2:
        st.markdown("### 🎯 Parámetros Propuestos de Llenado")
        vol_propuesto = st.number_input("Volumen de Medio de Cultivo a Llenar por Envase (mL):", min_value=0.1, value=4.0, step=0.5)

    # Lógica de cálculo técnico
    vol_minimo_recomendado = max(2.0, vol_capacidad * 0.30)  # Mínimo 30% del envase o 2 mL
    vol_maximo_permitido = vol_capacidad * 0.75             # Máximo 75% para dejar 25% headspace
    headspace_obtenido = ((vol_capacidad - vol_propuesto) / vol_capacidad) * 100
    
    st.markdown("---")
    st.markdown("### 📊 Resultados del Diagnóstico Volumétrico")
    
    col_r1, col_r2, col_r3 = st.columns(3)
    col_r1.metric("Volumen Mínimo Humectación", f"{vol_minimo_recomendado:.1f} mL")
    col_r2.metric("Volumen Máximo Permisible", f"{vol_maximo_permitido:.1f} mL")
    col_r3.metric("Headspace Libre de Aire", f"{headspace_obtenido:.1f} %")

    # Evaluación de criterios
    if vol_propuesto < vol_minimo_recomendado:
        st.error(f"❌ **ALERTA (Volumen Insuficiente):** El volumen propuesto de {vol_propuesto} mL es menor al mínimo recomendado ({vol_minimo_recomendado:.1f} mL). Existe riesgo de que el medio de cultivo no humedezca totalmente las paredes e interior del tapón durante la inversión.")
    elif vol_propuesto > vol_maximo_permitido:
        st.warning(f"⚠️ **ALERTA (Headspace Deficiente):** El volumen propuesto de {vol_propuesto} mL deja solo un {headspace_obtenido:.1f}% de espacio de aire. Puede asfixiar bacterias aerobias obligadas y generar falsos negativos.")
    else:
        st.success(f"✅ **VOLUMEN CONFORME:** El llenado con {vol_propuesto} mL proporciona suficiente volumen para humedecer las paredes y conserva un **{headspace_obtenido:.1f}% de headspace con aire estéril** para el desarrollo de la flora de prueba.")

    # Justificación técnica en caja elegante
    st.markdown(f"""
    <div class="card">
        <h4>📜 Sustento Regulatorio de Aceptación</h4>
        <ul>
            <li><b>OMS TRS 1044 Anexo 2 (Sección 9.33):</b> El volumen debe ser representativo y suficiente para contactar todas las superficies del contenedor post-inversión.</li>
            <li><b>PDA Technical Report No. 22:</b> Se requiere un volumen adecuado de aire estéril (no nitrógeno) en el headspace para evitar la inhibición del crecimiento de levaduras y bacilos aerobios.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# MÓDULO 5: GUÍA DE DESPLIEGUE E INSTALACIÓN EN CELULAR / PC
# ---------------------------------------------------------
else:
    st.header("📲 Módulo 5: ¿Cómo Compartir e Instalar esta App en Celular (PWA) o PC?")
    st.markdown("""
    ### 📱 Pasos para Instalar en el Celular (Android / iPhone)
    1. **Despliegue Gratuito en la Nube (2 minutos):**
       - Guarde este archivo como `evaluador_peor_caso_app.py` y súbalo a un repositorio en **GitHub**.
       - Ingrese a [share.streamlit.io]([suspicious link removed]) e inicie sesión gratis.
       - Seleccione su repositorio y presione **"Deploy"**.
       - Obtendrá una URL pública segura.
    2. **Agregar a la Pantalla de Inicio en Celulares:**
       - Abra el enlace en **Google Chrome** (Android) o **Safari** (iPhone).
       - En el menú de opciones (tres puntos en Android / botón Compartir en iPhone), toque **"Agregar a la pantalla de inicio"** (*Add to Home Screen*).
       - ¡Listo! La App aparecerá con su icono en la pantalla del celular como una App nativa.

    ### 💻 Pasos para Ejecutar en Computador
    1. Abra la terminal e instale las librerías:
       ```bash
       pip install streamlit pandas
       ```
    2. Ejecute la aplicación con:
       ```bash
       streamlit run evaluador_peor_caso_app.py
       ```
    """)