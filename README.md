# <div align="center">🚀 Encryption-tool</div>

<div align="center">

### Encryption Toolkit 🔐

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=Professional+Encryption+Toolkit;Smart+Encryption+%26+Guaranteed+Recovery;Enterprise+CLI+Security+Tool" />

<br>

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![CLI](https://img.shields.io/badge/CLI-Rich_UI-green?style=for-the-badge&logo=windows-terminal)
![Security](https://img.shields.io/badge/Security-Cipher_Tool-red?style=for-the-badge&logo=shield)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## 🌟 Overview

**Encryption** is a professional command-line encryption toolkit built for Cipher operations with an enterprise-grade UI.

Designed with modern CLI aesthetics, smart encryption support, and guaranteed recovery for tool-generated ciphertext.

---

## ✨ Features

✅ Professional colorful CLI interface  
✅ Smart encrypted payload mode  
✅ Guaranteed recovery mode  
✅ Standard Caesar encryption  
✅ Standard decryption  
✅ Automatic smart payload detection  
✅ Crack analysis mode  
✅ Rich tables & panels UI  
✅ Python 3.11+ support  
✅ Enterprise terminal experience  

---

## 📸 Preview

### Encryption

```bash
caesar-cipher encrypt "HELLO WORLD" --key 3 --smart
```

Example Output:

```text
──────────────────── ENCRYPTION RESULT ────────────────────

┌──────── Caesar Cipher Toolkit ────────┐
│ Mode    SMART GUARANTEED              │
│ Key     3                             │
│ Output  Q1N8M3xLSE9PUiBaUlVPRw==      │
└───────────────────────────────────────┘
```

### Decryption

```bash
caesar-cipher decrypt "Q1N8M3xLSE9PUiBaUlVPRw==" --key 3
```

```text
──────────────────── DECRYPTION RESULT ────────────────────

┌──────── Recovered Plaintext ──────────┐
│ Mode            SMART AUTO-DETECTED   │
│ Recovered Text  HELLO WORLD           │
└───────────────────────────────────────┘
```

### Crack Analysis

```bash
caesar-cipher crack "Q1N8M3xLSE9PUiBaUlVPRw=="
```

```text
Guaranteed Smart Recovery
┏━━━━━━━━━━┳━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Status   ┃ Key ┃ Recovered Text ┃
┣━━━━━━━━━━╋━━━━━╋━━━━━━━━━━━━━━━━┫
┃ SUCCESS  ┃ 3   ┃ HELLO WORLD    ┃
┗━━━━━━━━━━┻━━━━━┻━━━━━━━━━━━━━━━━┛
```

---

## ⚙️ Installation

Clone repository:

```bash
git clone 
```

Go into project:

```bash
cd CipherNova
```

Install:

```bash
python -m pip install . --force-reinstall --no-cache-dir
```

---

## 🚀 Usage

### Standard Encryption

```bash
caesar-cipher encrypt "HELLO WORLD" --key 3
```

### Smart Encryption

```bash
caesar-cipher encrypt "HELLO WORLD" --key 3 --smart
```

### Standard Decryption

```bash
caesar-cipher decrypt "KHOOR ZRUOG" --key 3
```

### Crack Ciphertext

```bash
caesar-cipher crack "KHOOR ZRUOG"
```

### Guaranteed Recovery

```bash
caesar-cipher crack "<smart ciphertext>"
```

---

## 🛠 Tech Stack

- Python 3.11+
- Typer
- Rich
- Base64 Encoding
- CLI Architecture

---

## 📂 Project Structure

```text
CipherNova/
│
├── src/
│   └── caesar_cipher/
│       ├── __init__.py
│       └── main.py
│
├── pyproject.toml
├── README.md
```

---

## 🔐 Security Note

Smart mode guarantees exact recovery only for tool-generated ciphertext.

Blind cracking external arbitrary ciphertext is probabilistic due to cipher ambiguity.

---

## 👨‍💻 Author

**Jagadeesh Pagoti**

GitHub: https://github.com/jagadeeshpagoti22

---

<div align="center">

### ⭐ If you like CipherNova, star the repository ⭐

</div>
