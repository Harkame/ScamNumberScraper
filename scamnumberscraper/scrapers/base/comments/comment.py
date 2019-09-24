import os


class Comment:
    username = None
    content = None
    date = None

    def __str__(self):
        to_string = "Username : "
        to_string += self.username
        to_string += os.linesep

        to_string += "Date : "
        to_string += self.date
        to_string += os.linesep

        to_string += "Content : "
        to_string += self.content
        to_string += os.linesep

        return to_string
