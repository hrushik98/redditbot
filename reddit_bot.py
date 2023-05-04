import requests
import streamlit as st
import praw
import os
import json
import csv
import openai 
import regex as re
import time 
import pandas as pd

api_key = st.text_input("enter openai api key")
openai.api_key = api_key
st.title("Reddit bot v1.0")

if st.button("Session Reset"):
    if os.path.exists("file9.csv"):
        os.remove("file9.csv")

        with open("file9.csv", "a") as f:
            datai = csv.writer(f)
            col1 = "postUrl"
            col2 = "context"
            col3 = "score"
            col4 = "reply"
            datai.writerow([col1, col2, col3, col4])
    else:
        with open("file9.csv", "a") as f:

            datai = csv.writer(f)
            col1 = "postUrl"
            col2 = "context"
            col3 = "score"
            col4 = "reply"
            datai.writerow([col1, col2, col3, col4])

def score_75to100():
    lst1 = []
    data2 = pd.read_csv("file9.csv", encoding='latin-1')
    for i in range(0, len(data2)):
        if str(data2['score'][i]) == "25-50":
            lst1.append(i)
        if str(data2['score'][i]) == "0-25":
            lst1.append(i)
        if str(data2['score'][i]) == "50-75":
            lst1.append(i)
        if len(str(data2['score'][i])) > 7:
            lst1.append(i)
    for i in range(0, len(data2)):
        if i in lst1:
            data2 = data2.drop(i)
    data2 = data2.reset_index()
    data3 = data2[['postUrl', 'context','score', 'reply']]
    st.write(data3)
    output_file = data3
    data3.to_csv("file10.csv")



client_id = st.text_input("Enter Client ID")
client_secret = st.text_input("Enter Client Secret")
user_agent = st.text_input("Enter User agent (format: <platform>:<app ID>:<version string> (by /u/<Reddit username>))")
user_name = st.text_input("Enter username")
password = st.text_input('Enter password', type='password')
reddit = praw.Reddit(client_id= client_id,
                      client_secret=client_secret,
                      user_agent=user_agent,
                      username=user_name,
                     password=password)


problem_statement = st.text_input("Entetr problem description")
product_description = st.text_input("Enter product description")



score_content = f""" You are a classifier that can generate a score between 0 and 100 to determine the relevancy of the  post with a passage.
The passage: {problem_statement}

How to determine the score:
- Higher is a better answer 
- Don't be overconfident!
- Just return the score and nothing else.
- Only return values from '0-25' or '25-50' or '50-75' or '75-100'


Example #1
Passage: A conifer is a tree or shrub which produces distinctive cones as part of its sexual reproduction. These woody plants are classified among the gymnosperms, and they have a wide variety of uses, from trapping carbon in the environment to providing resins which can be used in the production of solvents. Several features beyond the cones set conifers apart from other types of woody plants. A conifer is typically evergreen, although some individuals are deciduous, and almost all conifers have needle or scale-like leaves.
Reddit Post: Conifers are also characterized by their tall and straight trunks, which often have a conical shape. This shape helps the tree to shed snow in colder climates and also helps to maximize light absorption in areas with limited sunlight. Conifers are found all over the world, from the Arctic tundra to the tropical rainforest, and they are an important part of many ecosystems. One of the main uses of conifers is as a source of lumber. Many species of conifers are grown in plantations specifically for their wood, which is used in the production of paper, furniture, and construction materials. Conifers are also an important source of food and shelter for wildlife, with many animals relying on the cones, bark, and needles of these trees for sustenance. In addition to their practical uses, conifers are also valued for their aesthetic qualities. They are often used in landscaping and gardening, with some species, such as the Christmas tree, being particularly popular during the holiday season. The distinctive cones and needles of conifers also make them popular subjects for artists and photographers. Overall, conifers are a diverse and important group of trees and shrubs, with a wide range of practical and aesthetic uses. Their distinctive cones and needles, along with their tall and straight trunks, set them apart from other types of woody plants and make them a fascinating and valuable part of many ecosystems around the world.
Score: 75-100

Example #2
Passage: In his younger years, Ronald Reagan was a member of the Democratic Party and campaigned for Democratic candidates; however, his views grew more conservative over time, and in the early 1960s he officially became a Republican. In November 1984, Ronald Reagan was reelected in a landslide, defeating Walter Mondale and his running mate Geraldine Ferraro (1935-), the first female vice presidential candidate from a major U.S. political party.
Reddit Post: The question of whether Ronald Reagan was a Democrat has been a subject of debate for a long time. Some people believe that Reagan was a Democrat in his early years, while others believe that he was always a Republican. There are also some who argue that Reagan switched from being a Democrat to a Republican at some point in his political career. However, regardless of whether Reagan was a Democrat or a Republican, he remains one of the most iconic and influential political figures in American history. His policies and ideas have had a lasting impact on American society and continue to shape political discourse to this day. Whether he was a Democrat or a Republican, Reagan's legacy remains a vital part of American political culture, and his presidency continues to be studied and analyzed by historians and political scientists alike.
Score: 50-75

Example #3
Passage: The amount of time needed to explore Sydney and its surrounding areas depends on individual interests and travel style. A few days may be enough to see the main highlights of Sydney and take a day trip to nearby attractions like the Blue Mountains or Hunter Valley. 
Reddit Post: On your right across College Street, in the sandstone building on the corner, is the Australian Museum [3] ($12 adult/$6 children, $30 family (2+2)). This museum, which focuses on natural history, is worth a visit in its own right if you have more time in Sydney and will take a couple of hours to explore. If you're up for exploring the area by bike (one of the best ways to do so as much of it is parkland), take the train to Concord West station on the Northern Line (red line on the Sydney Trains map-about 20-25 minutes from the city on a direct train).
Score: 25-50

Example #4
Passage: The cost to install tile in a shower can vary depending on a few factors, such as the size of the shower, the type of tile used, and the complexity of the design. On average, the cost to install tile in a shower can range from $1,000 to $3,000 or more. This cost may include the removal of any existing tile or fixtures, preparation of the shower walls and floor, and the installation of the new tile.
Reddit Post: In the context of adult body CT, the Computed Tomography Dose Index volume (CTDI vol) is commonly used to estimate the dose received by an organ that is fully encompassed by the primary radiation beam. A protocol-independent conversion coefficient is used for this purpose. However, research shows that fully encompassed organs only account for approximately 50% ± 19% of the k factor and 46% ± 24% of the q factor. This implies that the dose received by organs that are only partially encompassed by the primary radiation beam is also substantial and cannot be ignored when estimating the effective dose and risk index from the Dose Length Product (DLP). To accurately estimate the dose and risk associated with partial irradiation of organs, it is necessary to use conversion coefficients that are specific to the anatomical region being examined. In summary, the estimation of the effective dose and risk index in adult body CT requires a comprehensive understanding of the radiation dose received by both fully and partially encompassed organs and the use of appropriate conversion coefficients for the anatomical region under examination.
Score: 0-25
"""

