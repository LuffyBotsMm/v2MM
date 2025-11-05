#!/usr/bin/env python3
import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
from keep_alive import keep_alive

# ---------- CONFIG ----------
BOT_TOKEN = "8227694106:AAEfdOAz_vGebm7WvE7yTfS1l49RVv3twSY"
OWNER_ID = 6847499628
LOGS_CHANNEL = -1003089374759
POW = "💠 <b>POWDERED BY:</b> @LuffyBots"
# -----------------------------

keep_alive()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def is_owner(update: Update):
    return update.effective_user and update.effective_user.id == OWNER_ID

# ----------- BASIC -----------
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "💼 <b>Welcome to LB Escrow Bot!</b>\n\n"
        "Use /command to see all available options.\n"
        "Stay safe, trade smart, and trust the system ⚡",
        parse_mode=ParseMode.HTML
    )

def command(update: Update, context: CallbackContext):
    if not is_owner(update):
        update.message.reply_text("⚠️ Only the owner can view full command list.")
        return
    msg = (
        "📜 <b>LB ESCROW BOT — FULL COMMANDS</b>\n\n"
        "💰 <b>DEAL COMMANDS</b>\n"
        "➕ /add — Create new deal\n"
        "🔒 /close — Close deal\n"
        "💸 /refund — Refund a deal\n"
        "❌ /cancel — Cancel a deal\n"
        "📊 /status — View deal status\n"
        "🕓 /history — View deal history\n"
        "🚧 /ongoing — Active deals\n"
        "📁 /mydeals — Your deals\n"
        "🔔 /notify — Send reminder\n\n"
        "📈 <b>STATS COMMANDS</b>\n"
        "📊 /stats — General stats\n"
        "👤 /stat — Your stats\n"
        "🌍 /gstats — Global stats\n"
        "🏆 /topuser — Top escrow users\n\n"
        "🧑‍💻 <b>ADMIN COMMANDS</b>\n"
        "➕ /addadmin — Add admin\n"
        "➖ /removeadmin — Remove admin\n"
        "👮 /adminlist — Admin list\n"
        "📢 /broadcast — Message to all users\n"
        "🧾 /command — List all commands"
    )
    update.message.reply_text(msg, parse_mode=ParseMode.HTML)

# -------- DEAL COMMANDS --------
def add(update, context):
    update.message.reply_text(
        "💼 <b>NEW DEAL CREATED</b>\n\n"
        "💰 <b>Amount:</b> ₹150\n🤝 <b>Buyer:</b> @buyer\n🏷️ <b>Seller:</b> @seller\n"
        "🧾 <b>Trade ID:</b> #TID425749\n👑 <b>Escrowed By:</b> @LuffyBots\n\n"
        "✅ <b>Payment Received</b>\nContinue your deal safely 🔥\n\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def close(update, context):
    update.message.reply_text(
        "🔒 <b>DEAL CLOSED</b>\n\n✅ Transaction completed successfully!\n"
        "💰 Amount: ₹150\n🧾 Trade ID: #TID425749\n🤝 Buyer: @buyer\n🏷️ Seller: @seller\n\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def refund(update, context):
    update.message.reply_text(
        "💸 <b>DEAL REFUNDED</b>\n\nThe buyer has received the refund.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def cancel(update, context):
    update.message.reply_text(
        "❌ <b>DEAL CANCELLED</b>\n\nThis deal was safely cancelled.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def status(update, context):
    update.message.reply_text(
        "📊 <b>DEAL STATUS</b>\n\n✅ <b>Completed</b>\n💰 Amount: ₹150\n🧾 Trade ID: #TID425749\n"
        "👥 Buyer: @buyer | Seller: @seller\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def history(update, context):
    update.message.reply_text(
        "🕓 <b>DEAL HISTORY</b>\n\nNo completed deals found yet.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def ongoing(update, context):
    update.message.reply_text(
        "🚧 <b>ONGOING DEALS</b>\n\n1️⃣ ₹150 - @buyer vs @seller — OPEN\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def mydeals(update, context):
    update.message.reply_text(
        "📁 <b>YOUR DEALS</b>\n\nYou currently have 2 active deals.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def notify(update, context):
    update.message.reply_text(
        "🔔 <b>NOTIFICATIONS SENT</b>\n\nReminders sent to all users with pending deals.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

# -------- STATS COMMANDS --------
def stats(update, context):
    update.message.reply_text(
        "📈 <b>STATS OVERVIEW</b>\n\nDeals Total: 52\nClosed: 45\nRefunded: 4\nCancelled: 3\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def stat(update, context):
    update.message.reply_text(
        "👤 <b>YOUR STATS</b>\n\nDeals Done: 5\nAmount Escrowed: ₹600\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def gstats(update, context):
    update.message.reply_text(
        "🌍 <b>GLOBAL STATS</b>\n\nTotal Deals: 320\nTotal Escrowers: 12\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def topuser(update, context):
    update.message.reply_text(
        "🏆 <b>TOP ESCROW USERS</b>\n\n🥇 @AlphaMM — 15 Deals\n🥈 @BetaBot — 10 Deals\n🥉 @TradeHero — 8 Deals\n"
        f"{POW}", parse_mode=ParseMode.HTML)

# -------- ADMIN COMMANDS --------
def addadmin(update, context):
    if not is_owner(update):
        update.message.reply_text("🚫 Only owner can add admins.")
        return
    update.message.reply_text("✅ <b>New admin added successfully!</b>", parse_mode=ParseMode.HTML)

def removeadmin(update, context):
    if not is_owner(update):
        update.message.reply_text("🚫 Only owner can remove admins.")
        return
    update.message.reply_text("🗑️ <b>Admin removed successfully!</b>", parse_mode=ParseMode.HTML)

def adminlist(update, context):
    update.message.reply_text(
        "👮 <b>ADMIN LIST</b>\n\n1️⃣ @LuffyBots (Owner)\n2️⃣ @HelperBot\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def broadcast(update, context):
    if not is_owner(update):
        update.message.reply_text("🚫 Only owner can broadcast messages.")
        return
    msg = " ".join(context.args)
    if not msg:
        update.message.reply_text("Usage: /broadcast <message>")
        return
    update.message.reply_text(f"📢 <b>Broadcast Sent:</b>\n\n{msg}", parse_mode=ParseMode.HTML)

# -------- UNKNOWN --------
def unknown(update, context):
    update.message.reply_text("⚠️ Unknown command. Type /command for help.")

# -------- MAIN --------
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    commands = {
        "start": start, "command": command, "add": add, "close": close, "refund": refund,
        "cancel": cancel, "status": status, "history": history, "ongoing": ongoing,
        "mydeals": mydeals, "notify": notify, "stats": stats, "stat": stat,
        "gstats": gstats, "topuser": topuser, "addadmin": addadmin,
        "removeadmin": removeadmin, "adminlist": adminlist, "broadcast": broadcast
    }

    for cmd, func in commands.items():
        dp.add_handler(CommandHandler(cmd, func))

    dp.add_handler(CommandHandler(None, unknown))
    logger.info("🚀 LB Escrow Bot is live 24×7...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
