from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        try:
            category = next(filter(lambda c: c.id == category_id, self.categories))
        except StopIteration:
            return None

        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        try:
            topic = next(filter(lambda t: t.id == topic_id, self.topics))
        except StopIteration:
            return None

        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
        except StopIteration:
            return None

        document.edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        try:
            category = next(filter(lambda c: c.id == category_id, self.categories))
        except StopIteration:
            return None

        self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        try:
            topic = next(filter(lambda t: t.id == topic_id, self.topics))
        except StopIteration:
            return None

        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
        except StopIteration:
            return None

        self.documents.remove(document)

    def get_document(self, document_id) -> [Document, None]:
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
        except StopIteration:
            return None

        return document

    def __repr__(self):
        return '\n'.join(str(d) for d in self.documents)

