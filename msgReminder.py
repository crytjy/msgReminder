from twilio.rest import Client
import itchat

# 登录
itchat.auto_login(hotReload=True)
# 登录时向助手推送消息
itchat.send('Hello, 已开启消息通知！', toUserName='filehelper')
# 填写你关注的好友备注（此处以小明为例）
my_friend = itchat.search_friends(name=u'小明')
fromUserName = my_friend[0]['UserName']
# 控制第一次收到信息时需通知
isCall = True


# 调用Twilio，电话通知
def goddessCallMe():
    # twilio SID
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # twilio token
    auth_token = "XXXXXXXXXXXXXXXXXXXXX"
    # twilio 申请的号码
    twilioNumber = "XXXXXXXXXXXXX"
    # twilio 验证的手机号
    myNumber = "XXXXXXXXXXXXXXXXX"

    client = Client(account_sid, auth_token)
    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=myNumber,
        from_=twilioNumber
    )
    print(call.sid)
    global isCall
    isCall = False



@itchat.msg_register([itchat.content.TEXT, itchat.content.PICTURE, itchat.content.RECORDING, itchat.content.ATTACHMENT, itchat.content.VIDEO])
def get_msg(msg):
    global isCall
    if msg['FromUserName'] == fromUserName and isCall == True:
        goddessCallMe()



itchat.run()
