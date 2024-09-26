from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from pyquery import PyQuery

os.environ["OPENAI_KEY"] = "sk-TFKiWXbqHc9QM9F70e8aBdA8E3C44f5d8dF5946e5645E9B2"
os.environ["OPENAI_API_BASE"] = "https://ai-yyds.com/v1"

# 调用AI预测
def football_predict(match_info, custom_prompt):
    api_base = os.getenv("OPENAI_API_BASE")
    api_key = os.getenv("OPENAI_KEY")
    llm = OpenAI(
        model="gpt-3.5-turbo-instruct",
        temperature=0,
        openai_api_key=api_key,
        openai_api_base=api_base,
        max_tokens=1024
        )
    if len(custom_prompt) > 0:
        return llm.predict(custom_prompt)
    else:
        prompt = PromptTemplate.from_template("假如你是一名足球预测师,请预测{match_info}的比赛结果，可以参考球队近况、历史对阵、欧洲赔率、亚洲赔率等，只输出预测比分及胜负。")
        message = prompt.format(match_info=match_info)
        return llm.predict(message)
# 查询联赛队伍
def team_query(match_league):
    result = []
    pyquery = PyQuery(url=f"https://tiyu.baidu.com/match/{match_league}/tab/赛程", encoding="utf-8")
    for item in pyquery(".status-text").parent().parent().parent().parent().parent().parent().items():
        pyquery1 = PyQuery(item)
        day = pyquery1(".date").text()
        for item1 in pyquery1(".c-line-clamp").prev().items():
            time = item1.text()
            match = match_league + item1.next().text()
            team = PyQuery(item1.parent().parent().next())(".c-line-clamp1").text().replace(" ", "对阵")
            result.append(day + " " + time + " " + match + " " + team)
    return result