

import praw

#Setting up - explained in book/presentation
reddit = praw.Reddit(client_id='thisisaclientid',
                     client_secret='thisisaclientsecret',
                     user_agent='thisisauseragent',     
                     username='thisusernameisoptional',
                     password='=thispasswordisoptional')

#sometimes you need to be in read_only mode, but sometimes not. For the first few examples, you can be in read_only mode. 
reddit.read_only = True


#getting current hottest posts from the subreddit -----------------------

subreddit = reddit.subreddit('learnpython') #defining subreddit
for submission in subreddit.hot(limit=15): #we want only the hottest 15 posts
    print(submission.title)  # title
    print(submission.score)  # score
    print(submission.id)     # ID
    print(submission.url)	#Url


#getting comments from a post ------------------------------

submission = reddit.submission(id='akjob6') #choosing post
submission.comments.replace_more(limit=None) #this says that we want comments from the post, and that we want all of them with no limit
for comment in submission.comments.list(): #print them 
    print(comment.body)




#This is a reddit bot. It will automatically do things for you. ---------------------------------------------

reddit.read_only = False #We must turn off read only mode so that it can do more than just read stuff on reddit. This is also one of those
#instances where you need to include a reddit usernamae and password at the top so that you can login.


looking_for = ['dog','puppy','doggo'] #list of words we are looking for in a title
reply = 'Cute dog' #what we will reply


def main():

    subreddit = reddit.subreddit('dogpictures') #we will be looking for things in the dogpictures subreddit
    for submission in subreddit.stream.submissions(): #going through the stream of submissions
        process_submission(submission) #process the submission


def process_submission(submission):

    normalized_title = submission.title.lower() #lowering it so caps don't matter

    for dog in looking_for: #searching for the terms we listed phrase
        if dog in normalized_title: #searching for the terms  in the normalized title
            print('Replying to: {}'.format(submission.title)) #just so we can see what our bot is replying to
            submission.reply(reply) #comment the reply
            # A reply has been made so do not attempt to match other phrases
            break

if __name__ == '__main__':
    main()


#Say we want to find all the comments or content of a specific Reddit user -------------
#in this instance, we'll load 10 Barack Obama's top comments

# we define the redddit account with reddit.redditor('') and then that we want comments, the top comments, and only 10 of them
for comment in reddit.redditor('presidentobama').comments.top(limit=10):
	print(comment.body) #print the comment body


