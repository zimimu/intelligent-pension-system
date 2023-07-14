import json
import openai

openai.api_key = "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"


def ChatGPT(request):
    # 得到的是一个二进制数据
    json_str = request.body
    # 对二进制数据进行解码,解码得到json数据
    json_str = json_str.decode()
    # 将json数据转化成字典形式
    json_data = json.loads(json_str)
    print(json_data)

    text_words = json_data["content"]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text_words}]
    )
    print("回答是：" + completion.choices[0].message.content)
    result = completion.choices[0].message.content
    return {'msg': '获取成功', "code": '200', "result": result}

