from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8859778786:AAHsUtK_quRETVDxUAQPawIC5bqM3l0U_q0"

faq = {

    "prova":
    "📅 Vá em Calendário → Provas",

    "provas":
    "📅 Vá em Calendário → Provas",

    "aviso":
    "📢 Abra Avisos da Gestão",

    "avisos":
    "📢 Abra Avisos da Gestão",

    "norma":
    "📜 Consulte Normas",

    "normas":
    "📜 Consulte Normas",

    "arquivo":
    "📂 Abra Arquivos",

    "arquivos":
    "📂 Abra Arquivos",

    "evento":
    "🎉 Veja Eventos no menu principal",

    "eventos":
    "🎉 Veja Eventos no menu principal",

    "horário":
    "🕒 Consulte Horários no site",

    "horario":
    "🕒 Consulte Horários no site",

    "calendário":
    "📆 Abra Calendário Escolar",

    "calendario":
    "📆 Abra Calendário Escolar",

    "secretaria":
    "🏫 Procure a Secretaria",

    "coordenação":
    "👨‍🏫 Procure Coordenação",

    "coordenacao":
    "👨‍🏫 Procure Coordenação",

    "senha":
    "🔑 Clique em 'Esqueci minha senha' na tela de login",

    "login":
    "🔐 Faça login pela página inicial",

    "petrolino":
    "🤖 Oi! Sou o Petrolino 💙"
}


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
"""
🤖 Olá! Eu sou o Petrolino.

Posso ajudar você a encontrar informações no site e responder dúvidas frequentes.

Exemplos:

📅 provas
📢 avisos
📜 normas
📂 arquivos
🕒 horários
🎉 eventos
📆 calendário
🏫 secretaria
"""
    )


async def responder(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    texto = update.message.text.lower()

    for palavra, resposta in faq.items():

        if palavra in texto:

            await update.message.reply_text(
                resposta
            )

            return
            
await update.message.reply_text(
"""
🤔 Ainda não consegui responder sua dúvida.

Você pode:

📧 Entrar em contato com a coordenação

ou

🏫 Procurar a gestão escolar presencialmente.

Também posso ajudar com:

📅 provas
📢 avisos
📜 normas
📂 arquivos
🕒 horários
🎉 eventos
📆 calendário

💙 Estou aprendendo cada vez mais.
"""
)


def main():

    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            responder
        )
    )

    print(
        "🤖 Petrolino funcionando!"
    )

    app.run_polling()


if __name__ == "__main__":
    main()
