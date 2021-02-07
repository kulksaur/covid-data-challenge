from crontab import CronTab
import pathlib

CURRENT_DIR = pathlib.Path().absolute()

cronLogFilePath = pathlib.Path(str(CURRENT_DIR)) / "cron.log"
executableFilePath = pathlib.Path(str(CURRENT_DIR)) / "ImportCovidDataTaskExecutable"
commandToRunForCron = f"{executableFilePath} >> {cronLogFilePath} 2>&1"
cron = CronTab(user=True)
job = cron.new(command=commandToRunForCron)
job.minute.every(1)
cron.write()