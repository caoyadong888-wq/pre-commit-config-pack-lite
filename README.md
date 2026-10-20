# pre-commit Config Pack (Lite)

## English

Three local hooks: trailing whitespace, a final newline check, and YAML parse. `repo: local` and `language: system` keep the run on your machine. Copy `deliverables/.pre-commit-config.yaml` to the repository root and copy `deliverables/hooks/` to `hooks/`.

`examples/settings.yaml` is a filled file the YAML hook can parse. The host is `shop.example.com`.

The full pack adds JSON, optional black, ruff, and shellcheck stubs, a remote-hook sketch with `REPLACE_WITH_REV`, a sample repository, dirty fixtures, and a checker. Check upstream docs before you pin a remote revision.

### Deliverables

- `deliverables/.pre-commit-config.yaml` — three local hooks
- `deliverables/hooks/trailing_whitespace.py` — report trailing spaces or tabs
- `deliverables/hooks/end_of_file.py` — report a missing final newline
- `deliverables/hooks/check_yaml.py` — `yaml.safe_load`
- `examples/settings.yaml` — filled YAML for shop.example.com

## 中文

三个本地钩子：行尾空白、末尾换行、YAML 解析。配置使用 `repo: local` 和 `language: system`，检查在你自己的机器上跑。把 `deliverables/.pre-commit-config.yaml` 复制到仓库根目录，把 `deliverables/hooks/` 复制为 `hooks/`。

`examples/settings.yaml` 是一份填好的 YAML，主机名是 `shop.example.com`。

完整版另外包含 JSON、black / ruff / shellcheck 占位钩子、带 `REPLACE_WITH_REV` 的远端草稿、示例仓库、失败夹具和校验器。给远端钩子写 rev 之前请 check upstream docs。

### 交付文件

- `deliverables/.pre-commit-config.yaml`
- `deliverables/hooks/trailing_whitespace.py`
- `deliverables/hooks/end_of_file.py`
- `deliverables/hooks/check_yaml.py`
- `examples/settings.yaml`

Full version: GUMROAD_URL
