import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:

        if userId not in self.follows[userId]:
            self.follows[userId].add(userId)

        heap = []
        for uid in self.follows[userId]:
            arr = self.tweets.get(uid)
            if arr:
                t, tid = arr[-1]
                idx = len(self.tweets[uid]) - 1
                heapq.heappush(heap, (-t, tid, uid, idx))
        
        feed = []
        while heap and len(feed) < 10:
            t, tid, uid, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx - 1 >= 0:
                heapq.heappush(heap, (-t, tid, uid, idx - 1))

        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)