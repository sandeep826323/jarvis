import sys
from pathlib import Path

MODEL_FILE = Path(r"F:\jarvis\Backend\Model.py")
if not MODEL_FILE.exists():
    print("FILE NOT FOUND")
    sys.exit(1)

content = MODEL_FILE.read_text(encoding="utf-8")
original = content

# ============ PATCH 1: Imports ============
if "import json" not in content:
    old = "import time\nimport re\nfrom rich import print"
    new = "import time\nimport re\nimport json\nimport threading\nfrom pathlib import Path\nfrom rich import print"
    if old in content:
        content = content.replace(old, new, 1)
        print("PATCH 1: Imports added")
    else:
        print("PATCH 1: marker not found")
else:
    print("PATCH 1: already present")

# ============ PATCH 2: Config ============
if "BOOTSTRAP_FILE" not in content:
    marker = "# ================== INTENT"
    config = (
        "# ================== BOOTSTRAP CONFIG ==================\n"
        "BOOTSTRAP_DIR = Path(_PROJECT_ROOT) / 'Data' / 'bootstrap'\n"
        "BOOTSTRAP_FILE = BOOTSTRAP_DIR / 'learned_queries.json'\n"
        "BOOTSTRAP_DIR.mkdir(parents=True, exist_ok=True)\n\n\n"
        "# ================== INTENT"
    )
    if marker in content:
        content = content.replace(marker, config, 1)
        print("PATCH 2: Config added")
    else:
        print("PATCH 2: marker not found")
else:
    print("PATCH 2: already present")

# ============ PATCH 3: __init__ ============
if "_load_bootstrap_memory" not in content:
    old = "        self._api_call_counter = 0\n        self.monitor = get_monitor()"
    new = (
        "        self._api_call_counter = 0\n"
        "        self.monitor = get_monitor()\n\n"
        "        # Bootstrap memory load karo\n"
        "        self._bootstrap_memory = self._load_bootstrap_memory()\n"
        "        self._bootstrap_lock = threading.Lock()"
    )
    if old in content:
        content = content.replace(old, new, 1)
        print("PATCH 3: __init__ updated")
    else:
        print("PATCH 3: marker not found")
else:
    print("PATCH 3: already patched")

# ============ PATCH 4: Bootstrap Methods ============
if "def _learn_from_query" not in content:
    marker = "    # ---------- INTENT"
    methods = '''    # ---------- BOOTSTRAP MEMORY ----------
    def _load_bootstrap_memory(self) -> dict:
        """Disk se pehle seekhi hui queries load karo."""
        if not BOOTSTRAP_FILE.exists():
            return {}
        try:
            with BOOTSTRAP_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"[bootstrap] loaded {len(data)} learned queries")
            return data
        except Exception as e:
            print(f"[bootstrap] load failed: {e}")
            return {}

    def _save_bootstrap_memory(self):
        """Memory ko disk pe atomic write karo."""
        try:
            tmp = BOOTSTRAP_FILE.with_suffix(".tmp")
            with tmp.open("w", encoding="utf-8") as f:
                json.dump(self._bootstrap_memory, f, ensure_ascii=False, indent=2)
            tmp.replace(BOOTSTRAP_FILE)
        except Exception as e:
            print(f"[bootstrap] save failed: {e}")

    def _learn_from_query(self, query: str, commands: list, source: str):
        """Har query ko bootstrap memory me save karo."""
        if not query or not commands:
            return
        key = query.strip().lower()
        with self._bootstrap_lock:
            self._bootstrap_memory[key] = {
                "query": query,
                "commands": commands,
                "source": source,
                "ts": time.time(),
            }
        self._save_bootstrap_memory()

    # ---------- INTENT'''
    if marker in content:
        content = content.replace(marker, methods, 1)
        print("PATCH 4: Methods added")
    else:
        print("PATCH 4: marker not found")
else:
    print("PATCH 4: already present")

# ============ PATCH 5: Bootstrap Check in route() ============
if "boot_hit = self._bootstrap_memory.get" not in content:
    old = '''            self._finalize(query, pat, latency_ms=(time.time() - t0) * 1000)
            return pat["commands"]

        # ===== L5: ML ====='''
    new = '''            self._finalize(query, pat, latency_ms=(time.time() - t0) * 1000)
            return pat["commands"]

        # ===== BOOTSTRAP MEMORY CHECK =====
        boot_key = query.strip().lower()
        boot_hit = self._bootstrap_memory.get(boot_key)
        if boot_hit and boot_hit.get("commands"):
            commands = boot_hit["commands"]
            self.cache.set(query, commands, static=True)
            self._log(query, commands, layer="bootstrap",
                      latency_ms=(time.time() - t0) * 1000,
                      extra={"source": boot_hit.get("source", "?")})
            self.predictor.observe(query, commands)
            return commands

        # ===== L5: ML ====='''
    if old in content:
        content = content.replace(old, new, 1)
        print("PATCH 5: Bootstrap check added")
    else:
        print("PATCH 5: marker not found")
else:
    print("PATCH 5: already present")

# ============ PATCH 6: API Learn ============
if 'self._learn_from_query(query, commands, source="api")' not in content:
    old = '''            self.cache.set(query, commands, static=True)
            self.predictor.observe(query, commands)

        self._log(query, commands, layer="api", latency_ms=latency)'''
    new = '''            self.cache.set(query, commands, static=True)
            self.predictor.observe(query, commands)
            self._learn_from_query(query, commands, source="api")

        self._log(query, commands, layer="api", latency_ms=latency)'''
    if old in content:
        content = content.replace(old, new, 1)
        print("PATCH 6: API learn added")
    else:
        print("PATCH 6: marker not found")
else:
    print("PATCH 6: already present")

# ============ PATCH 7: FirstLayerDMM ============
if "def FirstLayerDMM" in content and "commands = _router.route(prompt)" not in content:
    old = '''def FirstLayerDMM(prompt: str = "test"):
    return _router.route(prompt)'''
    new = '''def FirstLayerDMM(prompt: str = "test"):
    commands = _router.route(prompt)
    if commands:
        _router._learn_from_query(prompt, commands, source="auto")
    return commands'''
    if old in content:
        content = content.replace(old, new, 1)
        print("PATCH 7: FirstLayerDMM updated")
    else:
        print("PATCH 7: marker not found")
else:
    print("PATCH 7: already patched")

# ============ SAVE ============
if content != original:
    MODEL_FILE.write_text(content, encoding="utf-8")
    print(f"\nSAVED: {MODEL_FILE}")
    print(f"CHANGES: {len(content) - len(original)} chars added")
else:
    print("\nNO CHANGE - already patched or markers not found")