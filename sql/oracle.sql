SELECT count(*) FROM P_COMUNIDADES_CAMPESINAS;
DELETE FROM P_COMUNIDADES_CAMPESINAS;

SELECT count(*) FROM ANPAdministracionRegional;

INSERT INTO INTEROPERABILIDAD.P_COMUNIDADES_CAMPESINAS (objectid, nom_comuni, nom_dpto, nom_prov, nom_dist, shape) VALUES (sde.gdb_util.next_rowid('INTEROPERABILIDAD', 'P_COMUNIDADES_CAMPESINAS'), 'CAMILACA', 'TACNA', 'CANDARAVE', 'CAMILACA', SDE.ST_POLYFROMTEXT(to_clob('POLYGON ((-70.458008264 -17.077777723,-70.456700716 -17.078174993,-70.455661075 -17.078111348,-70.455483207 -17.079689749,-70.455374853 -17.081039083,-70.454955623 -17.082139222,-70.454015893 -17.083540234,-70.453454422 -17.084687104,-70.452941889 -17.086016478,-70.452525114 -17.087436592,-70.451941098 -17.088743619,-70.451093719 -17.089801105,-70.450245978 -17.090812877,-70.448826283 -17.091623023,-70.448072697 -17.092519829,-70.447272457 -17.09353125,-70.446071022 -17.094911243,-70.445341705 -17.095876438,-70.444776447 -17.096543321,-70.443831466 -17.09728148,-70.442483342 -17.09813679,-70.441159673 -17.099083346,-70.440642977 -17.099887015,-70.440224328 -17.101078554,-70.439591603 -17.102248757,-70.43905534 -17.103601129,-70.438355162 -17.105274662,-70.43776977 -17.106421668,-70.437356178 -17.108276019,-70.436991342 -17.110290023,-70.436958894 -17.112255953,-70.43704353 -17.113992481,-70.436922681 -17.116827603,-70.436845332 -17.119136705,-70.436552311 -17.121218768,-70.436305419 -17.123117648,-70.436060279 -17.125245085,-70.435878722 -17.126366364,-70.43571953 -17.127304629,-70.435462978 -17.127946444,-70.435259402 -17.129296449,-70.43515213 -17.130805769,-70.434853119 -17.132110736,-70.434331482 -17.13538298,-70.433939306 -17.136940033,-70.433687296 -17.138176096,-70.433505368 -17.139251662,-70.433249847 -17.14003061,-70.432993973 -17.140763846,-70.432548279 -17.141544141,-70.432054162 -17.142210493,-70.431186526 -17.143770911,-70.430287756 -17.144371554,-70.428508728 -17.144886989,-70.427013902 -17.145263261,-70.426468722 -17.145472823,-70.425638278 -17.145684395,-70.424995218 -17.145528931,-70.42390032 -17.145353792,-70.421950334 -17.145276093,-70.421095243 -17.145373536,-70.420645663 -17.145650981,-70.420340452 -17.146155981,-70.4199202 -17.147164644,-70.419498555 -17.147990459,-70.4191713 -17.148724183,-70.418584283 -17.149688301,-70.418065975 -17.150309079,-70.417309071 -17.150817245,-70.414277947 -17.152392766,-70.413354094 -17.152833516,-70.411956505 -17.153506144,-70.411057622 -17.154106709,-70.409641245 -17.155442309,-70.408818839 -17.156728045,-70.408331322 -17.158285728,-70.408223489 -17.159749335,-70.408697271 -17.162671739,-70.408348765 -17.163748454,-70.408046942 -17.164710557,-70.407672586 -17.165513166,-70.40717918 -17.166293747,-70.406543295 -17.167098177,-70.40550235 -17.168227168,-70.358936247 -17.166294419,-70.358016988 -17.167453854,-70.356300244 -17.16892618,-70.35531184 -17.169378742,-70.35449803 -17.169645608,-70.353939568 -17.169833875,-70.353318466 -17.170207081,-70.352762454 -17.170733615,-70.352191783 -17.171444767,-70.35174962 -17.17223194,-70.35165889 -17.172955253,-70.351602488 -17.174001246,-70.35151198 -17.17475531,-70.351194536 -17.175095723,-70.350527542 -17.175761386,-70.350147896 -17.176348241,-70.350040162 -17.176933276,-70.350060832 -17.177578959,-70.350128932 -17.178147441,-70.350070741 -17.178947419,-70.34983471 -17.179487183,-70.349565909 -17.179919528,-70.349344424 -17.180259297,-70.349268454 -17.180813366,-70.349287231 -17.181197658,-70.349579266 -17.181764643,-70.349822648 -17.182239692,-70.349923854 -17.182961719,-70.349818233 -17.183838897,-70.349631519 -17.184562851,-70.349096461 -17.185781')||to_clob('189,-70.346507043 -17.188274142,-70.345601269 -17.18911053,-70.345048622 -17.190113703,-70.344798122 -17.190868832,-70.344611606 -17.191623534,-70.344632374 -17.192284594,-70.344989289 -17.192974165,-70.345377533 -17.193571266,-70.34610215 -17.194227627,-70.346586935 -17.194900964,-70.347039508 -17.195543762,-70.347379552 -17.196110427,-70.347608956 -17.196862351,-70.347759047 -17.197707065,-70.348324834 -17.198518245,-70.348732327 -17.199561132,-70.349280902 -17.200203281,-70.350165083 -17.200797049,-70.351097373 -17.201405868,-70.351741051 -17.201924358,-70.352225542 -17.20255155,-70.352953795 -17.20369991,-70.353522978 -17.204972349,-70.354008938 -17.205799423,-70.354225742 -17.20701272,-70.354331797 -17.208395904,-70.354565837 -17.209778227,-70.354714294 -17.210392294,-70.355072964 -17.211312478,-70.355253532 -17.211941705,-70.355484113 -17.212847374,-70.355845593 -17.214151953,-70.356122829 -17.214872788,-70.356656152 -17.215607273,-70.357334473 -17.216479169,-70.357849337 -17.216875489,-70.358443073 -17.21711751,-70.35903445 -17.217036637,-70.359674721 -17.217078445,-70.360046281 -17.217567986,-70.360466063 -17.218087954,-70.360902296 -17.218669317,-70.361388215 -17.219480991,-70.361680917 -17.220124827,-70.361700856 -17.220662873,-70.361753806 -17.221339084,-70.361761689 -17.222415391,-70.361813514 -17.222937843,-70.361883253 -17.223721577,-70.362194667 -17.224734323,-70.36213867 -17.225826438,-70.361968425 -17.226611795,-70.36173283 -17.227213075,-70.361512671 -17.227737368,-70.361391433 -17.228660782,-70.361286983 -17.229691718,-70.361227603 -17.230322559,-70.361060504 -17.231538437,-70.360923489 -17.232492711,-70.360656787 -17.233217213,-70.360150198 -17.233958713,-70.359673579 -17.234423232,-70.359436394 -17.234809249,-70.359360557 -17.235378694,-70.359335532 -17.23633221,-70.359325269 -17.237116484,-70.35933382 -17.238285045,-70.359405248 -17.239299415,-70.359542591 -17.240574741,-70.359613909 -17.241573735,-70.359601848 -17.242111996,-70.358985479 -17.243161768,-70.358655991 -17.244055835,-70.358677055 -17.244747638,-70.358730907 -17.245546854,-70.358913331 -17.246422085,-70.359483269 -17.247771369,-70.36026033 -17.248996236,-70.360891361 -17.249945311,-70.361472478 -17.25063332,-70.362154346 -17.251966459,-70.363237729 -17.253496767,-70.363739311 -17.254246813,-70.363918718 -17.254706891,-70.36397452 -17.255767492,-70.364043613 -17.256458966,-70.364226415 -17.257380316,-70.364489567 -17.258347249,-70.365070952 -17.259065996,-70.36630763 -17.259672651,-70.366694849 -17.260100559,-70.367791941 -17.261307836,-70.369853154 -17.263046711,-70.371911221 -17.264355043,-70.372651311 -17.264888163,-70.375533299 -17.26723642,-70.376520071 -17.268659668,-70.37739381 -17.269945297,-70.37905239 -17.271317791,-70.379843513 -17.272250318,-70.380819694 -17.272243607,-70.38157401 -17.27253057,-70.38268395 -17.27329175,-70.383682565 -17.274145948,-70.384731268 -17.27527657,-70.385489582 -17.276163168,-70.386501069 -17.277257836,-70.387393818 -17.27824852,-70.388567428 -17.279886171,-70.389506917 -17.281274386,-70.390039546 -17.282609626,-70.39129905 -17.284079297,-70.393726612 -17.286433466,-70.395363816 -17.287928377,-70.397751287 -17.288804375,-')||to_clob('70.399643311 -17.289432752,-70.400898928 -17.290372391,-70.401951954 -17.29139712,-70.403500684 -17.292697316,-70.404395634 -17.293919159,-70.406002171 -17.294363437,-70.407267232 -17.294441333,-70.408488292 -17.294671374,-70.409530707 -17.295162967,-70.410302844 -17.295743222,-70.410717031 -17.296759831,-70.410836208 -17.297583287,-70.412333867 -17.298548883,-70.41360227 -17.299060552,-70.414914511 -17.299398368,-70.416342309 -17.300082429,-70.417746872 -17.300679877,-70.418852757 -17.300606979,-70.420135778 -17.300077291,-70.420914224 -17.298531654,-70.42169649 -17.2974849,-70.422139567 -17.296375473,-70.422531814 -17.294528882,-70.422704107 -17.293443067,-70.422649616 -17.292228709,-70.422480737 -17.290819935,-70.422043092 -17.289695059,-70.4212877 -17.288355515,-70.420825828 -17.287013889,-70.420658467 -17.285800327,-70.420652478 -17.285019461,-70.421113788 -17.283345919,-70.421489776 -17.282323737,-70.421727303 -17.280912081,-70.421491217 -17.279568855,-70.421571871 -17.278310153,-70.421584297 -17.276986858,-70.421301404 -17.275427043,-70.421000098 -17.274409656,-70.420700125 -17.273565794,-70.420356666 -17.272939158,-70.420215062 -17.272137558,-70.420297222 -17.271074072,-70.420519369 -17.270010329,-70.422147932 -17.267562811,-70.423506305 -17.265129562,-70.424700011 -17.263043705,-70.425818952 -17.261279875,-70.427241101 -17.258784326,-70.428750434 -17.255917186,-70.430488581 -17.252689811,-70.432343243 -17.249560517,-70.433104897 -17.248207259,-70.434159912 -17.246518039,-70.435072891 -17.244768002,-70.435809251 -17.243476742,-70.436482317 -17.242321952,-70.437677659 -17.24048333,-70.438896318 -17.238335401,-70.440484824 -17.235764394,-70.441296778 -17.23427473,-70.441931852 -17.233206756,-70.442094318 -17.232587321,-70.441893743 -17.231611892,-70.441933791 -17.230140123,-70.441784397 -17.22912723,-70.441713736 -17.22831162,-70.441848741 -17.227469805,-70.442126615 -17.226800083,-70.44248149 -17.226105077,-70.442694549 -17.225373991,-70.442960415 -17.224815642,-70.443159358 -17.223923907,-70.443114714 -17.223145207,-70.442915011 -17.22228106,-70.442599999 -17.221479566,-70.442544028 -17.220898793,-70.4426291 -17.220255182,-70.442662996 -17.219649034,-70.442542027 -17.218982169,-70.442370078 -17.218377496,-70.442372491 -17.217029648,-70.442696153 -17.215630038,-70.442857086 -17.213155802,-70.442961939 -17.211745393,-70.443335035 -17.210085754,-70.44366723 -17.208129638,-70.44385291 -17.207188536,-70.444226281 -17.20556599,-70.444888133 -17.204646204,-70.445165488 -17.203914655,-70.445610845 -17.203280824,-70.445860132 -17.202687576,-70.446306525 -17.201718291,-70.446428705 -17.200751332,-70.446128445 -17.19966275,-70.445530765 -17.197872078,-70.445230657 -17.196659835,-70.444755341 -17.195921709,-70.444381149 -17.195247339,-70.444122524 -17.193615668,-70.444086818 -17.193336506,-70.444047447 -17.192584507,-70.444109777 -17.191971489,-70.44421816 -17.191530092,-70.444360664 -17.191163677,-70.444469379 -17.190765265,-70.44471175 -17.190301413,-70.44507718 -17.189847426,-70.445264483 -17.189491437,-70.445383208 -17.188942496,-70.445457381 -17.188415368,-70.445635474 -17.187323138,-70.445733903 -17.187012248,-70.445848058 -17.186778792,-70')||to_clob('.446007663 -17.186554703,-70.446207941 -17.186373941,-70.446472933 -17.18608609,-70.4467234 -17.185875889,-70.446868895 -17.185782759,-70.447040012 -17.185742759,-70.447191827 -17.185814369,-70.447354103 -17.18593437,-70.447516642 -17.186088295,-70.447699085 -17.186208151,-70.447901318 -17.186279399,-70.448153555 -17.186296974,-70.44839503 -17.186227388,-70.448615444 -17.186150682,-70.449096581 -17.185825354,-70.449539818 -17.185410889,-70.4498534 -17.185068882,-70.450315096 -17.1846364,-70.450665182 -17.184204721,-70.45079219 -17.183792527,-70.45090004 -17.183308944,-70.450858801 -17.18279067,-70.45046595 -17.182507388,-70.450092118 -17.182277613,-70.449513258 -17.181995665,-70.449121105 -17.181801783,-70.448840421 -17.181589218,-70.448633863 -17.181340357,-70.448538079 -17.180983409,-70.448513365 -17.180196789,-70.44850878 -17.179606724,-70.448243645 -17.179000647,-70.447868157 -17.178556298,-70.447492115 -17.178040425,-70.447116631 -17.177596074,-70.446906473 -17.17688231,-70.446787239 -17.175899667,-70.446853456 -17.174844167,-70.446884275 -17.174021383,-70.446800719 -17.172841785,-70.446716609 -17.171590662,-70.446908866 -17.169997805,-70.447119166 -17.16833329,-70.447518511 -17.16706082,-70.447940197 -17.166270997,-70.448401161 -17.165749119,-70.448826451 -17.165424195,-70.449232167 -17.164974239,-70.449544329 -17.164453426,-70.44987495 -17.163914599,-70.449945735 -17.163449164,-70.450106321 -17.162571803,-70.45024775 -17.161623053,-70.450556291 -17.160637339,-70.451069417 -17.159650155,-70.45160364 -17.15898469,-70.452250286 -17.158425706,-70.453145635 -17.157798768,-70.453971169 -17.156805754,-70.45475228 -17.155841667,-70.455297108 -17.155108166,-70.455767985 -17.154432419,-70.455897655 -17.153887879,-70.455892636 -17.153244172,-70.455812444 -17.152500869,-70.455593107 -17.151086213,-70.455265503 -17.149143037,-70.454807123 -17.147601352,-70.454694065 -17.146457732,-70.454702928 -17.145685175,-70.454833934 -17.145312291,-70.455439137 -17.144692801,-70.456668202 -17.143940064,-70.457377762 -17.143348427,-70.458130724 -17.142599116,-70.458554919 -17.141666203,-70.458816686 -17.140891822,-70.459003952 -17.140103673,-70.459116607 -17.139287452,-70.459391236 -17.13825548,-70.459988469 -17.136620352,-70.460305152 -17.135259051,-70.460431782 -17.134328285,-70.460735706 -17.133238879,-70.461101034 -17.13239222,-70.46133448 -17.131804012,-70.461403386 -17.131102549,-70.461353949 -17.130487774,-70.461142322 -17.13006014,-70.461035615 -17.129731887,-70.460736182 -17.129490857,-70.460362479 -17.129264669,-70.459958241 -17.128938563,-70.459688006 -17.128625794,-70.459251451 -17.127970894,-70.459053481 -17.1273858,-70.458795114 -17.126686697,-70.458789759 -17.126000075,-70.458813711 -17.12525602,-70.458926809 -17.124497017,-70.458979285 -17.123595396,-70.45905906 -17.122378859,-70.459226974 -17.121018632,-70.459619587 -17.11985706,-70.459447919 -17.118828307,-70.459572876 -17.117682971,-70.459789317 -17.116823084,-70.460124761 -17.115962338,-70.460625061 -17.115257762,-70.461142242 -17.114810561,-70.461702036 -17.114105554,-70.462022927 -17.113287827,-70.462342139 -17.11225553,-70.462455442 -17.111525135,-70.462746799 -17.110736231,-70.462751952 -')||to_clob('17.109491622,-70.462736308 -17.107488974,-70.46272547 -17.106101426,-70.46286852 -17.105370815,-70.463086165 -17.104668277,-70.463347762 -17.103879588,-70.463802949 -17.10311811,-70.464373886 -17.101940938,-70.464928935 -17.10063513,-70.465529159 -17.099400522,-70.466258765 -17.097592758,-70.466859755 -17.096458279,-70.467540037 -17.095952663,-70.468259455 -17.095458093,-70.468767355 -17.094806075,-70.470002945 -17.094020867,-70.471110609 -17.092758891,-70.471785086 -17.09167919,-70.471777585 -17.090723863,-70.471578214 -17.089053393,-70.471193541 -17.08750369,-70.470566638 -17.086731991,-70.470187129 -17.085839073,-70.470740238 -17.085118525,-70.47178202 -17.083379334,-70.470581651 -17.081817779,-70.469767238 -17.080815216,-70.468911294 -17.079657801,-70.468519856 -17.078593987,-70.467198529 -17.077226602,-70.466024872 -17.076692068,-70.464754347 -17.07666246,-70.463038436 -17.076403334,-70.461789434 -17.076548096,-70.46070218 -17.076749866,-70.459194832 -17.077381315,-70.458008264 -17.077777723),(-70.389132687 -17.244884722,-70.385908635 -17.245884754,-70.378124902 -17.244857463,-70.377973781 -17.224481867,-70.386245809 -17.224704347,-70.386301004 -17.228612134,-70.388183958 -17.228599155,-70.388210826 -17.232196232,-70.390093815 -17.232183232,-70.39017592 -17.243072108,-70.389132687 -17.244884722),(-70.419239046 -17.287056683,-70.419384196 -17.287099584,-70.419285354 -17.287247069,-70.41928915 -17.287640052,-70.419343656 -17.287834201,-70.419432755 -17.287834154,-70.419431737 -17.287793094,-70.419524565 -17.28779185,-70.419557434 -17.287611854,-70.419637966 -17.287469177,-70.419990478 -17.28705215,-70.420107375 -17.287078984,-70.420091015 -17.287275276,-70.41993247 -17.28726779,-70.419914718 -17.287256071,-70.419907662 -17.287263613,-70.419872878 -17.287240531,-70.419676075 -17.287473352,-70.419594395 -17.287618062,-70.419557037 -17.287822642,-70.419563606 -17.287987716,-70.419551952 -17.288071669,-70.419416424 -17.288131099,-70.419423898 -17.288140909,-70.41942618 -17.288154967,-70.419492292 -17.288255519,-70.419497022 -17.288269157,-70.41949937 -17.288295926,-70.419473754 -17.288382578,-70.419440761 -17.288521814,-70.419454383 -17.288590067,-70.419601449 -17.288787712,-70.419594698 -17.288792722,-70.419647531 -17.288855474,-70.419702603 -17.288951653,-70.419661539 -17.288964547,-70.419649982 -17.289147883,-70.419471741 -17.289159043,-70.41944118 -17.289544545,-70.419495289 -17.289544252,-70.419560245 -17.289850249,-70.419563184 -17.289899897,-70.419382833 -17.289909937,-70.419202018 -17.289950337,-70.419172353 -17.289883819,-70.419108947 -17.289888642,-70.418978866 -17.289905071,-70.41895378 -17.289854988,-70.418914526 -17.289741487,-70.418939763 -17.289728653,-70.418903399 -17.289628235,-70.418930639 -17.289414053,-70.419032687 -17.289239138,-70.419041037 -17.289243686,-70.419092247 -17.289155492,-70.419010656 -17.28909328,-70.418904759 -17.289046037,-70.418968863 -17.288832867,-70.41901878 -17.288724754,-70.419090767 -17.288548448,-70.41912572 -17.288488977,-70.419151347 -17.288401072,-70.419154671 -17.288294347,-70.419172211 -17.288230373,-70.419257255 -17.288099812,-70.419292616 -17.288072108,-70.419293798 -17.287771754,-70.419258269')||to_clob(' -17.287649913,-70.419255189 -17.287379165,-70.419040597 -17.287151957,-70.419125067 -17.28707646,-70.419084711 -17.287013853,-70.419123647 -17.286974231,-70.419239046 -17.287056683))'), 4248));

