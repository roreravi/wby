# Repo compartido con el equipo de Data Science para el trabajo de datos de Webookyou
esquema de trabajo:
- EDA de xls de reporte de ANT
- División de los campos para la confección de la Base de Datos Relacional
- Conexión  al RSD de AWS con PostgreSQL
- Ingesta de tablas


módulos:
- eda.ipynb: jupiter notebook con el EDA que vienen realizado del xls
- conexion.py: modulo con conexión a la BD (psycopg2)
- tablas.py: modulo con tablas de hechos y dimensiones (pandas) para ingestar a la BD
- ingesta.py: modulo para ingesta a la DB de las tablas realizadas en tablas.py (pandas.to_sql) . importar los modulos

links:
- excel compartido de análisis: https://docs.google.com/spreadsheets/d/1niVlNzs8LKRxE6mVss1BGcV4cAAb8tbn2Lxl3piaqsk/edit?usp=sharing
- armado de tablas y visualización: https://lucid.app/lucidchart/fc84d66d-6ab6-4a1e-b642-56aec4653277/edit?view_items=0kbcktc7B9Q9&invitationId=inv_31687623-6f49-4400-a322-db6f1e32b2d1