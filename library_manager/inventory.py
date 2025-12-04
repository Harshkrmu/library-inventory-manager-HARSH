"""
LibraryInventory handles:
- adding books
- searching
- issuing/returning
- JSON persistence
- logging
- exception safety
"""

import json
import logging
from pathlib import Path
from typing import List, Optional

from .book import Book

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class LibraryInventory:
    def __init__(self, storage_path: Path):
        self.storage_path = Path(storage_path)
        self.books: List[Book] = []
        self._ensure_storage()
        self.load()

    def _ensure_storage(self):
        """Create file if missing."""
        try:
            if not self.storage_path.exists():
                self.storage_path.write_text("[]")
                logger.info("Created new catalog.json file.")
        except Exception as e:
            logger.error(f"Storage file creation error: {e}")

    def save(self):
        """Save current book list to JSON."""
        try:
            data = [b.to_dict() for b in self.books]
            with open(self.storage_path, "w") as f:
                json.dump(data, f, indent=4)
            logger.info("Catalog saved successfully.")
        except Exception as e:
            logger.error(f"Failed to save catalog: {e}")

    def load(self):
        """Load books from JSON file."""
        try:
            text = self.storage_path.read_text()
            if not text.strip():
                text = "[]"

            raw = json.loads(text)
            self.books = [Book(**item) for item in raw]
            logger.info("Catalog loaded successfully.")

        except json.JSONDecodeError:
            logger.error("Corrupted catalog.json. Resetting file.")
            self.storage_path.write_text("[]")
            self.books = []

        except Exception as e:
            logger.error(f"Load error: {e}")

    def add_book(self, book: Book):
        """Add new book if ISBN doesn't exist."""
        if self.search_by_isbn(book.isbn):
            raise ValueError("Book with this ISBN already exists.")
        self.books.append(book)
        self.save()
        logger.info(f"Added book: {book.title}")

    def search_by_title(self, title: str) -> List[Book]:
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self) -> List[str]:
        return [str(b) for b in self.books]
