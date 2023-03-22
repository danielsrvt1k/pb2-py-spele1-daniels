# ASCII art Spēle "Karātavas"
Šajā kodā ir izveidota spēle "Karātavas", kur spēlētājam jāmin nejauši izvēlēts vārds no vārdu saraksta. Spēlētājam ir pieejamas 5 dzīvības, lai uzminētu vārdu, un spēle beidzas, ja spēlētājs uzmin vārdu vai izmanto visas dzīvības.

ASCII art tiek izmantots, lai parādītu spēles stāvokli, piemēram, parādot zaudējumu stāvokli, ja spēlētājs ir izmantojis visas dzīvības. Neuzminētie burti tiek parādīti ar apakšsvītrām, un spēlētājam tiek lūgts ievadīt burtu, lai mēģinātu uzminēt vārdu vēlreiz.

Vispirms kodā ir definēti iespējamie vārdi saraksts un pēc nejaušības principa tiek izvēlēts viens no iespējamajiem vārdiem. Tad vārds tiek pārveidots uz lielajiem burtiem, jeb CAPS un tiek izveidots tukšs saraksts, lai saglabātu spēlētāja minētos burtus. Tiek arī definēts mēģinājumu / dzīvību skaits: 5 dzīvības.

Spēlētājam tiek lūgts ievadīt burtu, un pēc tam tiek pārbaudīts, vai burts jau ir izmantots iepriekš, vai burts ietilpst vārdā. Ja burts ir pareizs, tas tiek pievienots uzminēto burtu sarakstam, bet ja burts ir nepareizs vai atkārtojās bez nepieciešamības, tad spēlētājam tiek atņemta dzīvība.

Spēle beidzas, ja spēlētājs ir uzminējis vārdu, un visi burti ir uzminēti, vai arī tad kad spēlētājs ir izmantojis visas savas dzīvības. ASCII art tiek izmantots, lai parādītu zaudējuma stāvokli, ja spēlētājs ir izmantojis visas dzīvības, kā arī kalpo kā grafiskais dizains šai spēlei.

Manuprāt kods ir labs piemērs spēļu izveidei ar "PARASTO Python", izmantojot ASCII art, un ir piemērots arī jaunajiem programmētājiem jeb jaunajiem developeriem (videospēļu izstrādātājiem).