INSERT INTO INTEROPERABILIDAD.P_COMUNIDADES_CAMPESINAS (objectid, nom_comuni, nom_dpto, nom_prov, nom_dist, shape) VALUES (sde.gdb_util.next_rowid('INTEROPERABILIDAD', 'P_COMUNIDADES_CAMPESINAS'), 'K''EHUAR', 'CUSCO', 'None', 'None', SDE.ST_POLYFROMTEXT('POLYGON ((-72.14930777 -13.441222078,-72.149405449 -13.44126446,-72.149469924 -13.441352443,-72.149698565 -13.441791019,-72.149753903 -13.441855865,-72.149988293 -13.441808031,-72.150143192 -13.441763902,-72.150269192 -13.441783663,-72.150383217 -13.441871845,-72.150608344 -13.442256548,-72.151190387 -13.443703695,-72.151494028 -13.444206886,-72.152387115 -13.443844599,-72.153099096 -13.442745302,-72.15333117 -13.442542173,-72.153491086 -13.442534228,-72.153910656 -13.442519374,-72.154312379 -13.442327917,-72.154625533 -13.442017859,-72.154780459 -13.44158841,-72.154886649 -13.441050656,-72.154909699 -13.439918269,-72.154627475 -13.438303718,-72.153331498 -13.438333411,-72.153246408 -13.437888964,-72.152186488 -13.437932882,-72.151562959 -13.437998173,-72.151314211 -13.438074208,-72.150916289 -13.438319357,-72.150476805 -13.438669257,-72.150088588 -13.43809312,-72.149702067 -13.437365892,-72.14937785 -13.436769704,-72.149291547 -13.436709566,-72.149218219 -13.436675859,-72.149090834 -13.436687603,-72.148378258 -13.436909581,-72.147824705 -13.435575661,-72.147429801 -13.434793511,-72.146597315 -13.435175894,-72.145898903 -13.435760669,-72.145113201 -13.436306066,-72.144366957 -13.437251581,-72.143372211 -13.4383219,-72.142706867 -13.439213771,-72.142571125 -13.43961922,-72.142178086 -13.440557085,-72.142050946 -13.441155288,-72.141079541 -13.442153597,-72.140637442 -13.442667744,-72.140027 -13.443308954,-72.140120246 -13.443413703,-72.140276301 -13.443583476,-72.140452711 -13.443701816,-72.140846158 -13.443835447,-72.141319824 -13.443873165,-72.141648928 -13.443876906,-72.142135174 -13.443966429,-72.142411533 -13.443982486,-72.142727153 -13.444018406,-72.142871377 -13.444065294,-72.143046004 -13.443999716,-72.143446098 -13.443868597,-72.143805883 -13.443697095,-72.144265549 -13.443343195,-72.145486889 -13.442527085,-72.146150561 -13.442111728,-72.146705856 -13.441918503,-72.147567358 -13.441675099,-72.147956774 -13.441564714,-72.14883001 -13.441280972,-72.149134778 -13.441220117,-72.14930777 -13.441222078))', 4248))

