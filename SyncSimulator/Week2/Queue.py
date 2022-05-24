from Environment import *

N = 4

leaderPipet = MyMutex("leaderPipet")
followerPipet = MyMutex("followerPipet")
leaderRendezvous = MySemaphore(0, "leaderRendezvous")
followerRendezvous = MySemaphore(0, "followerRendezvous")


def leadersThread():
    while True:
        leaderPipet.wait()

        followerRendezvous.signal()
        leaderRendezvous.wait()
        print("one leader with one follower ")

        leaderPipet.signal()


def followersThread():
    while True:
        followerPipet.wait()

        leaderRendezvous.signal()
        followerRendezvous.wait()
        print("one follower with one leader")

        followerPipet.signal()


def setup():
    for i in range(N):
        subscribe_thread(followersThread)
        subscribe_thread(leadersThread)