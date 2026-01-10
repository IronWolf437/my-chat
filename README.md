# MyChat Demo

A simple terminal-based chat demo to talk with yourself or simulate multiple users. Perfect for testing ideas, debugging thoughts, or just having fun.

---

## Features

* Simulate multiple users in a single terminal
* Logs all messages to `chat.txt`
* Easy to add/remove users
* Lightweight and easy to run

---

## How to Use

1. Clone or download the repository
2. Run the Python script:

```bash
python3 myChat.py
```

3. Enter the number of users you want to simulate
4. Enter a name for each user
5. Start chatting!

* Type messages for each user
* Messages are saved in `chat.txt` in the same folder
* To exit, press `Ctrl + Z` (or implement an exit command like `exit`)

---

## Example

```text
how number of users: 2
whoAreYou: iron
whoAreYou: BMO

[iron]: Hi there!
[BMO]: Hello!
[iron]: How are you?
[BMO]: I'm good, and you?
[iron]: Doing well, thanks!
```

All messages will also be logged in `chat.txt`:

```text
[iron]: Hi there!
[BMO]: Hello!
[iron]: How are you?
[BMO]: I'm good, and you?
[iron]: Doing well, thanks!
```

---

## Notes

* This is a **demo project**, meant for personal use or learning purposes
* You can change user names, add timestamps, or improve the exit flow as you like
* No network or internet connection required
