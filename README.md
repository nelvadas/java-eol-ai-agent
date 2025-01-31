# Java AI EOL Agent

This repository includes a demo lab on using function calling with LLMs, featuring an AI-powered agent that queries the [Oracle Java Releases API](https://docs.oracle.com/en-us/iaas/jms/doc/public-api-oracle-java-releases.html) to retrieve JDK End-of-Life (EOL) dates and other version details. 
to retrieve JDK End-of-Life (EOL) dates and version details.

```sh
git clone https://github.com/nelvadas/java-eol-ai-agent.git
```


## Python version

Move to python subfolder
```sh
cd python
```

Install requirements
```sh
pip install -r requirements.txt
```
Run a sample

```sh
java-eol-ai-agent/python on  main [!] via 🐍 v3.12.4 on ☁️  (us-east-2)
❯ python java-eol.py -java 8
INFO:root:jdk=8
...
 query:  What is the Oracle EOL Support date for Java 8?
response:The Oracle EOL (End of Life) Support date for Java 8 is December 31, 2030.

```

```sh
java-eol-ai-agent/python on  main [!] via 🐍 v3.12.4 on ☁️  (us-east-2)
❯ python java-eol.py -java 23.0.2
INFO:root:jdk=23.0.2
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
...
query:  What is the Oracle EOL Support date for Java 23.0.2?
response:The Oracle EOL (End of Life) Support date for Java 23.0.2 is March 17, 2025.
```

The [command.ipynb](./python/commands.ipynb) is exploring various agentic options like Executor Framework and langgraph react agents.


## Java Version

(coming soon)




## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.
🔗 License: MIT | 📜 API Reference: Oracle Java Releases API
Let me know if you want any refinements! 🚀