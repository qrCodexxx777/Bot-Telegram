import telebot
import os
import certifi
import threading
import time
import re
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

TOKEN = "8226952713:AAEB_wgNsUr53QpFh9gCB4TqmAiPAt3rbxM"

session = requests.Session()
session.verify = certifi.where()

bot = telebot.TeleBot(TOKEN, num_threads=8)

import telebot.apihelper as apihelper
apihelper.SESSION = session

PASTA = os.path.dirname(os.path.abspath(__file__))

VIDEO1_FILE_ID = None
VIDEO2_FILE_ID = None
VIDEO3_FILE_ID = None
VIDEO4_FILE_ID = None

VIDEO1 = None
VIDEO2 = None
VIDEO3 = None
VIDEO4 = None

for arquivo in os.listdir(PASTA):
    caminho = os.path.join(PASTA, arquivo)
    if not os.path.isfile(caminho) or not arquivo.lower().endswith(".mp4"):
        continue
    match = re.search(r'(\d+)', arquivo)
    numero = int(match.group(1)) if match else 0
    if numero == 4:
        VIDEO4 = caminho
    elif numero == 3:
        VIDEO3 = caminho
    elif numero == 2:
        VIDEO2 = caminho
    elif numero == 1:
        VIDEO1 = caminho

print(f"🎥 Vídeo 1 (/start):  {VIDEO1}")
print(f"🎥 Vídeo 2 (compra):  {VIDEO2}")
print(f"🎥 Vídeo 3 (reenvio): {VIDEO3}")
print(f"🎥 Vídeo 4 (reenvio): {VIDEO4}")

usuarios = set()

TEXTO_BOAS_VINDAS = (
    "😈 S4F4DINH4S MAKABRAS⁺¹⁸ 🔞\n\n"
    "⚠️ Mano vamos liberar pra vc acesso aqueles conteúdos q vc não acha em NENHUM lugar.𝐬𝐮𝐛𝐦𝐮𝐧𝐝𝐨 𝐝𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦. ⁺¹⁸ ⬇️🐷temos:--𝙑𝙄‌𝘿𝙀𝙊𝙎 𝘼𝘽𝙎𝙐𝙍𝘿𝙊𝙎 𝘾𝙈 𝙎𝘼𝙉𝙏𝙄𝙉𝙃𝘼𝙎 𝙀 𝙎𝘼𝙁𝘼𝘿𝘈𝙎--🚫𝗨𝗡𝗜𝗩𝗘𝗥𝗦𝗜𝗧𝗔𝗥𝗜𝗔𝗦, 𝗣𝗥𝗢𝗙𝗘𝗦𝗦𝗢𝗥𝗘𝗦 𝗖𝗢𝗠 𝗔𝗟𝗨𝗡𝗔𝗦⁺¹⁸ 📚🚫𝗜𝗡𝗖𝗘𝗦𝗧𝗢 𝗦𝗨𝗝𝗢𝗦 𝗥𝗘𝗔𝗜𝗦⁺¹⁸ 🐷 🚫𝗦𝗨𝗥𝗨𝗕𝗔 𝗲𝗻𝘁𝗿𝗲 𝗣𝗥𝗜𝗠𝗢𝗦 𝗘 𝗜𝗥𝗠𝗔𝗢𝗦⁺¹⁸ 🦊🚫𝗣𝗨𝗡𝗛𝗘𝗧𝗔 𝗚𝗨𝗜𝗔𝗗𝗔 𝗔𝗧𝗘 𝗩𝗖 𝗚𝗢𝗭𝗔𝗥 💦🚫𝗣𝗔𝗜𝗗𝗥𝗔𝗦𝗧𝗢 𝗙𝗨𝗗𝗘𝗡𝗗𝗢 𝗔 𝗙𝗙𝗹𝗟_H𝗔⁺¹⁸ 😱🚫𝗠𝗔𝗘 𝗠𝗔𝗦𝗧𝗨𝗥𝗕𝗔𝗡𝗗𝗢 𝗙𝗹𝗟_H𝗢⁺¹⁸ 🍆👹𝗩𝗜𝗣 𝗖𝗢𝗠 𝟲𝟳𝟱,𝟴𝟳𝟱 𝗠𝗜𝗟𝗟 𝗠𝗶𝗗𝗜𝗔𝗦 𝗥𝗔𝗥𝗢𝗦⁺¹⁸ 🔐 ➕ 𝔼 𝕞𝕦𝕚𝕥𝕠 𝕞𝕒𝕚𝕤 ... 🤫🙈𝗕𝗼𝗻𝘂𝘀 𝘃𝗶𝘁𝗮𝗹𝗶𝗰𝗶𝗼: Ⓜ️ 9.7T.B no link do ega ❌🚨 (𝘀𝗲𝗺 𝘀𝗲𝗻𝗵𝗮 𝗱𝗲 𝗮𝗰𝗲𝘀𝘀𝗼)🤫 𝘚𝘪𝘨𝘪𝘭𝘰 𝘵𝘰𝘵𝘢𝘭, 𝗚𝗥𝗨𝗣𝗢 𝘢 𝘱𝘳𝘰𝘷𝘢 𝘥𝘦 𝘲𝘶𝘦𝘥𝘢𝘴. 𝘛𝘖𝘋𝘖𝘚 𝘰𝘴 𝘤𝘰𝘯𝘦ú𝘥𝘰𝘴 𝘦𝘯𝘷𝘪𝘢𝘥𝘰𝘴 𝘴ã𝘰 100% 𝘙𝘌𝘈𝘐𝘚⁺¹⁸ ✅ temos atualizações diárias ⬇️😈 𝗘𝗡𝗧𝗥𝗘 𝗡𝗔 𝗦𝗔𝗟𝗔 𝗔𝗚𝗢𝗥𝗔⁺¹⁸ 😈⬇️"
)