SELECT objectid, acr_codi, acr_nomb, acr_sect, acr_ubpo, acr_balec, acr_felec, acr_balem, acr_felem, acr_obs, met_link, shape FROM INTEROPERABILIDAD.ANPAdministracionRegional


INSERT INTO INTEROPERABILIDAD.ANPAdministracionRegional 
(objectid, objectid_1, anp_gid, acr_codi, acr_nomb, acr_sect, acr_ubpo, acr_suleg, acr_balec, acr_felec, acr_balem, acr_felem, acr_obs, met_link, acr_orden, shape) VALUES 
(sde.gdb_util.next_rowid('INTEROPERABILIDAD', 'ANPAdministracionRegional'), '3404', 132, 'ACR23', 'Sistema de Lomas de Lima', 'Lomas de Carabayllo2', 'Lima', 198.26, 'D.S. N� 011-2019-MINAM', '31/12/2019', 'None', null, 'None', 'None', 23, SDE.ST_MPOLYFROMTEXT('MULTIPOLYGON (((-77.0863718869999 -11.8178490289999,-77.0874201839999 -11.8184489089999,-77.0892016449999 -11.8186617519999,-77.0902411139999 -11.8190246549999,-77.0906557159999 -11.8190151169999,-77.0906011109999 -11.8186754799999,-77.0901611109999 -11.8179842299999,-77.0897839859999 -11.8164758539999,-77.0899097369999 -11.8154701039999,-77.0918894869999 -11.8120132289999,-77.0920183609999 -11.8115881049999,-77.0920466119999 -11.8115418549999,-77.0930837359999 -11.8087134789999,-77.0930703609999 -11.8068574789999,-77.0922078609999 -11.8035747299999,-77.0851367359999 -11.8017363549999,-77.0822503609999 -11.8008737299999,-77.0806619419999 -11.7996462689999,-77.0805356549999 -11.799586233,-77.0797848349999 -11.7992213599999,-77.0790372559999 -11.7988500839999,-77.0782929739999 -11.7984724359999,-77.0775520449999 -11.7980884429999,-77.0768145239999 -11.7976981329999,-77.0761793099999 -11.7973549399999,-77.0761793109999 -11.7973551199999,-77.0761805169999 -11.797515572,-77.0761822699999 -11.7977489039999,-77.0762616319999 -11.808306801,-77.0778933099999 -11.8083613459999,-77.0778993829999 -11.808361949,-77.077907121 -11.8083639319999,-77.0779145179999 -11.8083672779999,-77.0789929559999 -11.8089790809999,-77.0799789559999 -11.8095384379999,-77.0862621569999 -11.8131027449999,-77.08626849 -11.8131070729999,-77.0862741849999 -11.8131126009999,-77.0862788199999 -11.8131190199999,-77.0862822529999 -11.813126134,-77.0862843799999 -11.8131337269999,-77.0862851299999 -11.8131410849999,-77.0862915989999 -11.8134921479999,-77.0862933759999 -11.8135885929999,-77.0863718869999 -11.8178490289999)))', 4326))



