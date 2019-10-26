from apscheduler.schedulers.blocking import BlockingScheduler
import tweet

tweetschedule = BlockingScheduler()

@tweetschedule.scheduled_job('interval', minutes=2)
def timed_job():
    tweet.puttweet()

if __name__ == "__main__":
    tweetschedule.start()


