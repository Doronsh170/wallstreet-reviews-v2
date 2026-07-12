"""Makes the repo root importable so the tests can `import paste_review`."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
