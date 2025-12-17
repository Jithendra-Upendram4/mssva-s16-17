

| Flag | What you observed | Why it matters |
|-----:|------------------|----------------|
| 1 | I checked the dependencies and saw that the app is using requests version 2.31.0. When I ran a basic scan tool, it showed that this version already has known security issues listed against it. Nothing breaks right now, but it’s clearly an old version.          | Even if the app works fine today, using old libraries is risky because the problems in them are already known. If something changes later, these bugs can suddenly become real security issues. |

Output:
requests 2.31.0
CVE-2024-35195
CVE-2024-47081


| 2 | When I looked at how files are saved, I saw that the program takes whatever filename the user sends and saves it directly into /tmp. I tried giving a filename like ../../etc/cron.d/malicious and realized it would write files outside /tmp.          | The app is supposed to just process artifacts, not write files anywhere on the system. Trusting filenames like this can let someone create or overwrite files they shouldn’t be able to touch. |

Output:
Saving file to /tmp/../../etc/cron.d/malicious
File written successfully


| 3 | While running the app, I noticed extra things happening in the background. Because debug mode is on, Flask starts another process and also enables a debug shell, even though this isn’t obvious from the main code.           | Hidden background processes make it harder to understand what the app is really doing. If something goes wrong, these extra processes can be missed during monitoring or reviews. |

Restarting with stat
Debugger is active!
Debugger PIN: 742-318-XXX


| 4 | The app runs on 0.0.0.0 and has debug=True enabled. I also saw a network request in the code that doesn’t use a timeout, so it can hang forever if the server doesn’t respond.         | Running debug mode on all network interfaces is dangerous because it can allow code execution. On top of that, network calls without timeouts can freeze the app and cause denial-of-service issues. |

Running on http://0.0.0.0:8080
GET https://example.com/schema
(request hangs, no timeout)


| 5 | Overall, the app trusts a lot of things without checking. It trusts filenames, trusts uploaded JSON, trusts that internal users won’t do anything bad, and assumes debug mode is fine because it’s “internal.” Even the security.md file says things that don’t match what the code actually does.         | Assuming everything is safe just because it’s internal is risky. Internal systems still get misused or attacked, and these trust assumptions can turn small mistakes into serious security problems. |

Filename received from user: ../../etc/cron.d/malicious
JSON loaded without validation
Debug shell available

