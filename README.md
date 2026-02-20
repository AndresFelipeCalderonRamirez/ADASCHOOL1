# Carbon Tracker Service – Enunciado del Proyecto

## FASE 1 – DISEÑO Y PLANIFICACIÓN (CHAIN OF THOUGHT)

### Instrucciones

Tenemos que construir un microservicio llamado:

Carbon Tracker Service  
Para la empresa EcoLogistics.

Debe calcular emisiones de CO₂ considerando:

- Tipo de vehículo:
  - ELECTRIC
  - DIESEL
  - HYBRID
- Peso de carga (toneladas)
- Distancia (km)
- Factor de eficiencia energética

---

## Paso 1 – Diseño lógico

Antes de escribir código:

1. Explica la fórmula matemática propuesta para calcular CO₂.
2. Define cómo variará el cálculo según el tipo de vehículo.
3. Identifica posibles edge cases.
4. Define reglas de validación.
5. Propón cómo evitar violaciones a principios SOLID.
6. Propón cómo desacoplar la lógica del framework.

NO escribas código todavía.

---

## Paso 2 – Diseño de Arquitectura

Propón:

- Estructura de carpetas.
- Separación entre:
  - Controllers
  - Services
  - Domain
  - DTOs
  - Validators
  - Tests
- Qué patrón aplicarías (Strategy Pattern para vehículos, por ejemplo).
- Explica brevemente por qué.

Luego espera confirmación antes de generar código.

---

## FASE 2 – IMPLEMENTACIÓN

Cuando yo diga: “Genera el código”

Debes:

- Crear el microservicio en Node.js + TypeScript con Express.
- Separar claramente:
  - Lógica de negocio
  - Controladores
  - Rutas
  - Validaciones
- Implementar Strategy Pattern para los tipos de vehículo.
- Agregar manejo de errores con:
  - Custom Error Classes
  - Middleware de errores
- Validar entradas con Zod o class-validator.
- Incluir tipado fuerte (interfaces y enums).

El código debe:

- Ser modular.
- Cumplir SOLID.
- Ser testeable.
- Evitar lógica en controladores.
- Tener comentarios mínimos pero claros.

---

## FASE 2.1 – REFINAMIENTO ITERATIVO

Después de generar el código:

1. Analiza posibles vulnerabilidades:
   - Input tampering
   - Overflow
   - Datos negativos
2. Mejora el manejo de errores.
3. Refactoriza si detectas violaciones de:
   - SRP
   - OCP
4. Optimiza para escalabilidad.

---

## FASE 3 – GENERACIÓN DE PRUEBAS

Cuando yo diga: “Genera pruebas unitarias”

Debes:

- Usar Jest.
- Crear pruebas para:
  - Cada tipo de vehículo
  - Distancia cero
  - Carga negativa
  - Tipo de vehículo inválido
  - Factor eficiencia cero
- Alcanzar mínimo 90% de cobertura lógica.
- Simular casos de error.
- Explicar brevemente qué cubre cada bloque de pruebas.

---

## FASE 4 – CODE REVIEW CRÍTICO

Cuando yo diga: “Haz code review”

Debes:

Analizar el código como si fueras un Tech Lead.

Evaluar:

- Seguridad
- Performance
- Escalabilidad
- Clean Architecture
- Principios SOLID

Además:

- Señalar mejoras concretas.
- Proponer refactorizaciones.
- Identificar posibles riesgos al usar LLMs en producción.

---

## FASE 5 – BITÁCORA DE PROMPTS

Cuando yo diga: “Genera bitácora”

Debes crear un resumen estructurado que incluya:

- Prompt inicial
- Evolución de la lógica
- Refinamientos
- Mejoras post review
- Lecciones aprendidas

Formato: Markdown listo para PDF.

---

## CONSIDERACIONES IMPORTANTES

- Nunca mezcles lógica de negocio con controladores.
- Usa enums para tipos de vehículo.
- Aplica Strategy Pattern.
- Evita código duplicado.
- Maneja errores de forma centralizada.
- Prioriza claridad sobre complejidad innecesaria.