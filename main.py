import telebot
from telebot import types
import random

TOKEN = '5899994681:AAGVLwlciwLGudDyibAa1rLLcOHXbzSY03M'
bot = telebot.TeleBot(TOKEN)

db = {
    '😂': [
        'https://i.pinimg.com/originals/fe/11/34/fe11344710966254bc4052a73acc42e1.jpg',
        'https://www.meme-arsenal.com/memes/f84094758ea891cf6d32f709942037a0.jpg',
        'https://sun9-35.userapi.com/impf/_oMMICgJkuCtADkFm1SbHXp8FEJEbmvcIEaIVg/HH24iD13lhw.jpg?size=466x604&quality=96&sign=464aef44ab7f8b74fdd59994d6d8b92b&type=album',
        'https://memepedia.ru/wp-content/uploads/2018/09/2fb0e0593a6a0a07de957de7bf14fe3b.jpg',
        'https://www.meme-arsenal.com/memes/ff09448201acd4f295d20da036a269a0.jpg',
        'https://i.ibb.co/0hX7tP3/photo-2023-05-20-14-03-08.jpg',
        'https://cs.pikabu.ru/post_img/2013/06/02/10/1370192174_35567040.jpg',
        'https://memesmix.net/media/created/jxjw9i.jpg',
        'https://www.meme-arsenal.com/memes/2e2488d00ebdc667f6fd660fdb17b467.jpg',
        'https://www.meme-arsenal.com/memes/2091524444bb97a9f5e0f6ddddfdfa6b.jpg',
        'https://memesmix.net/media/created/83a62b.jpg'
        ],

    '❤️': [
        'https://i.ibb.co/XJW3F6k/photo-2023-05-20-14-02-43.jpg',
        'https://i.ibb.co/51DQgjy/photo-2023-05-20-14-02-44.jpg',
        'https://i.ibb.co/RCNXLRz/photo-2023-05-20-14-02-49.jpg',
        'https://i.ibb.co/nPfqbCT/photo-2023-05-20-14-03-00.jpg',
        'https://i.ibb.co/sQBb3h3/photo-2023-05-20-14-03-01.jpg',
        'https://i.ibb.co/gMPkLd8/photo-2023-05-20-15-02-46.jpg',
        'https://i.ibb.co/JtTntns/photo-2023-05-20-15-02-47.jpg',
        'https://i.ibb.co/6gvhv7h/photo-2023-05-20-15-02-48.jpg',
        'https://i.ibb.co/X2hWmB4/photo-2023-05-20-15-02-57.jpg',
        'https://i.ibb.co/yRvn8ZC/photo-2023-05-20-15-03-02.jpg',
        'https://i.ibb.co/pb4MMxQ/photo-2023-05-20-15-03-03.jpg',
        'https://i.ibb.co/VpghMPt/photo-2023-05-20-15-03-10.jpg',
        'https://i.ibb.co/9TfgWH2/photo-2023-05-20-15-03-13.jpg',
        'https://i.imgur.com/5nXshAU.jpeg'
        ],

    '😭': [
        'https://i.ibb.co/qDSGC3c/photo-2023-05-20-14-02-31.jpg',
        'https://i.ibb.co/Qvxf4LZ/photo-2023-05-20-14-02-33.jpg',
        'https://i.ibb.co/Jmt2H14/photo-2023-05-20-14-02-35.jpg',
        'https://i.ibb.co/djhDmCb/photo-2023-05-20-14-02-36.jpg',
        'https://i.ibb.co/kD5jxbL/photo-2023-05-20-14-02-38.jpg',
        'https://i.ibb.co/S7v3pWR/photo-2023-05-20-14-02-40.jpg',
        'https://i.ibb.co/qpt2xfw/photo-2023-05-20-14-02-41.jpg',
        'https://i.ibb.co/KVZmQR3/photo-2023-05-20-14-02-46.jpg',
        'https://i.ibb.co/8jFst7J/photo-2023-05-20-14-02-50.jpg',
        'https://i.ibb.co/j6ryPjk/photo-2023-05-20-14-03-04.jpg',
        'https://i.ibb.co/xDgsrHF/photo-2023-05-20-14-03-09.jpg',
        'https://i.ibb.co/hyWcK4z/photo-2023-05-20-15-02-32.jpg',
        'https://i.ibb.co/QfS7JZD/photo-2023-05-20-15-02-33.jpg',
        'https://i.ibb.co/G20VxDw/photo-2023-05-20-15-02-34.jpg',
        'https://i.ibb.co/qBVHMbS/photo-2023-05-20-15-02-36.jpg',
        'https://i.ibb.co/1dXkFbg/photo-2023-05-20-15-02-37.jpg',
        'https://i.ibb.co/9sj9NLw/photo-2023-05-20-15-02-41.jpg',
        'https://i.ibb.co/kx9RNbS/photo-2023-05-20-15-02-42.jpg',
        'https://i.ibb.co/b7KGsvf/photo-2023-05-20-15-02-43.jpg',
        'https://i.ibb.co/mHFhpdx/photo-2023-05-20-15-02-45.jpg',
        'https://i.ibb.co/jJtgrpv/photo-2023-05-20-15-02-53.jpg',
        'https://i.ibb.co/Zxxx2M9/photo-2023-05-20-15-02-55.jpg',
        'https://i.ibb.co/qMRDsHp/photo-2023-05-20-15-02-56.jpg',
        'https://i.ibb.co/wgL8rsW/photo-2023-05-20-15-03-04.jpg',
        'https://i.ibb.co/VBxzbnT/photo-2023-05-20-15-03-06.jpg',
        'https://i.ibb.co/9HDQfRw/photo-2023-05-20-15-03-09.jpg',
        'https://i.ibb.co/CbSmkfR/photo-2023-05-20-15-03-11.jpg'
        ],

    '😡': [
        'https://i.ibb.co/HL8J1h8/photo-2023-05-20-14-02-22.jpg',
        'https://i.ibb.co/pdPF3XF/photo-2023-05-20-14-02-28.jpg',
        'https://i.ibb.co/7vtRtrK/photo-2023-05-20-14-02-29.jpg',
        'https://i.ibb.co/6ZzgPk0/photo-2023-05-20-14-02-34.jpg',
        'https://i.ibb.co/sCkWhcf/photo-2023-05-20-14-02-39.jpg',
        'https://i.ibb.co/bHKt65q/photo-2023-05-20-14-02-42.jpg',
        'https://i.ibb.co/nfSLTn4/photo-2023-05-20-14-02-47.jpg',
        'https://i.ibb.co/xqJsCCH/photo-2023-05-20-14-02-52.jpg',
        'https://i.ibb.co/fvR8yYj/photo-2023-05-20-14-02-55.jpg',
        'https://i.ibb.co/QFwFZXn/photo-2023-05-20-14-02-59.jpg',
        'https://i.ibb.co/N3cg0W4/photo-2023-05-20-14-03-02.jpg',
        'https://i.ibb.co/5n1Fz37/photo-2023-05-20-14-03-05.jpg',
        'https://i.ibb.co/YhR3Kky/photo-2023-05-20-14-03-10.jpg',
        'https://i.ibb.co/0f8QSd3/photo-2023-05-20-14-03-12.jpg',
        'https://i.ibb.co/Jn2RqmB/photo-2023-05-20-14-03-13.jpg',
        'https://i.ibb.co/f0MtQKF/photo-2023-05-20-14-03-15.jpg',
        'https://i.ibb.co/pWnxzHL/photo-2023-05-20-15-02-29.jpg',
        'https://i.ibb.co/F70SBm4/photo-2023-05-20-15-02-30.jpg',
        'https://i.ibb.co/h8P5QQ3/photo-2023-05-20-15-02-39.jpg',
        'https://i.ibb.co/T1Y8KCd/photo-2023-05-20-15-02-50.jpg',
        'https://i.ibb.co/yRk34bV/photo-2023-05-20-15-02-51.jpg',
        'https://i.ibb.co/qrJqxck/photo-2023-05-20-15-02-59.jpg',
        'https://i.ibb.co/mGvK7bw/photo-2023-05-20-15-03-00.jpg',
        'https://i.ibb.co/Z2Wr6gq/photo-2023-05-20-15-03-07.jpg'
        ],

    '👍': [
        'https://i.ibb.co/TBMM8rV/photo-2023-05-20-15-02-28.jpg',
        'https://antislang.ru/wp-content/uploads/%D0%BB%D0%B0%D0%B9%D0%BA-1.jpg',
        'https://risovach.ru/upload/2016/03/mem/lukashenko_109349282_orig_.jpg',
        'https://vsememy.ru/wp-content/uploads/2022/07/fb7877dcc644eed286bfe0417ebcd970.jpg',
        'https://memesmix.net/media/created/v9rsow.jpg',
        'https://www.meme-arsenal.com/memes/655a82fb1750930c243d9aeffb2e4f3f.jpg',
        'https://www.meme-arsenal.com/memes/99020ecc16a789efd2411e54cc216461.jpg',
        'https://risovach.ru/upload/2014/01/mem/ot-palca-do-palca_39803755_orig_.jpeg',
        'https://risovach.ru/upload/2016/02/mem/fak_105729877_orig_.jpg',
        'https://risovach.ru/upload/2015/05/mem/terebonka-car_81790272_orig_.jpg'
        ],

    '🤦‍♀️': [
        'https://upload.wikimedia.org/wikipedia/commons/3/3b/Paris_Tuileries_Garden_Facepalm_statue.jpg',
        'https://animatika.ru/netcat_files/userfiles/3/facepalm.jpg',
        'https://i.ytimg.com/vi/cC2vKoRSw8c/maxresdefault.jpg',
        'https://memoteka.com/images/e/e2/%D0%A4%D0%B5%D0%B9%D1%81%D0%BF%D0%B0%D0%BB%D0%BC1.jpeg',
        'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDIxZDBkYjY4ZDE1ZDE3YjE1MTYzMTAzMWE0MmFkZTViNjc1ODE3MiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/YmszCwM1FV7zCI8sgL/giphy.gif'
        'https://vsememy.ru/wp-content/uploads/2022/07/a6ab773e097a96716c80eea526cbdd71.jpg',
        'https://memepedia.ru/wp-content/uploads/2017/04/Computer-Guy-Facepalm.jpg',
        'https://www.meme-arsenal.com/memes/155c11fa55bfe561ab43653f0ed317e7.jpg',
        'https://cs6.pikabu.ru/post_img/big/2015/05/14/6/1431593533_2075115178.jpeg',
        'https://img1.goodfon.ru/wallpaper/nbig/a/3e/cat-kot-koshka-moetsya-sidit.jpg'
        ],

    '😘': [
        'https://i.ibb.co/gZN20CM/photo-2023-05-20-14-02-54.jpg',
        'https://i.ibb.co/55yDZSK/photo-2023-05-20-14-02-58.jpg',
        'https://i.ibb.co/R756cFw/photo-2023-05-20-14-02-56.jpg',
        'https://i.ibb.co/9p7CrdR/photo-2023-05-20-14-03-06.jpg',
        'https://cs10.pikabu.ru/post_img/big/2018/08/30/7/1535626250124899352.jpg',
        'https://cs8.pikabu.ru/post_img/2017/07/15/5/1500098725170734744.jpg',
        'https://bronk.club/uploads/posts/2023-02/1677539353_bronk-club-p-chmok-otkritka-pinterest-45.jpg',
        'https://memepedia.ru/wp-content/uploads/2017/11/%D1%82%D1%8C%D0%BC%D0%BE%D0%BA-%D1%86%D0%BC%D0%BE%D0%BA-3.jpg',
        'https://risovach.ru/upload/2015/02/mem/pidrila-ebanaya-kotik_73653141_orig_.jpg',
        'https://cs8.pikabu.ru/images/big_size_comm/2018-01_5/1516855059130748070.jpg',
        'https://i.pinimg.com/736x/b6/00/d3/b600d3146767ecefbfcdeecfa7788d48.jpg'
        ],

    '🥳': [
        'https://i.ibb.co/VwWqCZn/photo-2023-05-20-15-02-38.jpg',
        'https://www.meme-arsenal.com/memes/797523726559b2a353e723c6c36861b4.jpg',
        'https://risovach.ru/upload/2015/12/mem/hitriy-getsbi_100108698_orig_.jpg',
        'https://risovach.ru/upload/2015/06/mem/bender_83607547_orig_.jpg',
        'https://memchik.ru//images/memes/63de83ceb1c7e3230d660471.jpg',
        'https://www.meme-arsenal.com/memes/60103265074b0890b8f4ff235b5aace0.jpg',
        'https://memesmix.net/media/created/bwbgi2.jpg',
        'https://medialeaks.ru/wp-content/uploads/2016/12/15983d5042c69e-331x419.jpg',
        'https://koshka.top/uploads/posts/2021-12/1640230389_3-koshka-top-p-kotik-s-kolpakom-3.jpg',
        'https://memepedia.ru/wp-content/uploads/2021/12/tom-hardi-tancuet.jpg'
        ],

    '😏': [
        'https://www.meme-arsenal.com/memes/31befba55f20821796ba2f4bec9f29b0.jpg',
        'https://www.meme-arsenal.com/memes/982bc68ea3e660e47519ac33f178a518.jpg',
        'https://medialeaks.ru/wp-content/uploads/2021/10/fb-dasha-2-1-600x338.jpg',
        'https://fikiwiki.com/uploads/posts/2022-02/thumbs/1644877935_43-fikiwiki-com-p-yekhidnaya-ulibka-prikolnie-kartinki-44.jpg',
        'https://www.anekdot.ru/i/caricatures/normal/22/9/19/ulybka_65476.jpg',
        'https://risovach.ru/upload/2019/11/mem/flirt_224615632_orig_.jpg',
        'https://risovach.ru/upload/2014/05/mem/danka-soblaznitel_50601954_orig_.jpeg',
        'https://i.redd.it/v6iy41vugh751.jpg'
        ],

    '🐈 Кототерапия 🐈‍⬛': [
        'https://media.tenor.com/2bBe7oH3ulsAAAAd/%D0%BA%D0%BE%D1%82%D0%B8%D0%BA-%D0%BC%D0%B8%D0%BB%D0%BE.gif',
        'https://i.gifer.com/origin/58/58719fa23c73a10ac5ed3045337b2727_w200.gif',
        'https://i.gifer.com/origin/44/44c4ac7a74ab043524502a3406084802_w200.gif',
        'https://i.gifer.com/origin/33/3330fd236463c0aabd122b43100d738f_w200.gif',
        'https://otkritkis.com/wp-content/uploads/2022/07/qgwi6.gif',
        'https://media.tenor.com/2v1aDCelTJgAAAAC/cat-cats.gif',
        'https://media.tenor.com/wL59aqQiwzAAAAAd/cat-kitty.gif',
        'https://media.tenor.com/3s-xdJ9XuhwAAAAd/love-cat-love-cats.gif',
        'https://media.tenor.com/3iOz6X7ZeDkAAAAd/cats-cats-fun.gif',
        'https://media.tenor.com/J3XKVY7E-SoAAAAd/cats-cute-cats.gif',
        'https://zasmeshi.ru/data/gif/8871-v-dome-mozhet-byt-tolko-odin-kot.gif',
        'https://zasmeshi.ru/data/gif/8864-hozyajke-nuzhno-pryatat-svoi-igrushki.gif',
        'https://zasmeshi.ru/data/gif/8841-teplaya-vodichka.gif',
        'https://zasmeshi.ru/data/gif/8821-chto-za-magiya.gif',
        'https://zasmeshi.ru/data/gif/8810-kot-s-tuflej.gif',
        'https://zasmeshi.ru/data/gif/8788-lovkost-lap-ne-bolee.gif',
        'https://zasmeshi.ru/data/gif/8774-pervyj-sneg.gif',
        'https://zasmeshi.ru/data/gif/8755-ehto-tolko-moj-hozyain.gif',
        'https://zasmeshi.ru/data/gif/8754-koshachi-dogonyalki.gif',
        'https://zasmeshi.ru/data/gif/8750-znaj-sebe-cenu.gif',
        'https://zasmeshi.ru/data/gif/8744-ya-smogu-ya-dotyanus.gif',
        'https://zasmeshi.ru/data/gif/8728-uhazhivaet-za-soboj.gif',
        'https://zasmeshi.ru/data/gif/8712-on-tolko-moj.gif',
        'https://zasmeshi.ru/data/gif/8706-kot-tozhe-tak-umeet.gif',
        'https://zasmeshi.ru/data/gif/8668-brat-za-bratom.gif',
        'https://zasmeshi.ru/data/gif/8588-horoshij-naparnik.gif',
        'https://zasmeshi.ru/data/gif/8533-ehj-voobshche-to-ehto-byl-moj-stakan.gif',
        'https://zasmeshi.ru/data/gif/8531-sila-dzhedaya.gif',
        'https://zasmeshi.ru/data/gif/8446-moi-dengi-ne-lez-svoimi-ruchkami.gif',
        'https://zasmeshi.ru/data/gif/8357-chto-za-dela-poest-normalno-ne-dayut.gif',
        'https://zasmeshi.ru/data/gif/8304-vannaya-s-cyplyatami-mechta-lyubogo-kota.gif',
        'https://zasmeshi.ru/data/gif/8262-kuryashchij-kot-gore-v-seme.gif',
        'https://zasmeshi.ru/data/gif/8244-sboj-v-sisteme.gif',
        'https://zasmeshi.ru/data/gif/8168-kogda-nahodishsya-na-vazhnom-soveshchanii.gif',
        'https://zasmeshi.ru/data/gif/8146-kogda-tvoya-devushka-skazala-chto-ne-obidelas.gif',
        'https://zasmeshi.ru/data/gif/8128-popytka-ne-pytka.gif',
        'https://zasmeshi.ru/data/gif/8096-kot-basketbolist.gif',
        'https://zasmeshi.ru/data/gif/8089-kogda-vpervye-stoish-na-shuhere.gif'
        ]
    }

no_emoji = "https://i.ibb.co/pWLB8SL/photo-2023-05-20-15-03-17.jpg"

# Меню
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton('❤️')
    item2 = types.KeyboardButton('😂')
    item3 = types.KeyboardButton('😭')
    item4 = types.KeyboardButton('😡')
    item5 = types.KeyboardButton('👍')
    item6 = types.KeyboardButton('🤦‍♀️')
    item7 = types.KeyboardButton('😘')
    item8 = types.KeyboardButton('🥳')
    item9 = types.KeyboardButton('😏')
    item10 = types.KeyboardButton('🐈 Кототерапия 🐈‍⬛')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

    bot.send_message(
        message.chat.id, "Выбирай мем\nТам внизу тыкни на emoji", reply_markup=markup
        )

# Начало работы
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет")
    main_menu(message)

# Mem'ные запросы
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        emoji = message.text
        if emoji in db.keys():
            if emoji == '🐈 Кототерапия 🐈‍⬛':
                msg = bot.send_animation(message.chat.id, random.choice(db[emoji]))
            else:
                msg = bot.send_photo(message.chat.id, random.choice(db[emoji]))
        else:
            bot.send_photo(message.chat.id, no_emoji)
            main_menu(message)


bot.infinity_polling()