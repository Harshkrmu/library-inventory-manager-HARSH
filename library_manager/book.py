"""
Book class for Library Inventory Manager.
Implements core OOP methods and attributes.
"""

from dataclasses import dataclass, asdict


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    status: str = "available"   # available or issued

    def __post_init__(self):
        self.title = self.title.strip()
        self.author = self.author.strip()
        self.isbn = self.isbn.strip()

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self) -> dict:
        """Return dict format for JSON serialization."""
        return asdict(self)

    def issue(self) -> bool:
        """Mark book as issued."""
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self) -> bool:
        """Mark book as returned."""
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self) -> bool:
        return self.status == "available"
