import copy
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Metadata:
    author: str
    created_at: datetime
    version: int


class Document:
    def __init__(self, title: str, body: str, tags: list[str], metadata: Metadata):
        self.title = title
        self.body = body
        self.tags = tags
        self.metadata = metadata
        self.history: list[str] = []


    def edit(self, new_body: str) -> None:
        self.history.append(self.body)
        self.body = new_body


    def __str__(self) -> str:
        return (
            f"'{self.title}' v{self.metadata.version} "
            f"by {self.metadata.author} "
            f"[{self.metadata.created_at.strftime('%Y-%m-%d')}]\n"
            f"Теги: {self.tags} | История: {len(self.history)} изм."
        )


    def clone(self) -> "Document":
        cloned = copy.deepcopy(self)
        cloned.metadata.version += 1
        cloned.metadata.created_at = datetime.now()
        cloned.history.clear()
        return cloned


if __name__ == "__main__":
    original = Document(
        title="Введение в Python",
        body="Python — это...",
        tags=["python", "tutorial"],
        metadata=Metadata(author="Иван", created_at=datetime(2024, 1, 1), version=1),
    )
    original.edit("Python — это отличный язык...")

    draft = original.clone()
    draft.title = "Введение в Python (черновик)"
    draft.tags.append("draft")

    print(original)
    print()
    print(draft)
