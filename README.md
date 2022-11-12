# Twitter Bot
 Creates a Twitter bot that retweets and likes tweets using tweepy in Python. On startup, the bot also automatically follows users who are following the bot. View the documentation here on how to expand the bot's capabilities: [Tweepy Documentation](https://docs.tweepy.org/en/stable/)

## Instructions
- Signup for developer access to Twitter using the instructions provided in this [video](https://www.youtube.com/watch?v=2UBcRiddwAo)

- After grabbing your tokens from the developer portal, add the token keys to the keys.py file. **Make sure your repo is set to private as these credentials are sensitive!**

- Uncomment section "#Send a test tweet" to send a test tweet using your bot.
    - Don't forget to re comment the lines after the test!

- Uncomment #stream.add_rules(tweepy.StreamRule("#hashtaghere")) to use the rule to track a specific hashtag or hashtags!
    - Or see Example # 2 in twitter_bot.py to use a rule that tracks a keyword(s).
    - More info on creating/modifying your own rule can be found [here](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule#examples)
