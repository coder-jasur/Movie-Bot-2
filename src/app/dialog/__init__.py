from aiogram import Dispatcher, Router

from src.app.dialog.dialogs import op_management_dialog, channel_management_dialog, bot_management_dialog


def dialog_register(dp: Dispatcher):
    dialog_register_router = Router()

    dialog_register_router.include_router(op_management_dialog)
    dialog_register_router.include_router(bot_management_dialog)
    dialog_register_router.include_router(channel_management_dialog)



    dp.include_router(dialog_register_router)