# Imports
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import hashlib

# The Block class including a hash_block method
@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

@dataclass
class Counter:
	count: int = 0
	def update_count(self):
		self.count = self.count + 1

# Create a new block instance using some test data
new_block = Block(data="test", creator_id=0)

new_counter = Counter()

new_counter.update_count()
new_counter.update_count()


# Print the new_block
print("The Current Count is:", new_counter.count)