TEXTO_REENVIO = (
    "😈 S4F4DINH4S GOSTOSAS⁺¹⁸ 🔞\n\n"
    "Acesso vip te espera com + de 800 mídias😈💜- ⭐️Acesso a vídeos sem censura com a filha💜- 💦Se masturbando e gozando juntas 💜- 🍆Brincadeiras eróticas com seguidores💜- 👌Midias pesadas (pezinhos, boquete, anal e mais)💜- 🔥Transando com dois💜- 🎥Filha safada fudendo gostoso com primo🎁BRINDES PROI**DOS(SÓ HOJE)🔞Primo gozando tudo dentro de nós duas... 💦🔞Tio pegando a gente no flagra e comendo as duas... 🔞⚡️Acesso Instantâneo🤝30 dias de Garantia⚠️Vagas limitadas acesso total a exclusividade e com gozada garantida!"
)

TEXTO_PACOTE = (
    "Promoçãoooo... Adicione esses pacotes exclusivos!\n\n"
    "Grupo de acesso imediato, conteúdo atualizado diariamente, e o melhor: 100% REAL! 🚀\n\n"
    "💎 *O que você ganha?*\n"
    "✅ Acesso a vídeos sem censura\n"
    "✅ Conteúdos exclusivos que você não encontra em nenhum lugar\n"
    "✅ Atualizações diárias\n"
    "✅ Garantia de satisfação\n\n"
    "⚠️ *Importante:*\n"
    "O acesso é liberado manualmente após a confirmação do pagamento, então pode levar um tempinho para processar, mas fique tranquilo que é 100% real e garantido! 🙌"
)

INTERVALO_REENVIO = 10 * 60  # 10 minutos

ADMIN_ID = 5470121122  # ✏️ Coloque seu chat_id de admin aqui (pegue com @userinfobot)
LINK_GRUPO_FREE = "https://t.me/Vazaadiinhoos"  # ✏️ Link do grupo free
TEXTO_LINK_LIBERADO = (
    "🎉 *Pagamento confirmado!*\n\n"
    "Aqui está o seu acesso ao grupo free:\n"
    f"👉 {LINK_GRUPO_FREE}\n\n"
    "Obrigado pela confiança! 🙏"
)

CHAVES_PIX = {
    "dias3":    "CHAVE_PIX_DIAS3_NORMAL",
    "vitalicio":"CHAVE_PIX_VITALICIO_NORMAL",
    "darkweb":  "CHAVE_PIX_DARKWEB_NORMAL",

    "dias3_plus":    "CHAVE_PIX_DIAS3_PLUS",
    "vitalicio_plus":"CHAVE_PIX_VITALICIO_PLUS",
    "darkweb_plus":  "CHAVE_PIX_DARKWEB_PLUS",
}

PACOTES = {
    "dias3": {
        "nome": "3 DIAS 30% OFF  por R$ 7.94 Com mais de 200 mídias exclusivas",
        "emoji": "🌟",
        "botao": "💥 3 DIAS 30% OFF💥",
        "valor_base": 7.94,
        "acrescimo": 6.00,
    },
    "vitalicio": {
        "nome": "VITALÍCIO + BÔNUS EXCLUSIVOS, acesso para sempre",
        "emoji": "🔥",
        "botao": "🔥 Vitalicio + BONUS🔥 por R$ 9.94",
        "valor_base": 15.60,
        "acrescimo": 5.00,
        "bonus": "🎁 Planos de bônus incríveis inclusos!",
    },
    "darkweb": {
        "nome": "DARK WEB +18 com acesso a conteúdos ultra exclusivos",
        "emoji": "💀",
        "botao": "DARK WEB +18 💀 por R$ 19.94",
        "valor_base": 23.67,
        "acrescimo": 7.00,
        "bonus": "🗂 +15 pastas disponíveis com grupo de entrada!",
    },
}

