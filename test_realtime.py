import sys
sys.path.insert(0, ".")
from Backend.pattern_engine import PatternEngine
from Backend.model import FirstLayerDMM

print("\n" + "=" * 60)
print("PATTERN ENGINE TEST (direct)")
print("=" * 60)
pe = PatternEngine()
tests = [
    "who is elon musk",
    "what is the current pm of india",
    "what is today's news",
    "tell me the latest news about ai",
    "what is the weather in delhi",
    "how are you",
    "what is python",
]
for q in tests:
    result = pe.handle(q)
    print(f"  {q!r}")
    print(f"    -> {result}")

print("\n" + "=" * 60)
print("ROUTER TEST (end-to-end)")
print("=" * 60)
for q in tests:
    result = FirstLayerDMM(q)
    print(f"  {q!r}  ->  {result}")

print("\n" + "=" * 60)
print("MONITOR STATS")
print("=" * 60)
from Backend.monitor import get_monitor
s = get_monitor().stats()
print(f"  Total Queries: {s['total_queries']}")
print(f"  Layer Distribution: {s['layer_distribution']}")
print(f"  Intent Distribution: {s['intent_distribution']}")
