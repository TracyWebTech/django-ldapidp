
from fabric.operations import put
from fabric.api import run, sudo, env
from fabric.contrib.files import exists
from fabric.decorators import with_settings
from fabric.context_managers import prefix, cd, settings

env.user = 'vagrant'
env.use_shell = False

environments = {
    'dev': {
        'hosts': ['127.0.0.1'],
        'key_filename': '~/.vagrant.d/insecure_private_key',
        'port': 2222,
    },
}
 
ENV_NAME = 'ldap'
SOURCE_VENV = 'source /usr/local/bin/virtualenvwrapper.sh'
WORKON_COLAB = '{} && workon {}'.format(SOURCE_VENV, ENV_NAME)


def environment(name):
    env.update(environments[name])
    env.environment = name
environment('dev')


def mkvirtualenv():
    if not exists('~/.virtualenvs/{}'.format(ENV_NAME)):
        with prefix(SOURCE_VENV):
            run('mkvirtualenv {}'.format(ENV_NAME))
            return True


def install():
    mkvirtualenv()

    with cd('/vagrant/'), prefix(WORKON_COLAB):
        run('pip install -r requirements.txt')
