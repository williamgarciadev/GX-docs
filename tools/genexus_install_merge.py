#!/usr/bin/env python3
"""
Fusiona los hooks de grounding GeneXus en un settings.json de Claude Code SIN
pisar lo que ya exista. Lo usan los instaladores (install_global.sh y
install_global.ps1); es multiplataforma (Linux/macOS/Windows) e idempotente.

Uso:
    genexus_install_merge.py <settings.json> <grounding_cmd> <validate_cmd>

<grounding_cmd>/<validate_cmd> son las lineas de comando completas a registrar
(cada instalador las construye con el interprete y las rutas de su plataforma).
"""
import json
import os
import sys


def main():
    if len(sys.argv) != 4:
        print("uso: genexus_install_merge.py <settings.json> "
              "<grounding_cmd> <validate_cmd>", file=sys.stderr)
        return 2
    settings_path, g_cmd, v_cmd = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        with open(settings_path, encoding="utf-8") as f:
            cfg = json.load(f)
    except (OSError, json.JSONDecodeError):
        cfg = {}
    if not isinstance(cfg, dict):
        cfg = {}

    hooks = cfg.setdefault("hooks", {})

    def has_cmd(groups, needle):
        for grp in groups:
            for h in grp.get("hooks", []):
                if needle in (h.get("command") or ""):
                    return True
        return False

    ups = hooks.setdefault("UserPromptSubmit", [])
    if not has_cmd(ups, "genexus_grounding.py"):
        ups.append({"hooks": [{
            "type": "command", "command": g_cmd, "timeout": 10,
            "statusMessage": "Anclando respuesta en el corpus GeneXus...",
        }]})
        print("  + UserPromptSubmit: genexus_grounding.py")
    else:
        print("  = UserPromptSubmit ya registrado (sin cambios)")

    ptu = hooks.setdefault("PostToolUse", [])
    if not has_cmd(ptu, "genexus_validate.py"):
        ptu.append({"matcher": "Write|Edit", "hooks": [{
            "type": "command", "command": v_cmd, "timeout": 10,
            "statusMessage": "Validando codigo GeneXus contra el catalogo...",
        }]})
        print("  + PostToolUse(Write|Edit): genexus_validate.py")
    else:
        print("  = PostToolUse ya registrado (sin cambios)")

    dirn = os.path.dirname(os.path.abspath(settings_path))
    os.makedirs(dirn, exist_ok=True)
    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Settings actualizado: {settings_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
