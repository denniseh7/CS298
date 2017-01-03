import tweepy
import json

#livestream from twitter for drug name

consumer_token="bY6PVmVwyn4mOvhpSG9YVJ3B8"
consumer_secret="Q7EZmDgwi4DWJwkL9jGoRZgDje2YFUqU4T1UZBymqYeXbqGq1H"

access_token="418316899-u8cdzS5kAMkgYCCv8eJncbKQa21jZHJj1IjBwyeg"
access_secret="B3LoHnA6fx1dXLBpkrfRBZO1Wx44kvjxZwFPRMEP7xwsf"

consumer_token2="Q4CWexZYjMIODDoFw0qphrTee"
consumer_secret2="Bwqc321nYLCQhZSsjLMaWuhamhJ92RyACLKsJRhXg3BntoYWdu"

access_token2="418316899-3lFEwwJT8CWz5vSv9EIM6RkhwWvobQ3aygEF6Tnf"
access_secret2="065RNxxvhq7Z62q7uDlawIhNsYZFfzDEQbbYyEMhZNBDP"

#authentication
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token,access_secret)

auth2 = tweepy.OAuthHandler(consumer_token2, consumer_secret2)
auth2.set_access_token(access_token2,access_secret2)

api = tweepy.API(auth)
api2 = tweepy.API(auth2)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.count=0

    def on_data(self, raw_data):
        if raw_data is not None:
            json_data = json.loads(raw_data)
            if "user" in json_data:
                if(int(json_data['user']['followers_count'])<10001):
                    tweet=json_data['text']
                    if "http" not in tweet:
                        output=' '.join(tweet.split())
                        output+='\n'
                        f = open('drugtweet13.txt', 'ab')
                        f.write(output.encode('utf-8'))
                        f.close()

                        self.count += 1
                        if(self.count%500==0):
                            print(str(self.count)+' '+output)


    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False



myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['Abilify,Acetaminophen,Acyclovir,Adderall,Albuterol,Aleve,Allopurinol,Alprazolam,Ambien,Amiodarone,Amitriptyline,Amlodipine,Amoxicillin,Aricept,Aspirin,Atenolol,Ativan,Atorvastatin,Augmentin,Azithromycin,Baclofen,Bactrim,Bactroban,Belsomra,Benadryl,Benicar,Biaxin,Bisoprolol,Boniva,Boniva,Breo Ellipta,Brilinta,Brovana,Bupropion,Buspar,Buspirone,Butrans,Bydureon,Bystolic,Cardizem,Carvedilol,Celebrex,Celexa,Cephalexin,Cetirizine,Cialis,Cipro,Ciprofloxacin,Citalopram,Claritin,Clindamycin,Clonazepam,Clonidine,Coreg,Coumadin,Cozaar,Crestor,Cyclobenzaprine,Cymbalta,Demerol,Depakote,Detrol,Dexamethasone,Dextromethorphan,Diazepam,Diclofenac,Diflucan,Digoxin,Dilantin,Dilaudid,Diltiazem,Diovan,Diphenhydramine,Ditropan,Doxazosin,Doxycycline,Dulera,DuoNeb,Dyazide,Effexor,Effient,Elavil,Eligard,Eliquis,Enalapril,Enbrel,Endocet,Entresto,EpiPen,Epogen,Erythromycin,Estrace,Estradiol,Etodolac,Evista,Excedrin,Exelon,Exforge,Ezetimibe,Famotidine,Farxiga,Faslodex,Femara,Fenofibrate,Fentanyl,Ferrous Sulfate,Fioricet,Flagyl,Flexeril,Flomax,Flonase,Flovent,Fluoxetine,Focalin,Folic Acid,Forteo,Fosamax,Furosemide,Gabapentin,Gammagard,Garcinia Cambogia,Gardasil,Gemfibrozil,Gemzar,Genvoya,Geodon,Gilenya,Gilotrif,Gleevec,Glipizide,Glucophage,Glucotrol,Glucovance,Glyburide,Glyxambi,Gralise,Guaifenesin,Guaifenex,Halaven,Harvoni,Havrix,Hcg,Heparin,Herceptin,Hetlioz,Hizentra,Horizant,Humalog,Humira,Humulin,Humulin N,Hydrochlorothiazide,Hydrocodone,Hydroxychloroquine,Hydroxyzine,Hysingla ER,Hytrin,Hyzaar,Ibrance,Ibuprofen,Imbruvica,Imdur,Imitrex,Imodium,Implanon,Incruse Ellipta,Inderal,Injectafer,Inlyta,Insulin,Intelence,Intuniv,Invega,Invokamet,Invokana,Iressa,Isentress,Isosorbide,Jakafi,Jalyn,Janumet,Januvia,Jardiance,Jentadueto,Jetrea,Jevtana,Jublia,Juvederm,Juvisync,Juxtapid,K-dur,Kadcyla,Kadian,Kaletra,Kalydeco,Kapidex,Kapvay'], languages=['en'], async=True)

