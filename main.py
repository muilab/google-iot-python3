# -*- coding: utf-8 -*-
import os
import time
import json
from google.auth import jwt
from google.cloud import pubsub_v1

PROJECT_ID =  os.environ.get('GOOGLE_IOT_PROJECT')

service_account_info = json.load(open("/data/service.json"))
audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

credentials = jwt.Credentials.from_service_account_info(
    service_account_info, audience=audience
)

subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

# The same for the publisher, except that the "audience" claim needs to be adjusted
publisher_audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
credentials_pub = credentials.with_claims(audience=publisher_audience)
publisher = pubsub_v1.PublisherClient(credentials=credentials_pub)


def publish_events(event_message: str):
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id=PROJECT_ID,
        topic='device-events',
    )
    publisher.publish(topic_name, event_message.encode(encoding='utf-8'), spam='eggs')    


def subscribe_events():
    def callback(message):
        print('received message : '.format(message.data.decode()))

    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id=PROJECT_ID,
        topic='device-events',
    )
    subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
        project_id=PROJECT_ID,
        sub='device-events',
    )

    print('subscribe topic')
    subscriber.subscribe(subscription_name, callback)


if __name__ == "__main__":
    print("works!")

    publish_events('boot!')

    while True:
        time.sleep(1)