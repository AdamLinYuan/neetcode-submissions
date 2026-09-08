class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.idToTweet = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.idToTweet[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.idToTweet[userId][:]
        
        # Now this iterates over people I actually follow
        for followeeId in self.followMap[userId]:
            feed.extend(self.idToTweet[followeeId])
        
        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            # FIX 1: Store that followerId follows followeeId
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # FIX 2: Use discard to avoid KeyError crash
        self.followMap[followerId].discard(followeeId)