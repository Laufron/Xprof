# coding: utf-8
# Fabric - mise à jour automatisée de l'application

from fabric.api import local, run, cd, env, settings, sudo, puts, abort
from fabric.contrib.project import rsync_project
from time import time

env.hosts = ['xprof.isae.fr']
env.user = 'root'
REMOTE_WORKING_DIR = '/srv/XProf/'


def sync(local_dir, remote_dir):
    """ synchronise les fichiers de l'application avec le serveur """

    rsync_project(local_dir=local_dir, remote_dir=remote_dir, delete=True, exclude=['*.pyc', '*.log', '__pycache__', '.idea', '.DS_Store'])


def services(status):
    """ commande de gestion des services de l'application """

    run("sudo systemctl %s xprof.service" % status)


def ajustements():
    """ ajuste les valeurs spécifiques aux serveurs """

    hostname = env.host_string.split(":")[0]

    with cd("xprof"):
        # serveur de production
        if hostname == 'xprof.isae.fr':
            run("mv settings_production.py settings.py")


def update():
    """ fonction de mise à jour de l'application """

    begin = time()
    services("stop")

    # copie des fichiers
    if local('basename "$(pwd)"', capture=True) != "xprof":
        abort("mise à jour avortée : mise à jour impossible à partir du répertoire courant, placez-vous à la racine du projet")
    sync(".", REMOTE_WORKING_DIR)

    # ajustements et mise à jour des fichiers statiques et de la base de données
    with cd(REMOTE_WORKING_DIR):
        run("pip3 install -r requirements.txt")
        ajustements()
        run("python3 manage.py collectstatic --noinput")
        result = run("python3 manage.py migrate --noinput")
        if result.failed:
            abort("mise à jour avortée : échec de la migration de la base de données; à corriger à la main")

    services("start")
    end = time()
    puts("durée de la mise à jour : %d s." % (end-begin))


