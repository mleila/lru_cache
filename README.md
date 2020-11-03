# lru_cache
A python implementation of an LRU Cache with unit tests

# installation
Follow these steps to install the package to your local python environment
```bash
git clone git@github.com:mleila/lru_cache.git
pip install -e lru_cache
```

# Usage

```python
from lru_cache.auxiliary_structures import Node
from lru_cache.cache import LRUCache

# initialize the LRU
lru = LRUCache(capacity=3)

# insert nodes (keys must be hashable)
lru.put('1', 1)
lru.put('2', 2)
lru.put('3', 3)

# to view values
print(lru.dll.values)
>>> [3, 2, 1]

# the cache evicts the stalest node
lru.put('4', 4)
print(lru.dll.values)
>>> [4, 3, 2]

# to get a node
value = lru.get('4')
print(value)
>>> 4

# you can delete a node directly by
lru.delete('2')
print(lru.dll.values)
>>> [4, 3]

# to reset the cache
lru.reset_cache()
print(lru.dll.values)
>>> []
```

# Unit Tests
to run unit tests
```bash
python lru_cache/unitTests
```
