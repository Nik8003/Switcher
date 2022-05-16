from PIL import Image, ImageDraw, ImageFont
from FunzioniStarting import PrintaByNik, AggiornaStato
from FunzioniInfoOra import InfoOra
import time

# importing module for logging
import logging

# Create and configure logger
logging.basicConfig(filename="C:/Users/coand/Google Drive/PC/Immagini/Switcher/Log/log.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


####InizioImport

def CreaImmagine(IinfoSfondo):
    L,H=IinfoSfondo.dimSfondo

    Ximm = 1470
    Yimm = 250
    img = Image.open(IinfoSfondo.path + ScegliImmagineDiSfondo(IinfoSfondo.InfoMeteoRoma[1]))
    logger.info(f"  il prog ha aperto l'immagine dal path[{IinfoSfondo.path + 'test1.jpg'}];")
    #
    # d = ImageDraw.Draw(img)
    #
    # d = StampaCalendario(d, L,H, Ximm, Yimm)
    #
    # fnt = ImageFont.truetype('arial.ttf', 19)
    # d.text((Ximm, Yimm), IinfoSfondo.STRINGONA, font=fnt, fill=(255, 255, 255))
    # logger.info("  il prog ha creato immagine da salvare;")

    #AggiornaStato(70)

    return img



def ScegliImmagineDiSfondo(met):
    if met.split()[0] == met.split()[-1]:
        if met == 'sereno':
            #if __name__ == '__main__':print(f"Il meteo è -{met}-")
            nomeImmagine=('fonti/sereno1.jpg')
        elif met == 'coperto':
            #if __name__ == '__main__':print(f"Il meteo è -{met}-")
            nomeImmagine=( 'fonti/coperto.jpg')
        elif met == 'pioggia':
            # if __name__ == '__main__':print(f"Il meteo è -{met}-")
            # img=Image.open(path+'fonti/pioggia.png')
            nomeImmagine = ('fonti/pioggia.jpg')
        elif met == 'temporale':
            # if __name__ == '__main__':print(f"Il meteo è -{met}-")
            # img=Image.open(path+'fonti/pioggia.png')
            nomeImmagine = ('fonti/pioggia.jpg')
        elif met == 'serenissimo':
            #if __name__ == '__main__':print(f"Il meteo è -{met}-")
            # img=Image.open(path+'fonti/pioggia.png')
            nomeImmagine=( 'fonti/serenissimo.jpg')
        else:
            nomeImmagine=( 'fonti/question.jpg')

    elif (met.split()[0] == 'poco' and met.split()[1] == 'nuvoloso'):
        if __name__ == '__main__':print(f"Il meteoF[0] è -{met.split()[0]}- mentre meteoF[1] è -{met.split()[1]}-")
        # img=Image.open(path+'fonti/pioggia.png')
        nomeImmagine=( 'fonti/poconuvoloso1.jpg')

    elif (met.split()[0] == 'pioggia' and met.split()[1] == 'debole'):
        if __name__ == '__main__':print(f"Il meteoF[0] è -{met.split()[0]}- mentre meteoF[1] è -{met.split()[1]}-")
        # img=Image.open(path+'fonti/pioggia.png')
        nomeImmagine=( 'fonti/pioggiadebole.jpg')

    elif (met.split()[0] == 'nubi' and met.split()[1] == 'sparse'):
        if __name__ == '__main__':print(f"Il meteoF[0] è -{met.split()[0]}- mentre meteoF[1] è -{met.split()[1]}-")
        # img=Image.open(path+'fonti/pioggia.png')
        nomeImmagine=( 'fonti/nubisparse.jpg')

    elif (met.split()[0] == 'pioggia' and met.split()[-1] == 'schiarite'):
        if __name__ == '__main__':print(f"Il meteoF[0] è -{met.split()[0]}- mentre meteoF[1] è -{met.split()[-1]}-")
        # img=Image.open(path+'fonti/pioggia.png')
        nomeImmagine=( 'fonti/pioggiaeschiarite.jpg')

    elif (met.split()[0] == 'temporale' and met.split()[-1] == 'schiarite'):
        if __name__ == '__main__':print(f"Il meteoF[0] è -{met.split()[0]}- mentre meteoF[1] è -{met.split()[-1]}-")
        # img=Image.open(path+'fonti/pioggia.png')
        nomeImmagine=( 'fonti/pioggiaeschiarite.jpg')

    elif (met.split()[0] == 'copertocon' and met.split()[-1] == 'piogge'):
        if __name__ == '__main__':print(f"Il meteoF[0] è -{met.split()[0]}- mentre meteoF[1] è -{met.split()[-1]}-")
        # img=Image.open(path+'fonti/pioggia.png')
        nomeImmagine=( 'fonti/copertoconIsolatePiogge.jpg')

    elif (met.split()[0] == 'nubi' and met.split()[-1] == 'piogge'):
        if __name__ == '__main__':print(f"Il meteoF[0] è -{met.split()[0]}- mentre meteoF[1] è -{met.split()[-1]}-")
        # img=Image.open(path+'fonti/pioggia.png')
        nomeImmagine=( 'fonti/copertoconIsolatePiogge.jpg')

    else:
        if __name__ == '__main__':print("Wewe!")
        if __name__ == '__main__':print(
            f"Non sono riuscito ad associare le deguenti due parole: [0] -{met.split()[0]}- e [-1] -{met.split()[-1]}-")
        nomeImmagine=( 'fonti/question.jpg')

    return nomeImmagine

def StampaCalendario(d, path, L, H, Ximm, Yimm, giorniCal=[]):
    fnt = ImageFont.truetype('arial.ttf', 19)
    giorniSettimana =["L", "M", "M", "G", "V", "S", "D"]
    giorniSSettimana = [" Lunedì  ", " Martedì ", "Mercoledì", " Giovedì ", " Venerdì ", "  Sabato ", "Domenica "]

    if len(giorniCal)==0:
        giorniCal=CreaArrayCalendario()

    appuntamentiList=CreaListAppuntamenti(path)

    righe= (len(giorniCal)//7)+3


    passoX= int((L - Ximm)/ 11)
    passoY= int((Yimm)/ righe)
    day=0


    for i in range(righe-1):
        for j in range(7):
            X=int(Ximm + passoX*j) #+ int(passoX / 2)
            Y =passoY * i + int(passoY / 2)
            if i==0:
                if j==0:
                    data = time.gmtime(time.time())
                    if data.tm_mday<10:
                        giorno= '0'+str(data.tm_mday)+'/'
                    else: giorno= str(data.tm_mday)+'/'

                    if data.tm_mon<10:
                        mese= '0'+str(data.tm_mon)+'/'
                    else: mese=str(data.tm_mon)+'/'
                    epoch= giorniSSettimana[data.tm_wday]+' '+giorno+mese+str(data.tm_year) +'  Agg: '+InfoOra()
                    corrx = -40
                    corry = - 6
                    fnt = ImageFont.truetype('arial.ttf', 30)
                    d.text((X+corrx,Y+corry), epoch, font=fnt, fill=(255, 255, 255))



            elif i==1:
                fnt = ImageFont.truetype('arial.ttf', 24)
                d.text((X-4,Y), giorniSettimana[j], font=fnt, fill=(255, 255, 255))

            else:
                fnt = ImageFont.truetype('arial.ttf', 19)
                strDay=giorniCal[day]
                if "X" in strDay:
                    strDay=strDay[:-1]
                    if len(strDay)==1:
                        corrx=0
                    else:
                        corrx = -6
                    corry=-6
                    fnt = ImageFont.truetype('arial.ttf', 34)
                    d.text((X+corrx,Y+corry), strDay, font=fnt, fill=(255, 255, 255))
                    fnt = ImageFont.truetype('arial.ttf', 19)

                    #Date Importanti
                    # fnt = ImageFont.truetype('arial.ttf', 12)
                    # d.text((X + corrx, Y + corry - 5), strDay, font=fnt, fill=(255, 255, 255))
                    # fnt = ImageFont.truetype('arial.ttf', 10)
                    # d.text((X + corrx, Y + corry + 10), "Mamma", font=fnt, fill=(255, 255, 255))
                    # fnt = ImageFont.truetype('arial.ttf', 19)
                else:
                    d.text((X,Y), strDay, font=fnt, fill=(255, 255, 255))
                day+=1

        if i< len(appuntamentiList) and i<6:

            X=int(Ximm + passoX*7) #+ int(passoX / 2)
            Y =passoY * (i+1) + int(passoY / 2)
            fnt = ImageFont.truetype('arial.ttf', 19)

            d.text((X, Y), appuntamentiList[i], font=fnt, fill=(255, 255, 255))



    return d




def CreaArrayCalendario():

    secondiAttuali=time.time()
    data = time.gmtime(secondiAttuali)
    meseAttuale=data.tm_mon
    secPrimoDelMese = int(secondiAttuali) - 3600*24*7*(data.tm_mday//7)- 3600*24*(data.tm_wday)

    c=1
    giorni=0

    listGiorni=[]
    while c==True:
        # print(giorni,": ",sep='', end='')
        sec = secPrimoDelMese + giorni * 3600 * 24
        if giorni>25:
            data = time.gmtime(sec+3600 * 24)
            if data.tm_mon !=meseAttuale and data.tm_wday==0:
                c=False
        data = time.gmtime(sec)
        if sec!= int(secondiAttuali):
            listGiorni.append(str(data.tm_mday))
        else:
            listGiorni.append(str(data.tm_mday) + "X")

        giorni+=1

    # for i in range(len(listGiorni)):
    #     print(listGiorni[i], '', end='')
    #     if i%7==0 and i>1:
    #         print('')

    return listGiorni

def CreaListAppuntamenti(path):

    path+='AppuntamentiFuturi.txt'
    import datetime

    printAll=False
    with open(path, "r") as f:
        x=''
        # while x!= "Close":
        x=f.read()
        x=x.split('\n')
        c=False
        i=0

        listaAppuntamenti=[]
        listaDateAppuntamenti=[]
        while c==False:
            if x[i]=="Close":
                break

            # if printAll==True:
            #     print(x[i])

            AppNome = x[i].split(',')[0]

            AppDataStringa= x[i].split(',')[1]

            AppDataTimestamp=datetime.datetime.strptime(AppDataStringa, " %d/%m/%Y %H:%M").timestamp()-time.time()
            if printAll == True:
                print(f'Per i={i} il temppo in secondi è: {AppDataTimestamp}')
            AppTempoStringa=''
            if int(AppDataTimestamp//(86400*30))>0:
                AppTempoStringa += str(int(AppDataTimestamp // (86400 * 30))) + "M "

            if int(  (AppDataTimestamp%(86400*30))//86400)>0:
                AppTempoStringa += str(int(  (AppDataTimestamp%(86400*30))//86400) ) +"g"

            if (int(   ((AppDataTimestamp%(86400*30))%86400)//3600)  >0) and (int(AppDataTimestamp//(86400*30)))==0:
                if (int(  (AppDataTimestamp%(86400*30))//86400)+int(AppDataTimestamp//(86400*30)))!=0:
                    AppTempoStringa += ' '
                AppTempoStringa +=  str(int(   ((AppDataTimestamp%(86400*30))%86400)//3600)    ) +"h"

            if (int(   (((AppDataTimestamp%(86400*30))%86400)%3600)//60)   >0) and (int(  (AppDataTimestamp%(86400*30))//86400)+int(AppDataTimestamp//(86400*30)))==0:
                AppTempoStringa += ' '+ str(int(   (((AppDataTimestamp%(86400*30))%86400)%3600)//60)     ) +"m"

            if int(AppDataTimestamp)<0:
                AppTempoStringa = "Passato"




            if AppTempoStringa!= "Passato":
                listaAppuntamenti.append(    AppNome+' -> '+ AppTempoStringa    )

            if printAll == True:
                print(f'Per i={i} la lista è: {listaAppuntamenti[i]}')
            i+=1

    if printAll==True:
        print(listaAppuntamenti)

    # listaAppuntamenti=2
    return(listaAppuntamenti)



if __name__ == '__main__':
    # Test della funzione CreaListAppuntamenti
    print(CreaListAppuntamenti(''))
