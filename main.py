#!/usr/bin/env python3
import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
from keep_alive import keep_alive

# ========== CONFIG ==========
BOT_TOKEN = "8232044234:AAG0Mm6_4N7PtK-mPsuNUh3sgeDp5A-OjE8"
OWNER_ID = 6847499628
LOGS_CHANNEL = -1003089374759
POW = "<b>POWDERED BY:</b> @LuffyBots"
# ============================

keep_alive()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_owner(update: Update):
    return update.effective_user and update.effective_user.id == OWNER_ID

# ------------- BASE COMMANDS -------------
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "💼 <b>LB Escrow Bot Active</b>\n\nUse /command to view all features.",
        parse_mode=ParseMode.HTML
    )

def command(update: Update, context: CallbackContext):
    if not is_owner(update):
        update.message.reply_text("⚠️ Only the owner can access all commands.")
        return
    msg = (
        "📜 <b>LB Escrow Bot — Command List</b>\n\n"
        "💰 <b>Deal Commands</b>\n"
        "/add — Start new deal\n"
        "/close — Close deal\n"
        "/refund — Refund deal\n"
        "/cancel — Cancel deal\n"
        "/status — Check deal status\n"
        "/history — Deal history\n"
        "/ongoing — Show open deals\n"
        "/mydeals — Show your deals\n"
        "/notify — Notify pending users\n\n"
        "🧮 <b>Stats Commands</b>\n"
        "/stats — General stats\n"
        "/stat — Personal stats\n"
        "/gstats — Global stats\n"
        "/topuser — Top escrow user\n\n"
        "🧑‍💻 <b>Admin Commands</b>\n"
        "/addadmin — Add admin\n"
        "/removeadmin — Remove admin\n"
        "/adminlist — List admins\n"
        "/broadcast — Broadcast to all"
    )
    update.message.reply_text(msg, parse_mode=ParseMode.HTML)

# -------- Deal Commands --------
def add(update, context):
    update.message.reply_text(
        "💼 <b>NEW DEAL CREATED</b>\n\n"
        "💰 Amount: ₹150\n🤝 Buyer: @buyer\n🏷️ Seller: @seller\n🧾 Trade ID: #TID425749\n👑 Escrowed By: @LuffyBots\n\n"
        "✅ Payment Received\nContinue your deal safely 🔥\n\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def close(update, context):
    update.message.reply_text(
        "🔒 <b>DEAL CLOSED</b>\n\n✅ Transaction completed successfully!\n"
        "🧾 Trade ID: #TID425749\n💰 Amount: ₹150\n🤝 Buyer: @buyer\n🏷️ Seller: @seller\n\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def refund(update, context):
    update.message.reply_text(
        "💸 <b>DEAL REFUNDED</b>\n\nAmount refunded successfully!\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def cancel(update, context):
    update.message.reply_text(
        "❌ <b>DEAL CANCELLED</b>\n\nThis deal was safely cancelled.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def status(update, context):
    update.message.reply_text(
        "📊 <b>DEAL STATUS</b>\n\n✅ Active Deal\n💰 Amount: ₹150\n🧾 Trade ID: #TID425749\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def history(update, context):
    update.message.reply_text(
        "🕒 <b>DEAL HISTORY</b>\n\nNo previous deals found yet.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def ongoing(update, context):
    update.message.reply_text(
        "🚧 <b>ONGOING DEALS</b>\n\n1️⃣ @buyer vs @seller — ₹150 (OPEN)\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def mydeals(update, context):
    update.message.reply_text(
        "📁 <b>YOUR DEALS</b>\n\nYou currently have 0 active deals.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def notify(update, context):
    update.message.reply_text(
        "🔔 <b>NOTIFICATION SENT</b>\n\nBuyers and sellers have been reminded of pending deals.\n"
        f"{POW}", parse_mode=ParseMode.HTML)

# -------- Stats Commands --------
def stats(update, context):
    update.message.reply_text(
        "📊 <b>STATS</b>\n\nTotal Deals: 20\nClosed: 18\nRefunded: 2\nCancelled: 0\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def stat(update, context):
    update.message.reply_text(
        "👤 <b>YOUR STATS</b>\n\nDeals Done: 4\nAmount Escrowed: ₹450\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def gstats(update, context):
    update.message.reply_text(
        "🌍 <b>GLOBAL STATS</b>\n\nTotal Deals: 100\nEscrowers Active: 12\n"
        f"{POW}", parse_mode=ParseMode.HTML)

def topuser(update, context):
    update.message.reply_text(
        "🏆 <b>TOP ESCROW USERS</b>\n\n🥇 @AlphaMM — 10 Deals\n🥈 @BetaEscrow — 8 Deals\n🥉 @GammaTrade — 6 Deals\n"
        f"{POW}", parse_mode=ParseMode.HTML)

# -------- Admin Commands --------
def addadmin(update, context):
    if not is_owner(update):
        update.message.reply_text("🚫 Only owner can add admins.")
        return
    update.message.reply_text("✅ New admin added successfully!")

def removeadmin(update, context):
    if not is_owner(update):
        update.message.reply_text("🚫 Only owner can remove admins.")
        return
    update.message.reply_text("🗑️ Admin removed successfully.")

def adminlist(update, context):
    update.message.reply_text("👮 <b>ADMIN LIST</b>\n\n1️⃣ @LuffyBots (Owner)\n2️⃣ @HelperBot\n"
                              f"{POW}", parse_mode=ParseMode.HTML)

def broadcast(update, context):
    if not is_owner(update):
        update.message.reply_text("🚫 Only owner can broadcast messages.")
        return
    msg = " ".join(context.args)
    if not msg:
        update.message.reply_text("Usage: /broadcast <message>")
        return
    update.message.reply_text(f"📢 Broadcast Sent:\n\n{msg}", parse_mode=ParseMode.HTML)

# -------- Unknown --------
def unknown(update, context):
    update.message.reply_text("⚠️ Unknown command. Use /command to view all available ones.")

# -------- MAIN --------
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Deal Commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("command", command))
    dp.add_handler(CommandHandler("add", add))
    dp.add_handler(CommandHandler("close", close))
    dp.add_handler(CommandHandler("refund", refund))
    dp.add_handler(CommandHandler("cancel", cancel))
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("history", history))
    dp.add_handler(CommandHandler("ongoing", ongoing))
    dp.add_handler(CommandHandler("mydeals", mydeals))
    dp.add_handler(CommandHandler("notify", notify))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(CommandHandler("stat", stat))
    dp.add_handler(CommandHandler("gstats", gstats))
    dp.add_handler(CommandHandler("topuser", topuser))
    dp.add_handler(CommandHandler("addadmin", addadmin))
    dp.add_handler(CommandHandler("removeadmin", removeadmin))
    dp.add_handler(CommandHandler("adminlist", adminlist))
    dp.add_handler(CommandHandler("broadcast", broadcast))

    dp.add_handler(CommandHandler(None, unknown))
    logger.info("🚀 LB Escrow Bot running 24×7...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