INSERT INTO INTEROPERABILIDAD.ANPAdministracionRegional 
(objectid, objectid_1, anp_gid, acr_codi, acr_nomb, acr_sect, acr_ubpo, acr_suleg, acr_balec, acr_felec, acr_balem, acr_felem, acr_obs, met_link, acr_orden, shape) VALUES 
(sde.gdb_util.next_rowid('INTEROPERABILIDAD', 'ANPAdministracionRegional') , 3468, 135, 'ACR23', 'Sistema de Lomas de Lima', 'Lomas de Carabayllo1', 'Lima', 228.97, 'D.S. N� 011-2019-MINAM', TO_DATE('2019/12/07', 'YYYY/MM/DD'), NULL, NULL, NULL, NULL, 23, SDE.ST_MPOLYFROMTEXT('MULTIPOLYGON (((-77.0863718869999 -11.8178490289999,-77.0874201839999 -11.8184489089999,-77.0892016449999 -11.8186617519999,-77.0902411139999 -11.8190246549999,-77.0906557159999 -11.8190151169999,-77.0906011109999 -11.8186754799999,-77.0901611109999 -11.8179842299999,-77.0897839859999 -11.8164758539999,-77.0899097369999 -11.8154701039999,-77.0918894869999 -11.8120132289999,-77.0920183609999 -11.8115881049999,-77.0920466119999 -11.8115418549999,-77.0930837359999 -11.8087134789999,-77.0930703609999 -11.8068574789999,-77.0922078609999 -11.8035747299999,-77.0851367359999 -11.8017363549999,-77.0822503609999 -11.8008737299999,-77.0806619419999 -11.7996462689999,-77.0805356549999 -11.799586233,-77.0797848349999 -11.7992213599999,-77.0790372559999 -11.7988500839999,-77.0782929739999 -11.7984724359999,-77.0775520449999 -11.7980884429999,-77.0768145239999 -11.7976981329999,-77.0761793099999 -11.7973549399999,-77.0761793109999 -11.7973551199999,-77.0761805169999 -11.797515572,-77.0761822699999 -11.7977489039999,-77.0762616319999 -11.808306801,-77.0778933099999 -11.8083613459999,-77.0778993829999 -11.808361949,-77.077907121 -11.8083639319999,-77.0779145179999 -11.8083672779999,-77.0789929559999 -11.8089790809999,-77.0799789559999 -11.8095384379999,-77.0862621569999 -11.8131027449999,-77.08626849 -11.8131070729999,-77.0862741849999 -11.8131126009999,-77.0862788199999 -11.8131190199999,-77.0862822529999 -11.813126134,-77.0862843799999 -11.8131337269999,-77.0862851299999 -11.8131410849999,-77.0862915989999 -11.8134921479999,-77.0862933759999 -11.8135885929999,-77.0863718869999 -11.8178490289999)))', 4326))

SELECT count(*) FROM all_tables
WHERE owner = 'INTEROPERABILIDAD' AND table_name='ANPADMINISTRACIONREGIONAL1';