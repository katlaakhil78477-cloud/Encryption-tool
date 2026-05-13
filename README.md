# Caesar Enterprise UI

Professional Caesar cipher CLI with clean Rich-based output.

## Install
```powershell
python -m pip install .
```

## Use
```powershell
caesar-cipher encrypt "JONYJACK" --key 3 --smart
caesar-cipher decrypt "Q1N8M3xNUlFCTURGTg==" --key 3
caesar-cipher crack "Q1N8M3xNUlFCTURGTg=="
```

## Notes
- `--smart` encryption stores a recovery payload.
- `decrypt` auto-detects smart payloads.
- `crack` guarantees recovery for smart payloads and ranks candidates for normal Caesar text.
