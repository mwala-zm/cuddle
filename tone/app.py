import os
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator(os.environ.get("IBM_API_KEY"))
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(os.environ.get("IBM_URL"))


user_input = input("Enter your mood to be analysed: ")
res = ta.tone(user_input).get_result()

