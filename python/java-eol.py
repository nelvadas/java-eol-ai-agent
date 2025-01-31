import requests
import os
import  argparse
import logging
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate



# Run the script 
# python java-eol.py -java 8
# python java-eol.py -java 1.8.0_431
# python java-eol.py -java 23.0.2
# python java-eol.py -java 23.0.1




# API call to https://java.oraclecloud.com/javaReleases to fetch EOL for jdkversion={releaseVersion} or java releaseVersion={releaseVersion}
@tool
def getOracleJavaEolSupportDate(releaseVersion: str) -> str:
    """ Get the Oracle JDK releases info : EOL Support dates , CPU, LTS status, Licence ... """
    api_url =f"https://java.oraclecloud.com/javaReleases"
    response = requests.get(api_url)
    if response.status_code ==200:
        data = response.json()
        logging.debug(f"data:{data}")
        releases= data["items"]
        customerReleases = [
            r for r in releases
             if r.get("jdkDetails", {}).get("releaseVersion") == releaseVersion
             or r.get("jdkDetails", {}).get("jdkVersion") == releaseVersion
             or releaseVersion.startswith(r.get("jdkDetails", {}).get("jdkVersion"))
        ]       
        print((f"customerReleases:{customerReleases}"))
        if len(customerReleases)<1:
            raise ValueError(f"No version {releaseVersion} found ")
            return
    
        item= customerReleases[0]
        logging.debug(f"Item:{item} ")
        return item.get("jdkDetails").get("endOfSupportLifeDate")
    else:
        raise ValueError(f"Faile to fetch EOL data for {releaseVersion}")



# Set logging level
logging.basicConfig(level=logging.INFO)

#load OPENAI KEY 

openai_api_key = os.environ.get("OPENAI_API_KEY")

# Create a utility to fectch JDK EOL support date from Oracle public JAva Releases API

tools=[getOracleJavaEolSupportDate]

# LLM 

llm = ChatOpenAI(api_key=openai_api_key,model_name="gpt-4o", temperature=0)

# Agent 
agent =create_react_agent(llm,tools=tools )

# Get the java version from command line 

parser = argparse.ArgumentParser(description="AI Agent with OpenAI that provide JDK EOL dates")
parser.add_argument("-java", "--jdk", type=str, required=True, help="Java Version e.g 8")
args = parser.parse_args()


query = f" What is the Oracle EOL Support date for Java {args.jdk}?"

logging.info(f"jdk={args.jdk}")
messages = agent.invoke({"messages": [("human", query)]})
print(f"query: {query} \nresponse:{messages['messages'][-1].content}")


