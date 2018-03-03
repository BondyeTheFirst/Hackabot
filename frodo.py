#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

STARTC, LISTAC, ORGANIZZATOREC, PUBBLICOC, SALEC, DOMANDA1C, I200C, ALTRIMODULIC, FINE, END = range(10)


def start(bot, update):
    reply_keyboard = [['Vedere lista eventi', 'Creare evento']]

    update.message.reply_text(
        'Salve, mi chiamo Frodo. Per poter interagire con me clicca i pulsanti che trovi sullo schermo e assieme potremo vedere cosa ti serve per creare un evento, oppure partecipare ad uno \n\n'
        'Cosa vorresti fare? Ricorda di utilizzare i bottoni in basso per rispondere.\n\n',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return STARTC


def lista(bot, update):
    reply_keyboard = [['No, fa lo stesso', 'Ok, fammi vedere']]

    previous = update.message.text
    update.message.reply_text('A breve i ragazzi dovrebbero fare anche questo...perdona la loro lentezza, sono giovani\n\nAd ogni modo se ti interessa posso aiutarti con la creazione di un evento tuo.',
                              #reply_markup=ReplyKeyboardRemove())
                              reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return LISTAC


def organizzatore(bot, update):
    reply_keyboard = [['Luogo pubblico', 'Sale comunali']]

    previous = update.message.text
    update.message.reply_text('Dove vorresti organizzarlo?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ORGANIZZATOREC


def scuse(bot, update):
    previous = update.message.text
    update.message.reply_text('Mi dispiace non essere stato d\'aiuto.\nBuona giornata!',
                              reply_markup=ReplyKeyboardRemove())

    return END


def pubblico(bot, update):
    reply_keyboard = [['Vorrei organizzarlo prima', 'Non ho fretta']]

    previous = update.message.text
    update.message.reply_text('Ok, ho capito')
    update.message.reply_text('Per questi eventi bisogna avere dei permessi e in alcuni casi è necessario organizzarsi per tempo in quanto l\'emissione di questi permessi richiedono un attesa di 30 giorni.')
    update.message.reply_text('Tieni quindi conto che riuscirai a creare l\'evento non prima del: 02/04/2018\nSe avevi intenzioni di organizzarlo prima, provvederò a metterti in contatto con un addetto dell\'ufficio comunale il quale cercherà di aiutarti.',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return PUBBLICOC


def sale(bot, update):
    reply_keyboard = [['Mostra d\'arte', 'Evento sportivo', 'Serata culturale']]

    previous = update.message.text
    update.message.reply_text('Ok, sono curioso. Che tipo di evento avevi in mente?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return SALEC


def ufficio(bot, update):
    reply_keyboard = [['Luogo pubblico', 'Sale comunali']]

    previous = update.message.text
    update.message.reply_text('Trovi l\'ufficio aperto dal lunedì al venerdi: 8.30/ 12.30 altrimenti chiama al numero 0463/451191 e chiedi di Menapace Dimitri. Lui saprà rispondere alle tue domande')
    update.message.reply_text('Se hai bisogno di informazioni ulteriori o hai dei dubbi da chiarire non esitare a contattare l\'Ufficio Commercio del comune di Tuenno.\nÈ stato un piacere parlare con te. A presto! ',
                              reply_markup=ReplyKeyboardRemove())

    return END


def domanda1(bot, update):
    reply_keyboard = [['Si, anche di piu\'', 'No, saranno meno']]

    previous = update.message.text
    logger.info("Siamo in prima domanda")
    update.message.reply_text('Ottimo. Cominciamo allora. Ti farò alcune domande in modo da poterti aiutare con i moduli da avere.')
    update.message.reply_text('La prima riguarda il numero di persone. Prevedi più di 200 persone?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return DOMANDA1C


def piu200(bot, update):
    reply_keyboard = [['Si, necessito dei moduli', 'No, va bene cosi\'']]

    previous = update.message.text
    logger.info("Siamo in più di 200")
    update.message.reply_text('Ok, Se hai più di 200 partecipanti dovrai consultare la seguente pagina dove troverai il modulo adatto a te.')
    update.message.reply_text('http://www.polizia.provincia.tn.it/eventi/pagina55.html')
    update.message.reply_text('Pensi siano necessari ulteriori servizi per il tuo evento?')
    update.message.reply_text('Potresti aver bisogno di palchi, il patrocinio del comune, della presenza dei vigili del fuoco ecc.?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return I200C


def meno200(bot, update):
    reply_keyboard = [['Si, ho bisogno di questi moduli', 'No, va bene cosi\'']]

    previous = update.message.text
    logger.info("Siamo in meno di 200")
    update.message.reply_text('Perfetto, allora ti lascio il link da cui poter scaricare il modulo')
    update.message.reply_text('http://www.polizia.provincia.tn.it/binary/pat_polizia/eventi/1063_SciaSpettacoli_18ago17.1519652238.pdf')
    update.message.reply_text('Pensi siano necessari ulteriori servizi per il tuo evento?')
    update.message.reply_text('Potresti aver bisogno di palchi, il patrocinio del comune, della presenza dei vigili del fuoco ecc.?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return I200C


def altrimoduli(bot, update):
    reply_keyboard = [['No, penso di avere tutto', 'Si, necessito di aiuto']]

    previous = update.message.text
    update.message.reply_text('Bene, allora ti indirizzo a questo link dove troverai ciò che ti serve per il tuo evento')
    update.message.reply_text('http://www.comune.villedanaunia.tn.it/Servizi-al-cittadino/Commercio-e-Licenze/Eventi-sagre-e-manifestazioni/Come-fare-per-organizzare-feste-e-manifestazioni')
    update.message.reply_text('Hai bisogno d\'altro?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
#TODO: add specific choice
    return ALTRIMODULIC


def nomoduli(bot, update):
    reply_keyboard = [['Si, sei stato all\'altezza', 'No, potevi fare meglio']]

    previous = update.message.text
    update.message.reply_text('Bene, io ho finito. Se ti servono informazioni ulteriori o hai dei dubbi da chiarire non esitare a contattare l\'Ufficio Commercio del comune a Tuenno.')
    update.message.reply_text('Trovi gli uffici aperti dal lunedì al venerdi: 8.30/ 12.30 altrimenti chiama l\'ufficio al numero 0463/451191 e chiedi di Menapace Dimitri. Lui saprà a rispondere ai tuoi dubbi')
    update.message.reply_text('Che dici...sono riuscito a soddisfare almeno qualche tua richiesta?\nIl tuo feedback è importante',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return FINE


def good(bot, update):

    previous = update.message.text
    update.message.reply_text('Ottimo, mi fa piacere essere d\'aiuto. Ci sentiamo qualora avessi ancora bisogno. Buona giornata!',
                              reply_markup=ReplyKeyboardRemove())

    #TODO: store positive feedback

    return END


def bad(bot, update):

    previous = update.message.text
    update.message.reply_text('Mi scuso per il mio sevizio. La prossima volta cercherò di fare di meglio.',
                              reply_markup=ReplyKeyboardRemove())

    #TODO: store negative feedback

    return END


def arte(bot, update):

    update.message.reply_text('Sembra interessante. Per poterti dare dei risultati mi serve però sapere in che mese vorresti organizzarlo.')

    #TODO: implement echo month and than book

    return END


def sport(bot,update):
    return END


def cultura(bot, update):
    return END





def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("553309755:AAEsY_DAtY0VEP6-PQyDzpDISObczlPsTMI")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            STARTC: [RegexHandler('^(Vedere lista eventi)$', lista),
                     RegexHandler('^(Creare evento)$', organizzatore)],

            LISTAC: [RegexHandler('^(No, fa lo stesso)$', scuse),
                     RegexHandler('^(Ok, fammi vedere)$', organizzatore)],

            ORGANIZZATOREC: [RegexHandler('^(Luogo pubblico)$', pubblico),
                             RegexHandler('^(Sale comunali)$', sale)],

            PUBBLICOC: [RegexHandler('^(Vorrei provare ad organizzarlo prima)$', ufficio),
                        RegexHandler('^(Non ho fretta)$', domanda1)],

            DOMANDA1C: [RegexHandler('^(Si, anche di piu\')$', piu200),
                        RegexHandler('^(No, saranno meno)$', meno200)],

            I200C: [RegexHandler('^(Si, necessito dei moduli)$', altrimoduli),
                    RegexHandler('^(No, va bene cosi\')$', nomoduli)],

            ALTRIMODULIC: [RegexHandler('^(Si, necessito di aiuto)$', altrimoduli),
                            RegexHandler('^(No, penso di avere tutto)$', nomoduli)],

            FINE: [RegexHandler('^(Si, sei stato all\'altezza)$', good),
                            RegexHandler('^(No, potevi fare meglio)$', bad)],

            SALEC: [RegexHandler('^(Mostra d\'arte)$', arte),
                    RegexHandler('^(Evento sportivo)$', sport),
                     RegexHandler('^(Serata culturale)$', cultura)]


        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
