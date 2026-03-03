import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from providers.base import BaseProvider

print("BaseProvider loaded:", BaseProvider)
print("Abstract methods:", BaseProvider.__abstractmethods__)