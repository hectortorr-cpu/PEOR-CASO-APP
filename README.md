# 🛡️ Evaluador de Peores Casos y Generador de Protocolos APS

> **Innovación con Propósito | Llenado Aséptico Farmacéutico (PAF)**  
> *Aplicación interactiva y herramienta de diagnóstico GxP para la Simulación de Procesos Asépticos (APS / Media Fill) bajo normatividad internacional (OMS TRS 1044, EU GMP Anexo 1, U.S. FDA y PDA TR 22).*

[![Streamlit App]([suspicious link removed])]([suspicious link removed])
[![Python Version]([suspicious link removed])]([suspicious link removed])
[![GxP Compliant]([suspicious link removed])](#-fundamentación-normativa)

---

## 📌 Descripción General

Esta aplicación web y móvil fue desarrollada para asistir a los equipos de **Validaciones, Garantía de Calidad y Microbiología** en la preparación, evaluación y documentación de los ejercicios de **Simulación de Procesos Asépticos (APS / Media Fill)**. 

La herramienta combina algoritmos de evaluación de peores casos (*worst-cases*), calculadores volumétricos de espacio de cabeza (*headspace*), listas de verificación de prerrequisitos (*Go/No-Go*) y un generador automatizado de protocolos de validación.

---

## 🚀 Módulos Principales

1. **📋 Diagnóstico de Prerrequisitos (Go / No-Go):**
   * Evaluación de 11 criterios críticos previos al llenado (HVAC, WFI, CIP/SIP, calificación IQ/OQ, *gowning* de operarios y pruebas GPT compendiales + aislados nativos).
   * Dictamen automatizado de alistamiento operacional.

2. **🎯 Evaluador Minucioso de Peores Casos (Worst-Case):**
   * Algoritmo de selección del envase de peor caso microbiológico (diámetro de boca/apertura más ancha).
   * Determinación de estrategia combinada de velocidades (mínima para exposición / máxima para estrés mecánico).
   * Alertas automáticas para la sustitución obligatoria de gases inertes (Nitrógeno/$\text{CO}_2$) por aire estéril filtrado.

3. **📝 Generador de Borrador de Protocolo APS:**
   * Construcción automatizada de la estructura inicial del protocolo de validación.
   * Clasificación de viales en las **Tres Poblaciones de Agalloco / OMS**.
   * Protocolo de incubación secuencial dual consecutiva (7 días a 20–25 °C + 7 días a 30–35 °C en posición invertida).

4. **🧪 Calculador de Volumen y Headspace de Oxígeno:**
   * Cálculo de volumen mínimo recomendado para humectación del 100% de paredes internas y tapón.
   * Diagnóstico de porcentaje de *headspace* para viabilizar el desarrollo de bacterias y hongos aerobios obligados.

5. **📲 Guía de Despliegue PWA:**
   * Instructivo para instalar la aplicación en teléfonos inteligentes (Android / iOS) como App nativa.

---

## 🛠️ Requisitos e Instalación Local

### Prerrequisitos
* Python 3.10 o superior instalado en el sistema.

### Pasos de Instalación en PC
1. Clona o descarga este repositorio:
   ```bash
   git clone [suspicious link removed]
   cd app-peores-casos-aps