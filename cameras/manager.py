''' Manager file for managing camera operations '''
import subprocess


class ProcessManager:
    ''' Class representing process manager '''

    def __init__(self, path: str = 'script.py'):
        self.process: None | subprocess.Popen = None
        self.script: str = path

    def run(self) -> None:
        ''' Runs the process '''
        if not self.is_running:
            self.process = subprocess.Popen(['python3', self.script])

    def terminate(self) -> None:
        ''' Terminates the process '''
        if self.is_running:
            self.process.terminate()
            self.process = None

    @property
    def is_running(self) -> bool:
        ''' Returns True if the process is running '''
        return self.process is not None
