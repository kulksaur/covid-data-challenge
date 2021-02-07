from crontab import CronTab
import pathlib

CURRENT_DIR = pathlib.Path().absolute()

cronLogFilePath = pathlib.Path(str(CURRENT_DIR)) / "cron.log"

# For Unix/Linux Environments
# executableFilePath = pathlib.Path(str(CURRENT_DIR)) / "ImportCovidDataTaskExecutable"
# commandToRunForCron = f"{executableFilePath} >> {cronLogFilePath} 2>&1"

# For Any Environments
pythonDirectory = pathlib.Path(str(CURRENT_DIR)) / "venv" / "bin" / "python"
mainSourceScriptPath = pathlib.Path(str(CURRENT_DIR)) / "source" / "importDataTask.py"
commandToRunForCron = f"{pythonDirectory} {mainSourceScriptPath} >> {cronLogFilePath} 2>&1"

cron = CronTab(user=True)
job = cron.new(command=commandToRunForCron)
job.setall("0 9 * * *")
cron.write()
