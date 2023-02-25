class Tag:
    def __init__(self):
        self.tag = "tag"
        self.is_solo = False

    def get_html(self):
        if self.is_solo:
            return f"<{self.tag}/>"
        else:
            return f"<{self.tag}></{self.tag}>"


class Image(Tag):
    def __init__(self):
        super().__init__()
        self.tag = "img"
        self.is_solo = True


class Link(Tag):
    def __init__(self):
        super().__init__()
        self.tag = "a"
        self.is_solo = False


class Input(Tag):
    def __init__(self):
        super().__init__()
        self.tag = "input"
        self.is_solo = False


class Paragraph(Tag):
    def __init__(self):
        super().__init__()
        self.tag = "p"
        self.is_solo = False


class EmptyTag(Tag):
    def __init__(self):
        super().__init__()
        self.tag = "tag"
        self.is_solo = False


def create_tag(tag_name: str) -> Tag:
    tags = {
        'img': Image,
        'a': Link,
        'p': Paragraph,
        'input': Input,
        '': EmptyTag
    }
    try:
        return tags[tag_name]()
    except KeyError:
        return Tag()


if __name__ == "__main__":
    my_tags = [
        "img",
        "input",
        "p",
        "a",
        ""
    ]

    for tag in my_tags:
        print(create_tag(tag).get_html())
