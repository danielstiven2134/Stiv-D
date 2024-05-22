# My app

## Configuración del entorno virtual

1. Primero, necesitamos crear un entorno virtual. Esto se puede hacer con el módulo `venv` de Python. En tu terminal, navega al directorio donde deseas crear el entorno virtual y ejecuta el siguiente comando:

```bash
python3 -m venv nombre_del_entorno
```


2. Una vez creado el entorno virtual, necesitamos activarlo. Esto se hace con el siguiente comando:

```bash
source nombre_del_entorno/bin/activate
```


3. Con el entorno virtual activado, podemos instalar las dependencias necesarias para el proyecto. Estas dependencias están listadas en el archivo requirements.txt. Para instalarlas, ejecuta el siguiente comando:


```bash
pip install -r requirements.txt
```

4. Finalmente, para ejecutar el servidor de Django, navega al directorio que contiene el archivo manage.py y ejecuta el siguiente comando:

```bash
python manage.py runserver
```

Esto iniciará el servidor de Django, y podrás acceder a él en tu navegador web en localhost:8000