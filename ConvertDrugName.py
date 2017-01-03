namelist=["abilify","acetaminophen","acyclovir","adderall","albuterol","aleve","allopurinol","alprazolam","ambien","amiodarone","amitriptyline","amlodipine","amoxicillin","aricept","aspirin","atenolol","ativan","atorvastatin","augmentin","azithromycin","baclofen","bactrim","bactroban","belsomra","benadryl","benicar","biaxin","bisoprolol","boniva","boniva","breo ellipta","brilinta","brovana","bupropion","buspar","buspirone","butrans","bydureon","bystolic","cardizem","carvedilol","celebrex","celexa","cephalexin","cetirizine","cialis","cipro","ciprofloxacin","citalopram","claritin","clindamycin","clonazepam","clonidine","coreg","coumadin","cozaar","crestor","cyclobenzaprine","cymbalta","demerol","depakote","detrol","dexamethasone","dextromethorphan","diazepam","diclofenac","diflucan","digoxin","dilantin","dilaudid","diltiazem","diovan","diphenhydramine","ditropan","doxazosin","doxycycline","dulera","duoneb","dyazide","effexor","effient","elavil","eligard","eliquis","enalapril","enbrel","endocet","entresto","epipen","epogen","erythromycin","estrace","estradiol","etodolac","evista","excedrin","exelon","exforge","ezetimibe","famotidine","farxiga","faslodex","femara","fenofibrate","fentanyl","ferrous sulfate","fioricet","flagyl","flexeril","flomax","flonase","flovent","fluoxetine","focalin","folic acid","forteo","fosamax","furosemide","gabapentin","gammagard","garcinia cambogia","gardasil","gemfibrozil","gemzar","genvoya","geodon","gilenya","gilotrif","gleevec","glipizide","glucophage","glucotrol","glucovance","glyburide","glyxambi","gralise","guaifenesin","guaifenex","halaven","harvoni","havrix","hcg","heparin","herceptin","hetlioz","hizentra","horizant","humalog","humira","humulin","humulin n","hydrochlorothiazide","hydrocodone","hydroxychloroquine","hydroxyzine","hysingla er","hytrin","hyzaar","ibrance","ibuprofen","imbruvica","imdur","imitrex","imodium","implanon","incruse ellipta","inderal","injectafer","inlyta","insulin","intelence","intuniv","invega","invokamet","invokana","iressa","isentress","isosorbide","jakafi","jalyn","janumet","januvia","jardiance","jentadueto","jetrea","jevtana","jublia","juvederm","juvisync","juxtapid","k-dur","kadcyla","kadian","kaletra","kalydeco","kapidex","kapvay","glatiramer","duloxetine","kazano","keflex","kenalog","keppra","kerydin","keytruda","kineret","klonopin","klor-con","kombiglyze xr","krill oil","kyprolis","kytril","lamictal","lansoprazole","lasix","latuda","levaquin","levothyroxine","levoxyl","lexapro","lidoderm","linzess","lipitor","lisinopril","loratadine","lorazepam","losartan","lovenox","lumigan","lupron","lyrica","macrobid","meclizine","melatonin","meloxicam","metformin","methadone","methocarbamol","methotrexate","methylphenidate","methylprednisolone","metoclopramide","metoprolol","metronidazole","miralax","mirtazapine","mobic","morphine","motrin","mucinex","myrbetriq","naloxone","namenda","naprosyn","naproxen","nasacort","nasonex","neulasta","neurontin","nexium","niacin","niaspan","nicotine","nifedipine","nitrofurantoin","norco","nortriptyline","norvasc","novolog","nucynta","nuvigil","ofev","omeprazole","omnicef","ondansetron","onfi","onglyza","opana","opdivo","opsumit","orencia","orlistat","ortho tri-cyclen","orthovisc","oseltamivir","osphena","otezla","oxybutynin","oxycodone","oxycontin","oxytrol","paroxetine","paxil","pepcid","percocet","phenergan","plaquenil","plavix","potassium chloride","pradaxa","pravachol","pravastatin","prednisone","pregabalin","premarin","prevacid","prilosec","prolia","promethazine","propranolol","protonix","prozac","qnasl","qsymia","quillivant xr","qutenza","ramipril","ranexa","ranitidine","rapaflo","reclast","reglan","relafen","remeron","remicade","renvela","requip","restasis","restoril","revlimid","risperdal","risperidone","ritalin","rituxan","robaxin","rocephin","saphris","savella","sensipar","septra","seroquel","sertraline","sildenafil","simvastatin","singulair","skelaxin","spiriva","spironolactone","stiolto respimat","strattera","suboxone","symbicort","synthroid","tamoxifen","tamsulosin","tegretol","temazepam","terazosin","","tizanidine","topamax","toprol","toradol","tradjenta","tramadol","travatan","trazodone","triamcinolone","triamterene","tricor","trileptal","trintellix","tylenol","uceris","ulesfia","uloric","ultane","ultracet","ultram","ultresa","uptravi","uroxatral","utibron neohaler","valacyclovir","valium","valtrex","vancomycin","vasotec","venlafaxine","ventolin","verapamil","vesicare","vicodin","victoza","viibryd","vimpat","vistaril","vitamin e","voltaren","voltaren gel","vytorin","vyvanse","warfarin","wellbutrin","wilate","xalatan","xalkori","xanax","xanax xr","xarelto","xeljanz","xeloda","xenazine","xenical","xeomin","xgeva","xifaxan","xigduo xr","xiidra","xofigo","xolair","xopenex","xtandi","xyrem","xyzal","yervoy","yondelis","yosprala","zanaflex","zantac","zemplar","zestoretic","zestril","zetia","ziac","zithromax","zocor","zofran","zoloft","zolpidem","zometa","zostavax","zosyn","zovirax","zyprexa","zyrtec","zytiga","zyvox"]
with open('traindataset1.txt') as f:
    for line in f:
        testline=line.split()
        output=[]
        outline=""
        for word in testline:
            if word in namelist:
                output.append("drug")
            else:
                output.append(word)

        outline=' '.join(output)
        print(outline)
        outline+='\n'
        f = open('traindatasetdrug1.txt', 'a')
        f.write(outline)
        f.close()




