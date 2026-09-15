# fix_indent.py (v2)
"""
Fixes indentation in Frontend/GUI.py
- Monitor button block
- show_monitor method
"""
from pathlib import Path

GUI_PATH = Path("Frontend/GUI.py")


def fix_monitor_button(lines):
    """Fix monitor button block to be 8-space indented."""
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if "# === MONITOR BUTTON ===" in line:
            start_idx = i
        if start_idx is not None and "button_layout.addWidget(self.monitor_button)" in line:
            end_idx = i
            break

    if start_idx is None or end_idx is None:
        print("⚠️  Monitor button block not found")
        return False

    print(f"✅ Found monitor button block: lines {start_idx+1} to {end_idx+1}")
    for i in range(start_idx, end_idx + 1):
        s = lines[i].rstrip("\n")
        stripped = s.lstrip()
        if stripped:
            lines[i] = "        " + stripped + "\n"
    return True


def fix_show_monitor(lines):
    """Fix show_monitor method: def at 4 spaces, body at 8 spaces."""
    start_idx = None
    for i, line in enumerate(lines):
        if "def show_monitor(self):" in line:
            start_idx = i
            break

    if start_idx is None:
        print("⚠️  show_monitor not found")
        return False

    print(f"✅ Found show_monitor at line {start_idx+1}")

    # Find the end of the method: next line with exactly 4-space "def " or "class "
    end_idx = start_idx + 1
    for i in range(start_idx + 1, len(lines)):
        line = lines[i]
        # Class-level def/class marker: starts with 4 spaces + def/class
        if line.startswith("    def ") or line.startswith("    class "):
            end_idx = i
            break
    else:
        end_idx = len(lines)

    # --- Replace method body with correct version ---
    new_method = [
        "    def show_monitor(self):\n",
        '        """Show API & Layer Monitor dashboard."""\n',
        "        try:\n",
        "            if hasattr(self, '_monitor_dialog') and self._monitor_dialog.isVisible():\n",
        "                self._monitor_dialog.raise_()\n",
        "                self._monitor_dialog.activateWindow()\n",
        "                self._monitor_dialog.refresh()\n",
        "                return\n",
        "            self._monitor_dialog = MonitorDialog(self)\n",
        "            self._monitor_dialog.show()\n",
        "        except Exception as e:\n",
        '            print(f"Error showing monitor: {e}")\n',
        '            QMessageBox.warning(self, "Error", f"Failed to open monitor: {str(e)}")\n',
        "\n",
    ]

    print(f"   Replacing lines {start_idx+1} to {end_idx} with fixed method ({len(new_method)} lines)")

    lines[start_idx:end_idx] = new_method
    return True


def main():
    with GUI_PATH.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"Total lines: {len(lines)}")

    fix_monitor_button(lines)
    fix_show_monitor(lines)

    with GUI_PATH.open("w", encoding="utf-8") as f:
        f.writelines(lines)

    print("✅ Fix applied! Now run:")
    print("   python -c \"import ast; ast.parse(open('Frontend/GUI.py', encoding='utf-8').read()); print('OK')\"")


if __name__ == "__main__":
    main()