# Q2. Create a class Book with the following attributes:
# • title
# • author
# • list of reviews
# And add methods to:
# • add a new review
# • count reviews
# • display all reviews

class Book:
    def detailsOfBook(self, title, author, reviews=None):
        if reviews is None:
            reviews = []
        self.title = title
        self.author = author
        self.list_of_reviews = reviews

    def addReview(self,newReview):
        self.list_of_reviews.append(newReview)

    def countReviews(self):
        print(len(self.list_of_reviews))

    def display_all_reviews(self):
        for i in self.list_of_reviews:
            print(i)
    def printing(self):
        print(self.title,self.author)
book1=Book()
Details=book1.detailsOfBook("fire of wings","A. P. J. Abdul Kalam",["review 1"])
book1.addReview("kya chal raha hai1")
book1.addReview("kya chal raha hai2")
book1.addReview("kya chal raha hai3")
book1.countReviews()
book1.printing()