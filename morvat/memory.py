import sqlite3
from datetime import datetime
from typing import List, Dict, Any
from morvat.config import config


class EpisodicCrypt:
    """Sistema de memória persistente em SQLite para registrar auditorias do Morvat."""

    def __init__(self, db_path: str = config.memory_db_path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS audits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    target_file TEXT NOT NULL,
                    entropy_score INTEGER NOT NULL,
                    findings_count INTEGER NOT NULL,
                    summary TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def record_audit(
        self, target_file: str, entropy_score: int, findings_count: int, summary: str
    ) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO audits (timestamp, target_file, entropy_score, findings_count, summary)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    datetime.now().isoformat(timespec="seconds"),
                    target_file,
                    entropy_score,
                    findings_count,
                    summary,
                ),
            )
            conn.commit()

    def get_recent_audits(self, limit: int = 10) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM audits ORDER BY id DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in cursor.fetchall()]
