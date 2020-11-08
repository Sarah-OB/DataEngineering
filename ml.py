df=pd.read_csv('Reviews.csv')

df = df[df['Score'] != 3]
df['sentiment'] = df['Score'].apply(lambda rating : +1 if rating > 3 else -1)

def remove_punctuation(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":",  "!",'"'))
    return final
df['Text'] = df['Text'].apply(remove_punctuation)
df = df.dropna(subset=['Summary'])
df['Summary'] = df['Summary'].apply(remove_punctuation)

index = df.index
df['random_number'] = np.random.randn(len(index))
train = df[df['random_number'] <= 0.8]
test = df[df['random_number'] > 0.8]

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
train_matrix = vectorizer.fit_transform(train['Summary'])
test_matrix = vectorizer.transform(test['Summary'])

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

X_train = train_matrix
X_test = test_matrix
y_train = train['sentiment']
y_test = test['sentiment']

lr.fit(X_train,y_train)

predictions = lr.predict(X_test)

from sklearn.metrics import confusion_matrix,classification_report
new = np.asarray(y_test)
confusion_matrix(predictions,y_test)

print(classification_report(predictions,y_test))

lr.score(X_test,y_test)

tx = "As long as I’m president of the United States, Iran will never be allowed to have a nuclear weapon. Good morning. I’m pleased to inform you the American people should be extremely grateful and happy. No Americans were harmed in last night’s attack by the Iranian regime. We suffered no casualties. All of our soldiers are safe, and only minimal damage was sustained at our military bases. Our great American forces are prepared for anything.Iran appears to be standing down, which is a good thing for all parties concerned and a very good thing for the world. No American or Iraqi lives were lost because of the precautions taken, the dispersal of forces and an early warning system that worked very well.I salute the incredible skill and courage of America’s men and women in uniform. For far too long, all the way back to 1979, to be exact, nations have tolerated Iran’s destructive and destabilizing behavior in the Middle East and beyond. Those days are over. Iran has been the leading sponsor of terrorism, and their pursuit of nuclear weapons threatens the civilized world. We will never let that happen. Last week, we took decisive action to stop a ruthless terrorist from threatening American lives. At my direction, the United States military eliminated the world’s top terrorist, Qassim Suleimani."
lr.predict(vectorizer.transform([tx]))