def formatar_valor(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def texto_pagamento(key, com_acrescimo: bool):
    p = PACOTES[key]
    valor = p["valor_base"] + p["acrescimo"] if com_acrescimo else p["valor_base"]

    chave_key = f"{key}_plus" if com_acrescimo else key
    chave = CHAVES_PIX.get(chave_key, "CHAVE_PIX_AQUI")

    linhas = [
        f"⭐ Você selecionou o seguinte plano:\n",
        f"🎁 Plano: {p['emoji']} {p['nome']} {p['emoji']}\n",
        f"💲 Valor: {formatar_valor(valor)}\n",
    ]
    if p.get("bonus"):
        linhas.append(f"{p['bonus']}\n")
    linhas += [
        f"💎 Pague via Pix Copia e Cola (ou QR Code em alguns bancos):\n",
        f"`{chave}`\n",
        f"👆 Toque na chave PIX acima para copiá-la\n",
        f"Após efetuar o pagamento, clique no botão abaixo ⤵️",
    ]
    return "\n".join(linhas)

def teclado_catalogo():
    markup = InlineKeyboardMarkup(row_width=1)
    for key, p in PACOTES.items():
        markup.add(InlineKeyboardButton(p["botao"], callback_data=f"ver_{key}"))
    return markup

def _enviar_video(chat_id, file_id_ref, caminho, caption, reply_markup=None):
    if file_id_ref:
        bot.send_video(chat_id, file_id_ref, caption=caption, reply_markup=reply_markup)
        return file_id_ref
    elif caminho:
        try:
            with open(caminho, "rb") as v:
                resp = bot.send_video(chat_id, v, caption=caption, timeout=120, reply_markup=reply_markup)
                fid = resp.video.file_id
                print(f"✅ file_id salvo: {fid}")
                return fid
        except Exception as e:
            print(f"Erro ao enviar vídeo ({caminho}): {e}")
            bot.send_message(chat_id, caption, reply_markup=reply_markup)
    else:
        bot.send_message(chat_id, caption, reply_markup=reply_markup)
    return file_id_ref

def enviar_video1(chat_id, caption, reply_markup=None):
    global VIDEO1_FILE_ID
    VIDEO1_FILE_ID = _enviar_video(chat_id, VIDEO1_FILE_ID, VIDEO1, caption, reply_markup)

def enviar_video2(chat_id, caption, reply_markup=None):
    global VIDEO2_FILE_ID
    VIDEO2_FILE_ID = _enviar_video(chat_id, VIDEO2_FILE_ID, VIDEO2, caption, reply_markup)

def enviar_video3(chat_id, caption, reply_markup=None):
    global VIDEO3_FILE_ID
    VIDEO3_FILE_ID = _enviar_video(chat_id, VIDEO3_FILE_ID, VIDEO3, caption, reply_markup)

def enviar_video4(chat_id, caption, reply_markup=None):
    global VIDEO4_FILE_ID
    VIDEO4_FILE_ID = _enviar_video(chat_id, VIDEO4_FILE_ID, VIDEO4, caption, reply_markup)

def loop_reenvio():
    while True:
        time.sleep(INTERVALO_REENVIO)
        if not usuarios:
            continue
        print(f"📤 Reenviando para {len(usuarios)} usuário(s)...")
        for chat_id in list(usuarios):
            try:
                enviar_video3(chat_id, caption=TEXTO_REENVIO)
                time.sleep(0.5)
                enviar_video4(chat_id, caption="👇 Veja os pacotes disponíveis:", reply_markup=teclado_catalogo())
            except Exception as e:
                print(f"Erro ao reenviar para {chat_id}: {e}")
            time.sleep(0.3)

thread_reenvio = threading.Thread(target=loop_reenvio, daemon=True)
thread_reenvio.start()

@bot.message_handler(commands=['meuid'])
def meu_id(message):
    bot.send_message(
        message.chat.id,
        f"🆔 Seu chat_id é: `{message.from_user.id}`",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    usuarios.add(message.chat.id)
    enviar_video1(
        message.chat.id,
        caption=TEXTO_BOAS_VINDAS,
        reply_markup=teclado_catalogo()
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("ver_"))
def mostrar_pacote(call):
    bot.answer_callback_query(call.id)
    key = call.data.replace("ver_", "")
    pacote = PACOTES.get(key)
    if not pacote:
        return

    p = pacote
    valor_com = formatar_valor(p["valor_base"] + p["acrescimo"])
    valor_sem = formatar_valor(p["valor_base"])

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(f"✅ Adicionar — {valor_com}", callback_data=f"comprar_sim_{key}"),
        InlineKeyboardButton(f"❎ Não quero — {valor_sem}", callback_data=f"comprar_nao_{key}")
    )

    enviar_video2(call.message.chat.id, caption=f"{p['emoji']} *{p['nome']}*")
    bot.send_message(call.message.chat.id, TEXTO_PACOTE, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("comprar_sim_"))
def pagamento_com(call):
    bot.answer_callback_query(call.id)
    key = call.data.replace("comprar_sim_", "")
    if key not in PACOTES:
        return
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ Já efetuei o pagamento", callback_data=f"pago_{key}"))
    bot.send_message(call.message.chat.id, texto_pagamento(key, com_acrescimo=True), parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("comprar_nao_"))
def pagamento_sem(call):
    bot.answer_callback_query(call.id)
    key = call.data.replace("comprar_nao_", "")
    if key not in PACOTES:
        return
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ Já efetuei o pagamento", callback_data=f"pago_{key}"))
    bot.send_message(call.message.chat.id, texto_pagamento(key, com_acrescimo=False), parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("pago_"))
def confirmacao(call):
    bot.answer_callback_query(call.id)
    key = call.data.replace("pago_", "")
    pacote = PACOTES.get(key)
    nome_pacote = pacote["nome"] if pacote else key

    chat_id = call.message.chat.id
    usuario = call.from_user
    nome_usuario = usuario.first_name or "Sem nome"
    username = f"@{usuario.username}" if usuario.username else "(sem username)"

    bot.send_message(
        chat_id,
        "✅ *Pagamento em análise!*\n\n"
        "Estamos confirmando seu pagamento. Assim que cair na conta, "
        "você receberá automaticamente o link do grupo free aqui mesmo. 🙏",
        parse_mode="Markdown"
    )

    if ADMIN_ID:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("✅ Aprovar e enviar link", callback_data=f"aprovar_{chat_id}"))
        try:
            bot.send_message(
                ADMIN_ID,
                f"💰 Novo pagamento reportado!\n\n"
                f"👤 Nome: {nome_usuario}\n"
                f"🆔 Username: {username}\n"
                f"💬 Chat ID: {chat_id}\n"
                f"📦 Pacote: {nome_pacote}\n\n"
                f"Confira se o Pix caiu e aprove abaixo ⤵️",
                reply_markup=markup
            )
        except Exception as e:
            print(f"Erro ao avisar admin: {e}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("aprovar_"))
def aprovar_pagamento(call):
    if call.from_user.id != ADMIN_ID:
        bot.answer_callback_query(call.id, "Você não tem permissão.")
        return

    chat_id_destino = int(call.data.replace("aprovar_", ""))

    try:
        bot.send_message(chat_id_destino, TEXTO_LINK_LIBERADO, parse_mode="Markdown")
        bot.answer_callback_query(call.id, "Link enviado!")
        bot.edit_message_text(
            f"✅ *Aprovado!* Link enviado para o chat `{chat_id_destino}`.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode="Markdown"
        )
    except Exception as e:
        bot.answer_callback_query(call.id, f"Erro: {e}")

@bot.message_handler(commands=['liberar'])
def liberar_acesso(message):
    if message.from_user.id != ADMIN_ID:
        return

    partes = message.text.split()
    if len(partes) < 2:
        bot.send_message(message.chat.id, "⚠️ Uso correto: /liberar <chat_id>")
        return

    try:
        chat_id_destino = int(partes[1])
    except ValueError:
        bot.send_message(message.chat.id, "⚠️ chat_id inválido.")
        return

    try:
        bot.send_message(chat_id_destino, TEXTO_LINK_LIBERADO, parse_mode="Markdown")
        bot.send_message(message.chat.id, f"✅ Link enviado para {chat_id_destino}")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Erro ao enviar: {e}")

print("✅ Bot iniciado com sucesso!")

# Polling com tratamento de erro para evitar crash em conflitos
while True:
    try:
        bot.infinity_polling(timeout=20, long_polling_timeout=20, skip_pending=True)
    except telebot.apihelper.ApiTelegramException as e:
        if "409" in str(e) and "Conflict" in str(e):
            print("⚠️ Conflito detectado (outra instância rodando). Aguardando 5 segundos...")
            time.sleep(5)
        else:
            print(f"❌ Erro na API do Telegram: {e}")
            time.sleep(5)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        time.sleep(5)

