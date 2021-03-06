from src import Twitter, Mongo, System
import time

l = System.Log()

def main():
    tw = Twitter.Twitter()
    mdb = Mongo.Mongo("twitter", "twitter")

    hashTagsList = ["#openbanking", "#apifirst", "#devops", 
                    "#cloudfirst", "#microservices", "#apigateway", 
                    "#oauth", "#swagger", "#raml", "#openapis"]

    for hashTag in hashTagsList:
        l.info(f"Getting tweets for {hashTag}")
        try:
            mdb.insert(tw.getHashTag(hashTag))
        except:
            l.error(f"timeout to inser {hashTag}")

while True:
    main()
    l.info("Sleeping for 1 hour")
    time.sleep(3600)

