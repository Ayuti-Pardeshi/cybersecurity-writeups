# Running the Unicode Security Demo

This guide explains how to run the `unicode_demo.py` script included in this repository. The demo shows how hidden Unicode characters (such as Zero Width Spaces) can make two strings **look identical to humans but behave differently in code**.

---

# Prerequisites

Before running the demo, make sure you have **Python installed** on your system.

To check if Python is installed, open a terminal or command prompt and run:

```
python --version
```

or

```
python3 --version
```

If Python is installed, you should see something like:

```
Python 3.x.x
```

If Python is not installed, download it from:

https://www.python.org/downloads/

---

# Step 1: Clone or Download the Repository

If you are using Git, clone the repository:

```
git clone https://github.com/yourusername/unicode-security-demo.git
```

Then move into the project folder:

```
cd unicode-security-demo
```

Alternatively, you can download the repository as a ZIP file from GitHub and extract it.

---

# Step 2: Verify the Files

Make sure the repository contains the following file:

```
unicode_demo.py
```

This file contains the code that demonstrates hidden Unicode characters.

---

# Step 3: Run the Demo

Open a terminal in the project directory and run:

```
python unicode_demo.py
```

or if your system uses Python3:

```
python3 unicode_demo.py
```

---

# Step 4: Understanding the Output

You will see an output similar to this:

```
Normal: admin
Hidden: admin

Are they equal?
False

Length of normal string: 5
Length of hidden string: 9

Raw representation:
'a\u200bd\u200bm\u200bi\u200bn'
```

At first glance, both strings appear identical.

However:

* The **normal string** contains only 5 characters.
* The **hidden string** contains additional **Zero Width Space (U+200B)** characters.

These characters are invisible but still exist in the string.

Because of this, the two strings are **not equal** even though they look the same.

---

# Step 5: Why This Is Important

Hidden Unicode characters can cause unexpected behavior in applications.

Possible risks include:

* Input validation bypass
* Log manipulation
* Security filter evasion
* Username impersonation
* Data processing errors

Developers should always consider **Unicode normalization and sanitization** when processing user input.

---

# Optional: Run the Demo Online

If you do not want to install Python locally, you can run the code using online environments such as:

* Replit
* Google Colab
* Online Python interpreters

Simply copy the contents of `unicode_demo.py` and execute it there.

---

# Conclusion

This small experiment demonstrates how invisible Unicode characters can alter program behavior.

While emojis and Unicode make digital communication richer, they also introduce subtle complexities that developers and security engineers must understand.

Always remember:

> What looks identical to the human eye may not be identical to the system processing it.