reply_content = f"""You are a sales agent propsecting on Reddit for a product.
Your task is to generate replies to the given Reddit posts, that will help generate interest for your product. Don't mention that you're a sales agent. Your sales pitch should feel like a recommendation rather than a sales pitch.
Also include our website: https://thesales.io and also a link to our demo audio call with an AI sales agent: https://on.soundcloud.com/LCRvK
Don't forget to include our company's website link and the soundcloud link. 
Description of the product: {product_description}
"""

topic = st.text_input("Enter the topic")
number_of_posts = st.number_input('Enter number of posts:', value=10, min_value=10, step=10)
if st.button("Scrape"):
    subreddit = reddit.subreddit('all')
    results = subreddit.search(topic, limit=number_of_posts)
    for post in results:
        title = post.title
        content = post.selftext
        url = post.url
        content = post.selftext

        context = title + (f"\n {content}")
    
        with open("file9.csv", "a", encoding='utf-8') as f:
            col1 = url     
            col2 = context
            
            try:
                
                
                m = [{"role": "system", "content": f"{score_content}"},
                    {"role": "user", "content": f"Reddit Post:\n {col2} \nScore:\n"}]

                result = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens = 4,
                messages=m)
                score=result["choices"][0]['message']['content']
                
                time.sleep(3)
            except:
                score = "Error"
            try:
                result = re.search(r'(?<=Score: ).*', score).group(0)
                col3 = str(result)
            except:

                col3 = str(score)

            if str(col3) == "75-100":


                
                
                m2 = [
                    {"role": "system", "content": f"{reply_content}"},
                        {"role": "user", "content": f"Reddit Post: {col2}\nReply:\n"}
                    ]
                result = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    max_tokens = 350,
                    temperature = 0.3,
                    messages=m2)
                reply=result["choices"][0]['message']['content']
                col4 = str(reply)
                time.sleep(3)
            else:
                col4 = "None"
            dataii = csv.writer(f)
            dataii.writerow([col1, col2, col3, col4])
data = pd.read_csv("file9.csv", encoding='latin-1')
st.write(data)

st.write("----")

if st.button("Filter"):
    score_75to100()

st.write("----")
if st.button("Send Reply"):
    df = pd.read_csv("file10.csv")
    for i in range(0, len(df)):
        post = reddit.submission(url= str(df['postUrl'][i]))
        post.reply(str(df['reply'][i]))
        st.write("comments are being posted!")
    os.remove("file10.csv")


    


            


