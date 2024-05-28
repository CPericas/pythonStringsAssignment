#Objective:
#The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize 
#customer feedback for a SaaS product.

#Task 1: Keyword Highlighter

#Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and 
#"average". Print out each review with the keywords in uppercase so they stand out.
reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]
keywords = ["good", "excellent", "bad", "poor", "average"]
def search_keywords(review):
    global reviews
    global keywords
    for review in reviews:
        found_keywords = []
        for keyword in keywords:
            if keyword in review.lower():
                found_keywords.append(keyword.upper())
            if found_keywords:
                print(f"Review: {review}")
                print(f"Keywords found: {', '.join(found_keywords)}\n")
search_keywords(reviews)


#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and 
#negative words to check against. The function should return the count of positive and negative words for each review.
#python positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
#negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

python_reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]
positive_words = ["good.", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
def tally_review_words(reviews):
    global python_reviews
    global positive_words
    global negative_words
    for idx, review in enumerate(reviews, start=1):
        positive_count = sum(1 for word in positive_words if word in review.lower())
        negative_count = sum(1 for word in negative_words if word in review.lower())
        print(f"Review {idx}: ")
        print(f"Positive words count: {positive_count}")
        print(f"Negative words count: {negative_count}\n")
tally_review_words(reviews)


#Task 3: Review Summary

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does 
#not cut off in the middle of a word.

def summarize_reviews(reviews):
    summary_reviews = []
    max_summary_length = 30
    for review in reviews:
        if len(review) <= max_summary_length:
            summary_reviews.append(review)
        else:
            last_space_index = review[:max_summary_length].rfind(' ')
            if last_space_index == -1:
                summary_reviews.append(review[:max_summary_length] + "...")
            else:
                summary_reviews.append(review[:last_space_index] + "...")
        return summary_reviews
summary_reviews = summarize_reviews(reviews) 
for idx, summary in enumerate(summary_reviews, start=1):
    print(f"Review {idx} summary: {summary}")