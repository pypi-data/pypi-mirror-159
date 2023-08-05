# implements a decentralized routines worker 
# connects to worker pool
# broadcast heartbeat
# listen to commands

import os,sys,psutil,time,json,boto3,subprocess
from importlib.metadata import version

import numpy as np
from pathlib import Path

from SharedData.Logger import Logger

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """
    Logger.log.info('restarting worker...')
    try:
        p = psutil.Process(os.getpid())
        children = p.children(recursive=True)
        for child in children:
            child.kill()         

    except Exception as e:
        Logger.log.error('restarting worker ERROR!')
        Logger.log.error(e)

    python = sys.executable
    os.execl(python, python, *sys.argv)

def send_command(command,env=None):
    Logger.log.debug('sending command: %s...' % (' '.join(command)))

    if env is None:
        process = subprocess.Popen(command,\
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,\
            universal_newlines=True, shell=True)        
    else:    
        process = subprocess.Popen(command,\
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,\
            universal_newlines=True, shell=True,env=env)        

    while True:
        output = process.stdout.readline()
        if ((output == '') | (output == b''))\
                & (process.poll() is not None):
            break        
        if (output) and not (output.startswith('Completed')):
            if output.rstrip()!='':
                Logger.log.debug('command response:'+output.rstrip())  
    rc = process.poll() #block until process terminated
    success= rc==0
    if success:
        Logger.log.debug('sending command DONE!')
        return True
    else:
        Logger.log.debug('sending command ERROR:%s!' % (''.join(process.stderr.readlines())))
        return False

def install_repo(command):
                
    runroutine = False
    if  ('GIT_USER' not in os.environ) | \
        ('GIT_TOKEN' not in os.environ) |\
        ('GIT_ACRONYM' not in os.environ):
        Logger.log.error('Installing repo %s ERROR missing git parameters'\
                % (command['repo']))
    else:
        repo_path=Path(os.environ['SOURCE_FOLDER'])/command['repo']
        requirements_path = repo_path/'requirements.txt'
        python_path=repo_path/'venv\\Scripts\\python.exe'
        
        repo_exists = repo_path.is_dir()
        venv_exists = python_path.is_file()
        install_requirements=~python_path.is_file()        

        env = os.environ.copy()
        env['VIRTUAL_ENV'] = str(repo_path/'venv')
        env['PATH'] = str(repo_path/'venv')+';'+str(repo_path/'venv\\Scripts')+';'+env['PATH']
        env['PYTHONPATH'] = str(repo_path/'venv')+';'+str(repo_path/'venv\\Scripts')
        env['GIT_TERMINAL_PROMPT'] = "0"
        
        GIT_URL='https://'+os.environ['GIT_USER']+':'+os.environ['GIT_TOKEN']+'@'\
            +os.environ['GIT_SERVER']+'/'+os.environ['GIT_ACRONYM']+'/'+command['repo']
        
        # GIT PULL OR GIT CLONE
        if repo_exists:                 
            Logger.log.info('Pulling repo %s' % (command['repo']))    
            requirements_lastmod = 0
            if requirements_path.is_file():
                requirements_lastmod = os.path.getmtime(str(requirements_path))            
            
            # pull existing repo               
            cmd = ['git','-C',str(repo_path),'pull',GIT_URL]
            if not send_command(cmd):
                Logger.log.error('Pulling repo %s ERROR!' % (command['repo']))
                runroutine = False
            else:
                if requirements_path.is_file():
                    install_requirements = os.path.getmtime(str(requirements_path))!=requirements_lastmod                        
                    runroutine=True        
                    Logger.log.info('Pulling repo %s DONE!' % (command['repo']))
                else:
                    install_requirements = False
                    runroutine = False
                    Logger.log.error('Pulling repo %s ERROR: requirements.txt not found!' % (command['repo']))
                    

        else:                        
            Logger.log.info('Cloning repo %s...' % (command['repo']))
            cmd = ['git','-C',str(repo_path.parents[0]),'clone',GIT_URL]
            if not send_command(cmd):
                Logger.log.error('Cloning repo %s ERROR!' % (command['repo']))
                runroutine=False
            else:               
                runroutine=True
                if requirements_path.is_file():
                    install_requirements = True
                    Logger.log.info('Cloning repo %s DONE!' % (command['repo']))
                else:
                    install_requirements = False
                    Logger.log.error('Cloning repo %s ERROR: requirements.txt not found!' % (command['repo']))

                

        # CREATE VENV
        if (runroutine) & (not venv_exists):
            Logger.log.info('Creating venv %s...' % (command['repo']))
            if not send_command(['python','-m','venv',str(repo_path/'venv')]):
                Logger.log.error('Creating venv %s ERROR!' % (command['repo']))
                runroutine=False
            else:
                runroutine=True
                if requirements_path.is_file():
                    install_requirements=True
                    Logger.log.info('Creating venv %s DONE!' % (command['repo']))
                else:
                    install_requirements = False
                    Logger.log.error('Creating venv %s ERROR: requirements.txt not found!' % (command['repo']))   
                        
        # INSTALL REQUIREMENTS
        if (runroutine) & (install_requirements):
            Logger.log.info('Installing requirements %s...' % (command['repo']))
            if not send_command([str(python_path),'-m','pip','install','-r',str(requirements_path)],env=env):
                Logger.log.error('Installing requirements %s ERROR!' % (command['repo']))
                runroutine=False
            else:                
                runroutine=True
                Logger.log.info('Installing requirements %s DONE!' % (command['repo']))
    
    return runroutine 