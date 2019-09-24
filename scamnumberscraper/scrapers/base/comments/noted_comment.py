import os

from .comment import Comment


class NotedComment(Comment):
    like = 0
    dislike = 0

    def __str__(self):
        to_string = super().__str__()

        to_string += "Like : "
        to_string += str(self.like)
        to_string += os.linesep

        to_string += "Dislike : "
        to_string += str(self.dislike)
        to_string += os.linesep

        return to_string