myStreamListener2 = MyStreamListener()
myStream2 = tweepy.Stream(auth = api2.auth, listener=myStreamListener2)

#Testosterone, Yaz, Yasmin?
myStream2.filter(track=['Glatiramer,Duloxetine,Kazano,Keflex,Kenalog,Keppra,Kerydin,Keytruda,Kineret,Klonopin,Klor-con,Kombiglyze XR,Krill Oil,Kyprolis,Kytril,Lamictal,Lansoprazole,Lasix,Latuda,Levaquin,Levothyroxine,Levoxyl,Lexapro,Lidoderm,Linzess,Lipitor,Lisinopril,Loratadine,Lorazepam,Losartan,Lovenox,Lumigan,Lupron,Lyrica,Macrobid,Meclizine,Melatonin,Meloxicam,Metformin,Methadone,Methocarbamol,Methotrexate,Methylphenidate,Methylprednisolone,Metoclopramide,Metoprolol,Metronidazole,MiraLax,Mirtazapine,Mobic,Morphine,Motrin,Mucinex,Myrbetriq,Naloxone,Namenda,Naprosyn,Naproxen,Nasacort,Nasonex,Neulasta,Neurontin,Nexium,Niacin,Niaspan,Nicotine,Nifedipine,Nitrofurantoin,Norco,Nortriptyline,Norvasc,NovoLog,Nucynta,Nuvigil,Ofev,Omeprazole,Omnicef,Ondansetron,Onfi,Onglyza,Opana,Opdivo,Opsumit,Orencia,Orlistat,Ortho Tri-Cyclen,Orthovisc,Oseltamivir,Osphena,Otezla,Oxybutynin,Oxycodone,Oxycontin,Oxytrol,Paroxetine,Paxil,Pepcid,Percocet,Phenergan,Plaquenil,Plavix,Potassium Chloride,Pradaxa,Pravachol,Pravastatin,Prednisone,Pregabalin,Premarin,Prevacid,Prilosec,Prolia,Promethazine,Propranolol,Protonix,Prozac,QNASL,Qsymia,Quillivant XR,Qutenza,Ramipril,Ranexa,Ranitidine,Rapaflo,Reclast,Reglan,Relafen,Remeron,Remicade,Renvela,Requip,Restasis,Restoril,Revlimid,Risperdal,risperidone,Ritalin,Rituxan,Robaxin,Rocephin,Saphris,Savella,Sensipar,Septra,Seroquel,Sertraline,Sildenafil,Simvastatin,Singulair,Skelaxin,Spiriva,Spironolactone,Stiolto Respimat,Strattera,Suboxone,Symbicort,Synthroid,Tamoxifen,Tamsulosin,Tegretol,Temazepam,Terazosin,,Tizanidine,Topamax,Toprol,Toradol,Tradjenta,Tramadol,Travatan,Trazodone,Triamcinolone,Triamterene,Tricor,Trileptal,Trintellix,Tylenol,Uceris,Ulesfia,Uloric,Ultane,Ultracet,Ultram,Ultresa,Uptravi,Uroxatral,Utibron Neohaler,Valacyclovir,Valium,Valtrex,Vancomycin,Vasotec,Venlafaxine,Ventolin,Verapamil,Vesicare,Vicodin,Victoza,Viibryd,Vimpat,Vistaril,Vitamin E,Voltaren,Voltaren Gel,Vytorin,Vyvanse,Warfarin,Wellbutrin,Wilate,Xalatan,Xalkori,Xanax,Xanax XR,Xarelto,Xeljanz,Xeloda,Xenazine,Xenical,Xeomin,Xgeva,Xifaxan,Xigduo XR,Xiidra,Xofigo,Xolair,Xopenex,Xtandi,Xyrem,Xyzal,Yervoy,Yondelis,Yosprala,Zanaflex,Zantac,Zemplar,Zestoretic,Zestril,Zetia,Ziac,Zithromax,Zocor,Zofran,Zoloft,Zolpidem,Zometa,Zostavax,Zosyn,Zovirax,Zyprexa,Zyrtec,Zytiga,Zyvox'],languages=['en'],async=True)