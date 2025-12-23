from telegram import Bot
from apscheduler.schedulers.background import BackgroundScheduler
import pytz
from datetime import datetime
import logging
import os

# Le token sera mis dans Railway (variable d'env)
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = "@lapassionprono"

MESSAGES = [
    """🚀 REJOINS LA PASSION VIP !

💎 30€ à vie (Lifetime)
✅ Aucun renouvellement
📊 Pronos quotidiens exclusifs
🎯 Discipline. Passion. Résultats.

👉 Message privé pour t'inscrire

#LaPassionProno""",

    """💚⚽️ REJOINS LES 50+ MEMBRES VIP !

LA PASSION VIP : l'espace privé réservé aux vrais passionnés

✓ Analyses quotidiennes
✓ Gestion bankroll complète
✓ Résultats & bilans
✓ Tickets exclusifs

💰 Prix : 30€ à VIE (une seule fois !)

👇 Message privé pour rejoindre

#LaPassionProno #VIP""",

    """⏰ LIMITE DE PLACES EN VIP BIENTÔT !

Tu regardes les gagnants et tu te demandes :
"Comment ils font ?"

🔐 LA PASSION VIP te montre EXACTEMENT comment

✅ 30€ à vie
✅ Pas d'abonnement
✅ Accès illimité
✅ Résultats garantis

Rejoins avant que ce soit complet ! 👑

👉 Message privé MAINTENANT

#LaPassionProno"""
]

bot = Bot(token=TOKEN)
message_counter = 0

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_daily_message():
    global message_counter
    try:
        message = MESSAGES[message_counter % len(MESSAGES)]
        bot.send_message(chat_id=CHANNEL_ID, text=message)
        logger.info(f"✅ Message #{message_counter + 1} posté à {datetime.now()}")
        message_counter += 1
    except Exception as e:
        logger.error(f"❌ Erreur : {e}")

scheduler = BackgroundScheduler(timezone=pytz.timezone('CET'))
scheduler.add_job(send_daily_message, 'cron', hour=10, minute=0, id='daily_promo')
scheduler.start()
logger.info("🚀 BOT LANCÉ SUR RAILWAY ! Attends 10h CET...")

try:
    while True:
        pass
except KeyboardInterrupt:
    scheduler.shutdown()
    logger.info("🛑 Bot arrêté.")
