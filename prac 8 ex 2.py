bad_words = ["bad", "hate", "stupid"]

feedback = "This is a bad and stupid product."

for word in bad_words:
    feedback = feedback.replace(word, "***")
    

print(feedback)
