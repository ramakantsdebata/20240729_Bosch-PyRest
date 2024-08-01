## Publisher ##########################
subscriber_notifiers = []

def Register(notifier):
    subscriber_notifiers.append(notifier)

def Deregister(notifier):
    subscriber_notifiers.remove(notifier)

def NotifyAll():
    print(subscriber_notifiers)

    for fn in subscriber_notifiers:
        fn()

## Subscriber1 ######################

def s1_notify():
    print("Notified sub 1 of event")

Register(s1_notify)


## Subscriber2 ######################

def s2_notify():
    print("Notified sub 2 of event")

Register(s2_notify)

## Subscriber3 ######################

def s3_notify():
    print("Notified sub 3 of event")

Register(s3_notify)



## Events will occur (Publisher) #################

NotifyAll()

print("\n", "="*40, "\n")
Deregister(s2_notify)

NotifyAll()