from apscheduler.schedulers.blocking import BlockingScheduler
import tweet

tweetschedule = BlckingScheduler()

@tweetschedule.scheduled_job('interval', minutes=720)
def timed_job():
    tweet.puttweet()

if __name__ == "__main__":
    tweetschedule.start()


