FROM python:3.11-alpine

# Créez l'utilisateur hbnb
RUN adduser -D -s /bin/bash hbnb

# Passez à l'utilisateur hbnb
USER hbnb

# Définissez le répertoire de travail
WORKDIR /home/hbnb

# Copiez le fichier requirements.txt
COPY requirements.txt .

# Installez les dépendances nécessaires pour pip et les librairies système
RUN pip install --no-cache-dir -r requirements.txt
    

# Copiez l'application dans le conteneur
COPY app /home/hbnb/app

# Définissez la variable d'environnement et exposez le port
ENV PORT 8000
EXPOSE 8000

# Définissez le volume
VOLUME ["/home/hbnb/app/data"]

# Changez le répertoire de travail pour /home/hbnb/app
WORKDIR /home/hbnb/app

# Utilisez l'ENTRYPOINT pour exécuter votre application
#ENTRYPOINT ["python", "app.py"]

CMD ["python", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]