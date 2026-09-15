# test_realtime2.py
"""
Test realtime patterns & routing end-to-end.
Run from F:\jarvis directory.
"""
import sys
import os

# Add project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

print(f"Project root: {PROJECT_ROOT}")
print(f"Backend exists: {os.path.exists(os.path.join(PROJECT_ROOT, 'Backend'))}")
print(f"model.py exists: {os.path.exists(os.path.join(PROJECT_ROOT, 'Backend', 'model.py'))}")
print()

# ---------- Test 1: Pattern Engine ----------
print("=" * 60)
print("PATTERN ENGINE TEST (direct)")
print("=" * 60)

try:
    from Backend.pattern_engine import PatternEngine
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
except Exception as e:
    print(f"❌ Pattern test failed: {e}")

# ---------- Test 2: Full Router ----------
print("\n" + "=" * 60)
print("ROUTER TEST (end-to-end)")
print("=" * 60)

try:
    from Backend.model import FirstLayerDMM
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
        result = FirstLayerDMM(q)
        print(f"  {q!r}  ->  {result}")
except Exception as e:
    print(f"❌ Router test failed: {e}")
    import traceback
    traceback.print_exc()

# ---------- Test 3: Monitor Stats ----------
print("\n" + "=" * 60)
print("MONITOR STATS")
print("=" * 60)

try:
    from Backend.monitor import get_monitor
    s = get_monitor().stats()
    print(f"  Total Queries: {s['total_queries']}")
    print(f"  Layer Distribution: {s['layer_distribution']}")
    print(f"  Intent Distribution: {s['intent_distribution']}")
except Exception as e:
    print(f"❌ Monitor test failed: {e}")