from crontab import CronTab


class MyCronTab:

    def __init__(self, filename: str):
        self.filename = filename
        self.cron = CronTab()

    def job_every_hour(self, hour: int = 3):
        job = self.cron.new(command=f"python {self.filename}")
        job.hour.every(hour)

    def job_every_day(self, hour: int = 15, minute: int = 15):
        job = self.cron.new(command=f"python {self.filename}")
        job.hour.on(hour)
        job.minute.on(minute)

    def job_every_sunday(self, hour: int = 0, minute: int = 0):
        job = self.cron.new(command=f"python {self.filename}")
        job.day.on(7)
        job.hour.on(0)
        job.minute.on(0)

    def write_file(self, user: str, filename: str):
        self.cron.write(user=user, filename=filename)